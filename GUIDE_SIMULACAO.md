# Guia de Simulação de Dados - SMAE

Este guia descreve como popular o banco de dados local com 100 projetos fictícios para testes de performance e prototipação de painéis BI.

## Pré-requisitos

1.  **Banco de Dados PostgreSQL**:
    *   Certifique-se de que o banco de dados está rodando.
    *   Se estiver usando o Docker da aplicação: `docker compose up -d db`.
    *   Se for um Postgres local instalado na máquina, verifique se o serviço está ativo.

2.  **Python 3**:
    *   Necessário para rodar o script de seed.

## Passo a Passo

### 1. Preparar o Ambiente Python

Navegue até a pasta `tools/` e instale as dependências necessárias:

```bash
cd tools/
pip install -r requirements.txt
```

> **Nota:** Recomenda-se usar um ambiente virtual (venv) para não poluir seu python global.
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> ```

### 2. Configurar Conexão com o Banco

O script `seed_projects.py` busca as configurações nas variáveis de ambiente. Se você estiver usando os valores padrão do `docker-compose.yml`, não precisa configurar nada.

Caso seu banco tenha senha ou porta diferente, exporte as variáveis antes de rodar:

```bash
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_DB=smae_dev_persistent
export POSTGRES_USER=smae
export POSTGRES_PASSWORD=smae
```

### 3. Executar a Simulação

Rode o script:

```bash
python3 seed_projects.py
```

O script irá:
1.  Verificar se existem Tipos de Órgão e criar se necessário.
2.  Criar 5 Órgãos fictícios (Secretarias).
3.  Criar 1 Usuário Admin fictício (se não existir).
4.  Inserir **100 Projetos** com:
    *   Status variados (Em Planejamento, Em Execução, etc).
    *   Datas aleatórias.
    *   **20 Tarefas** de cronograma por projeto.
    *   **5 Riscos** por projeto, cada um com Plano de Ação.
    *   **2 Contratos** por projeto.

### 4. Verificar os Dados

Acesse o banco de dados para confirmar a inserção:

```bash
# Se estiver usando Docker
docker exec -it smae_postgres psql -U smae -d smae_dev_persistent -c "SELECT count(*) FROM projeto;"

# Se estiver local
psql -U smae -d smae_dev_persistent -c "SELECT count(*) FROM projeto;"
```

Você deve ver um número superior a 100 (contando os que já existiam).

### 5. Monitorar Espaço em Disco

Para verificar o tamanho das tabelas geradas no Postgres:

```sql
SELECT
    table_name,
    pg_size_pretty(pg_total_relation_size(quote_ident(table_name))) as total_size
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY pg_total_relation_size(quote_ident(table_name)) DESC
LIMIT 10;
```

A estimativa é que essa carga de dados ocupe menos de **100 MB**, bem abaixo do limite de 500 MB.

---

**Observação:** O script pode ser rodado múltiplas vezes. Ele sempre adicionará mais 100 projetos a cada execução.
