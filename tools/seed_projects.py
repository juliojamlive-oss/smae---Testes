import os
import random
import datetime
from faker import Faker
import psycopg2

# Configuração do Faker
fake = Faker('pt_BR')

# Configuração do Banco de Dados
# Tenta pegar do ambiente, ou usa defaults
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "smae_dev_persistent")
DB_USER = os.getenv("POSTGRES_USER", "smae")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "smae")

# Quantidade de registros
NUM_PROJETOS = 100
TASKS_PER_PROJECT = 20
RISKS_PER_PROJECT = 5
CONTRACTS_PER_PROJECT = 2

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        print("Verifique se as variáveis de ambiente ou configurações padrão estão corretas.")
        return None

def create_dependencies(cursor):
    """Cria dados básicos necessários para os projetos (Pessoas, Orgãos, Tipos)"""
    print("Verificando/Criando dependências...")

    # 1. Garantir TipoOrgao
    cursor.execute("INSERT INTO tipo_orgao (descricao) VALUES ('Secretaria') ON CONFLICT DO NOTHING RETURNING id")
    tipo_orgao_id = cursor.fetchone()
    if not tipo_orgao_id:
        cursor.execute("SELECT id FROM tipo_orgao LIMIT 1")
        tipo_orgao_id = cursor.fetchone()[0]
    else:
        tipo_orgao_id = tipo_orgao_id[0]

    # 2. Criar ou Pegar Orgãos
    orgaos_ids = []
    for _ in range(5):
        cursor.execute(
            """
            INSERT INTO orgao (sigla, descricao, tipo_orgao_id, oficial)
            VALUES (%s, %s, %s, true)
            RETURNING id
            """,
            (fake.unique.company_suffix().upper(), fake.company(), tipo_orgao_id)
        )
        orgaos_ids.append(cursor.fetchone()[0])

    # 3. Criar Pessoa (Gestor)
    cursor.execute(
        """
        INSERT INTO pessoa (email, senha, nome_exibicao, nome_completo)
        VALUES (%s, 'hash_senha_dummy', %s, %s)
        ON CONFLICT (email) DO UPDATE SET nome_exibicao = EXCLUDED.nome_exibicao
        RETURNING id
        """,
        (fake.email(), fake.first_name(), fake.name())
    )
    pessoa_id = cursor.fetchone()[0]

    # 4. Criar Portfolio
    cursor.execute(
        """
        INSERT INTO portfolio (titulo, criado_por, criado_em)
        VALUES (%s, %s, NOW())
        RETURNING id
        """,
        (f"Portfólio Simulação {fake.word()}", pessoa_id)
    )
    portfolio_id = cursor.fetchone()[0]

    return orgaos_ids, pessoa_id, portfolio_id

