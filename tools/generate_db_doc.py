import re
import os

SCHEMA_PATH = "backend/prisma/schema.prisma"
OUTPUT_PATH = "TABELAS_ORIGEM.md"

# Mapeamento manual de tabelas para Módulos/Origens
MODULE_MAPPING = {
    'Gestão de Projetos': {
        'tables': [
            'Projeto', 'ProjetoEtapa', 'ProjetoRisco', 'ProjetoAcompanhamento',
            'ProjetoPremissa', 'ProjetoRestricao', 'ProjetoLicaoAprendida',
            'ProjetoFonteRecurso', 'ProjetoDocumento', 'ProjetoTag',
            'ProjetoOrgaoParticipante', 'ProjetoPessoaRevisao', 'Empreendimento',
            'Contrato', 'ContratoAditivo', 'ContratoFonteRecurso', 'ContratoSei',
            'TipoIntervencao', 'Equipamento', 'TipoAditivo', 'ModalidadeContratacao',
            'ProjetoPrograma', 'CompromissoOrigem', 'GrupoPortfolio',
            'ProjetoGrupoPortfolio', 'PortfolioGrupoPortfolio', 'GrupoPortfolioPessoa',
            'PortfolioProjetoCompartilhado', 'ProjetoEquipe', 'ProjetoRegiao',
            'ViewProjetoMDO', 'ViewProjetoV2', 'ViewPainelEstrategicoProjetos',
            'Portfolio', 'PortfolioOrgao', 'RiscoTarefa', 'PlanoAcao', 'PlanoAcaoMonitoramento',
            'ProjetoAcompanhamentoRisco', 'ProjetoAcompanhamentoItem', 'AcompanhamentoTipo',
            'ProjetoNumeroSequencial', 'ProjetoRelatorioFila', 'ProjetoRegistroSei'
        ],
        'origin': 'Módulo de Gestão de Projetos (Frontend: /projetos, Backend: /gestao-projetos). Utilizado para cadastro e acompanhamento de obras e projetos estratégicos.'
    },
    'Transferências Voluntárias / Emendas': {
        'tables': [
            'Transferencia', 'TransferenciaTipo', 'TransferenciaAnexo',
            'TransferenciaHistorico', 'TransferenciaParlamentar', 'DistribuicaoRecurso',
            'DistribuicaoParlamentar', 'DistribuicaoRecursoAditamento',
            'DistribuicaoRecursoSei', 'Workflow', 'WorkflowEtapa', 'WorkflowFase',
            'WorkflowSituacao', 'WorkflowTarefa', 'Fluxo', 'FluxoFase', 'FluxoTarefa',
            'TransferenciaAndamento', 'TransferenciaAndamentoTarefa',
            'DistribuicaoStatusBase', 'DistribuicaoStatus',
            'WorkflowDistribuicaoStatus', 'DistribuicaoRecursoStatus', 'Classificacao',
            'ComunicadoTransfereGov', 'TransfereGovOportunidade',
            'TransferenciaStatusConsolidado', 'ViewTransferenciaAnalise',
            'ViewRankingTransferenciaParlamentar', 'ViewNotasTransferencias',
            'FluxoFaseSituacao'
        ],
        'origin': 'Módulo de Transferências Voluntárias (Frontend: /transferenciasVoluntarias, Backend: /transferencias-voluntarias). Integração com TransfereGov e gestão de recursos de emendas.'
    },
    'PDM (Plano de Metas) / Metas': {
        'tables': [
            'Pdm', 'Meta', 'MetaTag', 'MetaOrgao', 'MetaResponsavel', 'Iniciativa',
            'IniciativaTag', 'IniciativaOrgao', 'IniciativaResponsavel', 'Atividade',
            'AtividadeTag', 'AtividadeOrgao', 'AtividadeResponsavel', 'Indicador',
            'IndicadorVariavel', 'Variavel', 'VariavelResponsavel', 'FormulaComposta',
            'FormulaCompostaVariavel', 'UnidadeMedida', 'Tag', 'MacroTema', 'Tema',
            'SubTema', 'Ods', 'PdmDocumento', 'PdmPerfil', 'PdmCicloConfig',
            'CicloFisico', 'CicloFisicoFase', 'CicloFasesBase', 'CicloFasesPdmConfig',
            'MetaCicloFisicoAnalise', 'MetaCicloFisicoAnaliseDocumento',
            'MetaCicloFisicoRisco', 'MetaCicloFisicoFechamento',
            'VariavelCicloFisicoQualitativo', 'FormulaCompostaCicloFisicoQualitativo',
            'FormulaCompostaCicloFisicoDocumento', 'PedidoComplementacao',
            'VariavelCicloFisicoDocumento', 'StatusVariavelCicloFisico',
            'StatusMetaCicloFisico', 'MetaStatusConsolidadoCf',
            'MetaStatusAtrasoConsolidadoMes', 'MetaStatusAtrasoVariavel',
            'VariavelCicloCorrente', 'VariavelGlobalPedidoComplementacao',
            'VariavelGlobalCicloAnalise', 'VariavelGlobalCicloDocumento',
            'PsDashboardConsolidado', 'PsDashboardVariavel', 'CategoriaAssuntoVariavel',
            'AssuntoVariavel', 'VariavelAssuntoVariavel', 'VariavelGrupoResponsavelEquipe',
            'VariavelSuspensaoLog', 'VariavelSuspensaControle',
            'GrupoResponsavelEquipe', 'GrupoResponsavelEquipeResponsavel',
            'GrupoResponsavelEquipeParticipante', 'TipoPdm', 'TipoVariavel',
            'IndicadorFormulaVariavel', 'IndicadorFormulaComposta', 'IndicadorFormulaCompostaEmUso',
            'SerieIndicador', 'SerieVariavel', 'SerieVariavelHistorico',
            'VariavelNumeroSequencial', 'FonteVariavel', 'VariavelCategorica',
            'VariavelCategoricaValor', 'FormulaCompostaRelVariavel',
            'view_pdm_meta_iniciativa_atividade', 'view_meta_pessoa_responsavel',
            'view_atividade_pessoa_responsavel', 'view_iniciativa_pessoa_responsavel',
            'view_meta_pessoa_responsavel_na_cp', 'view_meta_responsavel_orcamento',
            'view_etapa_rel_meta', 'view_etapa_rel_meta_indicador',
            'ViewVariavelGlobal', 'view_ps_dashboard_consolidado',
            'view_ps_dashboard_meta_stats', 'view_dashboard_variavel_corrente'
        ],
        'origin': 'Módulo PDM - Plano de Metas (Frontend: /pdm, /metas, Backend: /pdm, /meta). Cadastro de metas, indicadores, variáveis e monitoramento de ciclos.'
    },
    'Orçamento': {
        'tables': [
            'OrcamentoPrevisto', 'OrcamentoPlanejado', 'OrcamentoRealizado',
            'DotacaoPlanejado', 'DotacaoRealizado', 'DotacaoProcesso',
            'DotacaoProcessoNota', 'OrcamentoPrevistoZerado', 'PdmOrcamentoConfig',
            'PdmOrcamentoRealizadoConfig', 'PdmDotacaoPlanejado',
            'PdmDotacaoRealizado', 'PdmDotacaoProcesso', 'PdmDotacaoProcessoNota',
            'PortfolioDotacaoPlanejado', 'PortfolioDotacaoRealizado',
            'PortfolioDotacaoProcesso', 'PortfolioDotacaoProcessoNota',
            'PdmOrcamentoRealizadoControleConcluido', 'OrcamentoRealizadoItem',
            'ImportacaoOrcamento', 'FonteRecurso', 'SofEntidade'
        ],
        'origin': 'Módulo Orçamentário (Frontend: /orcamento, Backend: /orcamento). Gestão de orçamento planejado vs realizado, integração com SOF.'
    },
    'Cronograma': {
        'tables': [
            'Cronograma', 'Etapa', 'CronogramaEtapa', 'Tarefa', 'TarefaCronograma',
            'TarefaDependente', 'CronogramaOrgao', 'EtapaResponsavel',
            'CronogramaTerminoPlanejadoConfig', 'view_meta_cronograma'
        ],
        'origin': 'Módulo Cronograma (Backend: /cronograma). Gestão de tempo, etapas e tarefas de projetos e metas.'
    },
    'Parlamentar / Política': {
        'tables': [
            'Parlamentar', 'ParlamentarMandato', 'ParlamentarEquipe', 'Partido',
            'Bancada', 'BancadaPartido', 'Eleicao', 'EleicaoComparecimento',
            'MandatoRepresentatividade', 'view_parlamentares_mandatos_part_atual'
        ],
        'origin': 'Módulo Parlamentar (Frontend: /parlamentares, Backend: /parlamentar). Gestão de deputados, vereadores, bancadas e eleições.'
    },
    'Administração / Core': {
        'tables': [
            'Pessoa', 'PessoaFisica', 'PessoaSessaoAtiva', 'PessoaPerfil', 'Orgao',
            'TipoOrgao', 'PerfilAcesso', 'PerfilPrivilegio', 'Privilegio',
            'PrivilegioModulo', 'LogGenerico', 'PessoaSessao', 'PessoaAtividadeLog',
            'SmaeConfig', 'WikiLink', 'PessoaAcessoPdm', 'PessoaAcessoPdmValido',
            'Arquivo', 'Diretorio', 'TipoDocumento', 'GrupoTematico', 'feature_flag',
            'Relatorio', 'RelatorioFila', 'TextoConfig'
        ],
        'origin': 'Módulo Administrativo / Core (Frontend: /users, /organs). Gestão de usuários, órgãos, perfis de acesso, relatórios gerais e configurações do sistema.'
    },
    'Geolocalização': {
        'tables': [
            'GeoLocalizacao', 'GeoCamadaConfig', 'GeoCamada', 'GeoCamadaRegiao',
            'GeoLocalizacaoCamada', 'GeoLocalizacaoReferencia', 'Regiao', 'ProjetoRegiao'
        ],
        'origin': 'Módulo Geolocalização (Backend: /geo-loc). Gestão de coordenadas, camadas geográficas e regiões.'
    },
    'Sistema SEI': {
        'tables': [
            'StatusSEI'
        ],
        'origin': 'Integração SEI (Backend: /sei-api). Controle de status de processos no Sistema Eletrônico de Informações.'
    },
    'Email': {
        'tables': [
            'EmaildbConfig', 'EmaildbQueue', 'AvisoEmail', 'AvisoEmailDisparos'
        ],
        'origin': 'Serviço de Email (Backend: /aviso-email). Configuração e fila de envio de emails.'
    },
    'Painéis': {
        'tables': [
            'Painel', 'PainelConteudo', 'PainelConteudoDetalhe', 'GrupoPainel',
            'PessoaGrupoPainel', 'PainelGrupoPainel', 'GrupoPainelExterno',
            'GrupoPainelExternoPessoa', 'PainelExternoGrupoPainelExterno',
            'PainelExterno', 'MetabasePermissao'
        ],
        'origin': 'Módulo de Painéis (Frontend: /paineis). Configuração de dashboards e painéis de visualização.'
    },
    'Notas / Comunicação': {
        'tables': [
            'Nota', 'NotaEnderecamento', 'NotaEnderecamentoResposta', 'NotaRevisao',
            'BlocoNota', 'TipoNota', 'TipoNotaModulo', 'ViewNotas'
        ],
        'origin': 'Módulo de Notas (Backend: /bloco-nota). Sistema de comunicação interna e notas.'
    },
    'Tarefas de Sistema (Background Tasks)': {
        'tables': [
            'task_queue', 'task_buffer', 'AtualizacaoEmLote', 'ApiRequestLogControl',
            'api_request_log', 'view_api_request_log'
        ],
        'origin': 'Sistema de Tarefas em Segundo Plano. Tabelas técnicas para controle de jobs assíncronos e logs.'
    }
}