def seed_projects():
    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()

        orgaos_ids, pessoa_id, portfolio_id = create_dependencies(cur)

        print(f"Iniciando inserção de {NUM_PROJETOS} projetos...")

        for i in range(NUM_PROJETOS):
            # Status e Fase
            status_opts = ['EmPlanejamento', 'EmAcompanhamento', 'Fechado', 'Suspenso']
            status = random.choice(status_opts)

            fase = 'Planejamento'
            iniciado_em = None
            terminado_em = None

            if status == 'EmAcompanhamento' or status == 'Suspenso':
                fase = 'Acompanhamento'
                iniciado_em = fake.date_between(start_date='-1y', end_date='today')
            elif status == 'Fechado':
                fase = 'Encerramento'
                iniciado_em = fake.date_between(start_date='-2y', end_date='-1y')
                terminado_em = fake.date_between(start_date='-1y', end_date='today')

            # --- 1. Projeto ---
            # Campos ajustados conforme schema.prisma
            # REQUER: portfolio_id, nome, objeto, objetivo, publico_alvo, resumo
            cur.execute(
                """
                INSERT INTO projeto (
                    portfolio_id,
                    nome, objeto, objetivo, publico_alvo,
                    resumo, escopo, nao_escopo,
                    orgao_gestor_id, orgao_responsavel_id, responsavel_id,
                    status, fase, registrado_em, registrado_por,
                    iniciado_em, terminado_em,
                    origem_tipo, origem_eh_pdm
                ) VALUES (
                    %s,
                    %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s,
                    %s::"ProjetoStatus", %s::"ProjetoFase", NOW(), %s,
                    %s, %s,
                    'Outro', false
                ) RETURNING id
                """,
                (
                    portfolio_id,
                    fake.catch_phrase(),
                    fake.text(max_nb_chars=200), # objeto (html sim)
                    fake.text(max_nb_chars=200), # objetivo (html sim)
                    fake.text(max_nb_chars=100), # publico_alvo
                    fake.text(max_nb_chars=100), # resumo
                    fake.text(max_nb_chars=500), # escopo
                    fake.text(max_nb_chars=200), # nao_escopo
                    random.choice(orgaos_ids), # Gestor
                    random.choice(orgaos_ids), # Responsavel
                    pessoa_id,
                    status,
                    fase,
                    pessoa_id,
                    iniciado_em,
                    terminado_em
                )
            )
            projeto_id = cur.fetchone()[0]

            # --- 2. Cronograma ---
            # Cronograma está mais ligado a metas, mas vamos criar para manter compatibilidade
            cur.execute(
                """
                INSERT INTO cronograma (
                    descricao, inicio_previsto, termino_previsto,
                    regionalizavel, criado_por
                ) VALUES (%s, %s, %s, false, %s) RETURNING id
                """,
                (
                    f"Cronograma do Projeto {projeto_id}",
                    datetime.date.today(),
                    datetime.date.today() + datetime.timedelta(days=365),
                    pessoa_id
                )
            )
            cronograma_id = cur.fetchone()[0]

            # --- 3. Tarefas (TarefaCronograma e Tarefa) ---

            for _ in range(TASKS_PER_PROJECT):
                # Criar TarefaCronograma (Ligação com Projeto)
                cur.execute(
                    """
                    INSERT INTO tarefa_cronograma (
                        projeto_id, previsao_inicio, previsao_termino,
                        previsao_duracao, criado_por
                    ) VALUES (%s, %s, %s, %s, %s) RETURNING id
                    """,
                    (
                        projeto_id,
                        fake.date_between(start_date='-1m', end_date='+1m'),
                        fake.date_between(start_date='+1m', end_date='+3m'),
                        random.randint(5, 30),
                        pessoa_id
                    )
                )
                tarefa_crono_id = cur.fetchone()[0]

                # Criar Tarefa (Detalhe)
                cur.execute(
                    """
                    INSERT INTO tarefa (
                        tarefa_cronograma_id, tarefa, descricao, recursos,
                        numero, nivel, inicio_planejado, termino_planejado
                    ) VALUES (%s, %s, %s, %s, %s, 1, %s, %s)
                    """,
                    (
                        tarefa_crono_id,
                        fake.sentence(nb_words=3),
                        fake.sentence(nb_words=10),
                        fake.name(),
                        random.randint(1, 100),
                        datetime.date.today(),
                        datetime.date.today() + datetime.timedelta(days=10)
                    )
                )

            # --- 4. Riscos ---
            for _ in range(RISKS_PER_PROJECT):
                cur.execute(
                    """
                    INSERT INTO projeto_risco (
                        projeto_id, titulo, codigo, registrado_em,
                        descricao, causa, consequencia, probabilidade, impacto,
                        status_risco, criado_em, criado_por
                    ) VALUES (
                        %s, %s, %s, NOW(),
                        %s, %s, %s, %s, %s,
                        'Estatico'::"StatusRisco", NOW(), %s
                    ) RETURNING id
                    """,
                    (
                        projeto_id,
                        fake.sentence(nb_words=4),
                        random.randint(1000, 9999),
                        fake.paragraph(),
                        fake.sentence(),
                        fake.sentence(),
                        random.randint(1, 5),
                        random.randint(1, 5),
                        pessoa_id
                    )
                )
                risco_id = cur.fetchone()[0]

                # Plano de Ação
                cur.execute(
                    """
                    INSERT INTO plano_acao (
                        projeto_risco_id, contramedida, medidas_de_contingencia,
                        responsavel, criado_em, criado_por
                    ) VALUES (%s, %s, %s, %s, NOW(), %s)
                    """,
                    (
                        risco_id,
                        fake.sentence(),
                        fake.sentence(),
                        fake.name(),
                        pessoa_id
                    )
                )

            # --- 5. Contratos ---
            # Primeiro garantir modalidade
            cur.execute("INSERT INTO modalidade_contratacao (nome, criado_por, criado_em) VALUES ('Concorrência', %s, NOW()) ON CONFLICT DO NOTHING RETURNING id", (pessoa_id,))
            mod_id_res = cur.fetchone()
            mod_id = mod_id_res[0] if mod_id_res else 1

            for _ in range(CONTRACTS_PER_PROJECT):
                cur.execute(
                    """
                    INSERT INTO contrato (
                        projeto_id, modalidade_contratacao_id, numero,
                        contrato_exclusivo, status, objeto_resumo,
                        empresa_contratada, valor, criado_por, criado_em
                    ) VALUES (
                        %s, %s, %s,
                        true, 'Vigente'::"StatusContrato", %s,
                        %s, %s, %s, NOW()
                    )
                    """,
                    (
                        projeto_id,
                        mod_id,
                        str(fake.random_number(digits=8)),
                        fake.sentence(),
                        fake.company(),
                        random.uniform(10000, 1000000),
                        pessoa_id
                    )
                )

            if i % 10 == 0:
                print(f"Processado {i}/{NUM_PROJETOS} projetos...")
                conn.commit()

        conn.commit()
        print(f"Sucesso! {NUM_PROJETOS} projetos inseridos com dados relacionados.")

    except Exception as e:
        conn.rollback()
        print(f"Erro durante a execução do script: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == "__main__":
    seed_projects()