# Inverter o mapeamento para busca rápida: Tabela -> (Modulo, Origem)
TABLE_TO_MODULE = {}
for module, data in MODULE_MAPPING.items():
    for table in data['tables']:
        TABLE_TO_MODULE[table] = (module, data['origin'])

def parse_prisma_schema(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex simples para encontrar models e views
    # model Nome { ... } ou view Nome { ... }
    block_regex = re.compile(r'(model|view)\s+(\w+)\s+\{([^}]*)\}', re.DOTALL)

    tables = []

    for match in block_regex.finditer(content):
        type_ = match.group(1) # model ou view
        name = match.group(2)
        body = match.group(3)

        columns = []

        # Parse lines inside the block
        lines = body.strip().split('\n')
        for line in lines:
            line = line.strip()
            # Ignorar linhas vazias, comentários ou anotações de bloco (@@)
            if not line or line.startswith('//') or line.startswith('@@'):
                continue

            # Formato típico: nome Tipo @modificadores
            # Ex: id Int @id @default(autoincrement())
            # Ex: email String @unique
            parts = line.split()
            if len(parts) >= 2:
                col_name = parts[0]
                col_type = parts[1]

                # Juntar o resto como descrição técnica (modificadores)
                modifiers = " ".join(parts[2:])

                # Ignorar campos que são relacionamentos (geralmente o tipo é outro Model)
                # No Prisma, se o tipo começa com Maiúscula e não é um tipo escalar padrão (Int, String, DateTime, Boolean, Float, Decimal, Json, Bytes, BigInt), é provável que seja um relacionamento.
                # Mas vamos manter tudo por enquanto e filtrar na exibição se necessário,
                # ou apenas marcar.
                # Uma heurística simples: Se o tipo está na lista de modelos, é relacionamento.

                columns.append({
                    'name': col_name,
                    'type': col_type,
                    'modifiers': modifiers
                })

        tables.append({
            'name': name,
            'type': type_,
            'columns': columns
        })

    return tables

def generate_markdown(tables, output_path):
    # Agrupar tabelas por módulo
    modules = {}

    # Adicionar módulos conhecidos para manter ordem
    for mod_name in MODULE_MAPPING.keys():
        modules[mod_name] = []

    modules['Não Categorizado'] = []

    # Set de nomes de modelos para identificar relacionamentos
    model_names = set(t['name'] for t in tables)
    standard_types = {'Int', 'String', 'DateTime', 'Boolean', 'Float', 'Decimal', 'Json', 'Bytes', 'BigInt', 'Unsupported'}

    for table in tables:
        mod_info = TABLE_TO_MODULE.get(table['name'])
        if mod_info:
            module_name = mod_info[0]
            modules[module_name].append(table)
        else:
            modules['Não Categorizado'].append(table)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Dicionário de Dados SMAE\n\n")
        f.write("Este documento lista as tabelas do banco de dados, suas colunas e a origem funcional (módulo) de onde os dados provêm.\n\n")

        for module_name, module_tables in modules.items():
            if not module_tables:
                continue

            origin_desc = ""
            if module_name in MODULE_MAPPING:
                origin_desc = MODULE_MAPPING[module_name]['origin']
            else:
                origin_desc = "Tabelas que não foram categorizadas em um módulo específico."

            f.write(f"## {module_name}\n\n")
            f.write(f"**Origem/Funcionalidade:** {origin_desc}\n\n")

            for table in sorted(module_tables, key=lambda x: x['name']):
                table_type = "Tabela" if table['type'] == 'model' else "View (Visualização)"
                f.write(f"### {table['name']} ({table_type})\n\n")

                f.write("| Coluna | Tipo | Detalhes |\n")
                f.write("|---|---|---|\n")

                for col in table['columns']:
                    type_desc = col['type']
                    # Adicionar link/nota se for chave estrangeira (relacionamento)
                    if col['type'] in model_names:
                        type_desc = f"Relacionamento -> {col['type']}"

                    # Limpar modificadores para ficar mais legível, mas manter @id, @unique
                    modifiers = col['modifiers']
                    clean_modifiers = []
                    if '@id' in modifiers: clean_modifiers.append('PK')
                    if '@unique' in modifiers: clean_modifiers.append('Unique')
                    if '[]' in col['type']: type_desc += " (Lista)"
                    if '?' in col['type']: type_desc += " (Opcional)"

                    # Tentar identificar FKs pelos modificadores
                    if '@relation' in modifiers:
                        # Extrair campos da relação se possível, mas simples "FK" já ajuda
                        clean_modifiers.append('FK')

                    desc = ", ".join(clean_modifiers)

                    f.write(f"| {col['name']} | {type_desc} | {desc} |\n")

                f.write("\n---\n\n")

if __name__ == "__main__":
    if not os.path.exists(SCHEMA_PATH):
        print(f"Erro: Arquivo {SCHEMA_PATH} não encontrado.")
    else:
        print("Lendo schema.prisma...")
        tables = parse_prisma_schema(SCHEMA_PATH)
        print(f"Encontradas {len(tables)} tabelas/views.")

        print("Gerando Markdown...")
        generate_markdown(tables, OUTPUT_PATH)
        print(f"Arquivo gerado com sucesso: {OUTPUT_PATH}")
