# Dicionário de Dados SMAE

Este documento lista as tabelas do banco de dados, suas colunas e a origem funcional (módulo) de onde os dados provêm.

## Gestão de Projetos

**Origem/Funcionalidade:** Módulo de Gestão de Projetos (Frontend: /projetos, Backend: /gestao-projetos). Utilizado para cadastro e acompanhamento de obras e projetos estratégicos.

### AcompanhamentoTipo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| tipo_projeto | TipoProjeto |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| acompanhamentos | ProjetoAcompanhamento[] (Lista) |  |

---

### CompromissoOrigem (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| relacionamento | CompromissoOrigemRelacionamento |  |
| projeto_id | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| rel_meta_id | Int? (Opcional) |  |
| rel_meta | Meta? (Opcional) | FK |
| rel_atividade_id | Int? (Opcional) |  |
| rel_atividade | Atividade? (Opcional) | FK |
| rel_iniciativa_id | Int? (Opcional) |  |
| rel_iniciativa | Iniciativa? (Opcional) | FK |
| origem_tipo | ProjetoOrigemTipo |  |
| origem_eh_pdm | Boolean |  |
| origem_outro | String? (Opcional) |  |
| meta_codigo | String? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| Iniciativa | Iniciativa? (Opcional) | FK |
| iniciativaId | Int? (Opcional) |  |

---

### Contrato (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| modalidade_contratacao_id | Int? (Opcional) |  |
| modalidade_contratacao | ModalidadeContratacao? (Opcional) | FK |
| orgao_id | Int? (Opcional) |  |
| orgao | Orgao? (Opcional) | FK |
| numero | String |  |
| contrato_exclusivo | Boolean |  |
| status | StatusContrato |  |
| objeto_resumo | String? (Opcional) |  |
| objeto_detalhado | String? (Opcional) |  |
| contratante | String? (Opcional) |  |
| empresa_contratada | String? (Opcional) |  |
| cnpj_contratada | String? (Opcional) |  |
| observacoes | String? (Opcional) |  |
| data_assinatura | DateTime? (Opcional) |  |
| data_inicio | DateTime? (Opcional) |  |
| data_termino | DateTime? (Opcional) |  |
| prazo_numero | Int? (Opcional) |  |
| prazo_unidade | ContratoPrazoUnidade? (Opcional) |  |
| data_base_mes | Int? (Opcional) |  |
| data_base_ano | Int? (Opcional) |  |
| valor | Decimal? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| aditivos | ContratoAditivo[] (Lista) |  |
| processosSei | ContratoSei[] (Lista) |  |
| fontesRecurso | ContratoFonteRecurso[] (Lista) |  |

---

### ContratoAditivo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| contrato_id | Int |  |
| contrato | Relacionamento -> Contrato | FK |
| tipo_aditivo_id | Int |  |
| tipo_aditivo | Relacionamento -> TipoAditivo | FK |
| numero | String |  |
| data | DateTime? (Opcional) |  |
| data_termino_atualizada | DateTime? (Opcional) |  |
| valor | Decimal? (Opcional) |  |
| percentual_medido | Decimal? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ContratoFonteRecurso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| contrato_id | Int |  |
| contrato | Relacionamento -> Contrato | FK |
| cod_sof | String |  |
| ano | Int |  |

---

### ContratoSei (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| contrato_id | Int |  |
| contrato | Relacionamento -> Contrato | FK |
| numero_sei | String |  |

---

### Empreendimento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| identificador | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| projetos | Projeto[] (Lista) |  |

---

### Equipamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |

---

### GrupoPortfolio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| tipo_projeto | TipoProjeto |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| ProjetoGrupoPortfolio | ProjetoGrupoPortfolio[] (Lista) |  |
| PortfolioGrupoPortfolio | PortfolioGrupoPortfolio[] (Lista) |  |
| GrupoPortfolioPessoa | GrupoPortfolioPessoa[] (Lista) |  |

---

### GrupoPortfolioPessoa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| grupo_portfolio_id | Int |  |
| orgao_id | Int |  |
| pessoa_id | Int |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| grupo_portfolio | Relacionamento -> GrupoPortfolio | FK |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao | Relacionamento -> Orgao | FK |

---

### ModalidadeContratacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |
| contratos | Contrato[] (Lista) |  |

---

### PlanoAcao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_risco_id | Int |  |
| projeto_risco | Relacionamento -> ProjetoRisco | FK |
| contramedida | String |  |
| prazo_contramedida | DateTime? (Opcional) |  |
| custo | Float? (Opcional) |  |
| custo_percentual | Float? (Opcional) |  |
| medidas_de_contingencia | String |  |
| orgao_id | Int? (Opcional) |  |
| orgao | Orgao? (Opcional) | FK |
| responsavel | String? (Opcional) |  |
| PlanoAcaoMonitoramento | PlanoAcaoMonitoramento[] (Lista) |  |
| contato_do_responsavel | String? (Opcional) |  |
| data_termino | DateTime? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| removedor | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |

---

### PlanoAcaoMonitoramento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| plano_acao_id | Int |  |
| plano_acao | Relacionamento -> PlanoAcao | FK |
| data_afericao | DateTime |  |
| descricao | String |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### Portfolio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| Projeto | Projeto[] (Lista) |  |
| orgaos | PortfolioOrgao[] (Lista) |  |
| tipo_projeto | TipoProjeto |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| nivel_maximo_tarefa | Int |  |
| nivel_regionalizacao | Int |  |
| orcamento_execucao_disponivel_meses | Int[] (Lista) |  |
| descricao | String |  |
| data_criacao | DateTime? (Opcional) |  |
| modelo_clonagem | Boolean |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| ProjetoNumerosSequenciais | ProjetoNumeroSequencial[] (Lista) |  |
| PortfolioDotacaoPlanejado | PortfolioDotacaoPlanejado[] (Lista) |  |
| PortfolioDotacaoRealizado | PortfolioDotacaoRealizado[] (Lista) |  |
| PortfolioDotacaoProcesso | PortfolioDotacaoProcesso[] (Lista) |  |
| PortfolioDotacaoProcessoNota | PortfolioDotacaoProcessoNota[] (Lista) |  |
| ImportacaoLog | ImportacaoOrcamento[] (Lista) |  |
| PortfolioGrupoPortfolio | PortfolioGrupoPortfolio[] (Lista) |  |
| projetosCompartilhados | PortfolioProjetoCompartilhado[] (Lista) |  |
| ViewProjetoMDO | ViewProjetoMDO[] (Lista) |  |
| ViewPainelEstrategicoProjetos | ViewPainelEstrategicoProjetos[] (Lista) |  |
| ViewProjetoV2 | ViewProjetoV2[] (Lista) |  |

---

### PortfolioGrupoPortfolio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| grupo_portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| GrupoPortfolio | Relacionamento -> GrupoPortfolio | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### PortfolioOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |

---

### PortfolioProjetoCompartilhado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |

---

### Projeto (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| tipo | TipoProjeto |  |
| portfolios_compartilhados | PortfolioProjetoCompartilhado[] (Lista) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| projeto_etapa_id | Int? (Opcional) |  |
| projeto_etapa | ProjetoEtapa? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| regiao_id | Int? (Opcional) |  |
| regiao | Regiao? (Opcional) | FK |
| logradouro_tipo | String? (Opcional) |  |
| logradouro_nome | String? (Opcional) |  |
| logradouro_numero | String? (Opcional) |  |
| logradouro_cep | String? (Opcional) |  |
| codigo | String? (Opcional) |  |
| previsao_custo | Float? (Opcional) |  |
| nome | String |  |
| objeto | String |  |
| objetivo | String |  |
| origem_tipo | ProjetoOrigemTipo |  |
| origem_eh_pdm | Boolean |  |
| origem_outro | String? (Opcional) |  |
| meta_codigo | String? (Opcional) |  |
| publico_alvo | String |  |
| previsao_inicio | DateTime? (Opcional) |  |
| previsao_termino | DateTime? (Opcional) |  |
| previsao_duracao | Int? (Opcional) |  |
| tipo_aditivo_id | Int? (Opcional) |  |
| modalidade_contratacao_id | Int? (Opcional) |  |
| projeto_programa_id | Int? (Opcional) |  |
| ano_orcamento | Int[] (Lista) |  |
| risco_maximo | String? (Opcional) |  |
| qtde_riscos | Int |  |
| mdo_detalhamento | String? (Opcional) |  |
| mdo_programa_habitacional | String? (Opcional) |  |
| mdo_observacoes | String? (Opcional) |  |
| mdo_n_unidades_habitacionais | Int? (Opcional) |  |
| mdo_n_unidades_atendidas | Int? (Opcional) |  |
| mdo_n_familias_beneficiadas | Int? (Opcional) |  |
| grupo_tematico_id | Int? (Opcional) |  |
| mdo_previsao_inauguracao | DateTime? (Opcional) |  |
| grupo_tematico | GrupoTematico? (Opcional) | FK |
| tipo_intervencao_id | Int? (Opcional) |  |
| tipo_intervencao | TipoIntervencao? (Opcional) | FK |
| equipamento_id | Int? (Opcional) |  |
| equipamento | Equipamento? (Opcional) | FK |
| empreendimento_id | Int? (Opcional) |  |
| empreendimento | Empreendimento? (Opcional) | FK |
| tipo_aditivo | TipoAditivo? (Opcional) | FK |
| modalidade_contratacao | ModalidadeContratacao? (Opcional) | FK |
| programa | ProjetoPrograma? (Opcional) | FK |
| secretario_colaborador | String? (Opcional) |  |
| orgao_colaborador_id | Int? (Opcional) |  |
| orgao_colaborador | Orgao? (Opcional) | FK |
| colaboradores_no_orgao | Int[] (Lista) |  |
| orgao_executor_id | Int? (Opcional) |  |
| orgao_executor | Orgao? (Opcional) | FK |
| orgao_origem_id | Int? (Opcional) |  |
| orgao_origem | Orgao? (Opcional) | FK |
| status | ProjetoStatus |  |
| fase | ProjetoFase |  |
| arquivado | Boolean |  |
| eh_prioritario | Boolean |  |
| resumo | String |  |
| escopo | String? (Opcional) |  |
| principais_etapas | String? (Opcional) |  |
| principais_etapas_antigo | String? (Opcional) |  |
| nao_escopo | String? (Opcional) |  |
| secretario_responsavel | String? (Opcional) |  |
| secretario_executivo | String? (Opcional) |  |
| coordenador_ue | String? (Opcional) |  |
| orgao_gestor_id | Int |  |
| orgao_gestor | Relacionamento -> Orgao | FK |
| responsaveis_no_orgao_gestor | Int[] (Lista) |  |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| responsavel_id | Int? (Opcional) |  |
| responsavel | Pessoa? (Opcional) | FK |
| data_aprovacao | DateTime? (Opcional) |  |
| data_revisao | DateTime? (Opcional) |  |
| versao | String? (Opcional) |  |
| registrado_em | DateTime |  |
| registrado_por | Int |  |
| pessoaQRegistrou | Pessoa? (Opcional) | FK |
| selecionado_em | DateTime? (Opcional) |  |
| selecionado_por | Int? (Opcional) |  |
| pessoaQSelecionou | Pessoa? (Opcional) | FK |
| em_planejamento_em | DateTime? (Opcional) |  |
| em_planejamento_por | Int? (Opcional) |  |
| pessoaQPlanejou | Pessoa? (Opcional) | FK |
| arquivado_em | DateTime? (Opcional) |  |
| arquivado_por | Int? (Opcional) |  |
| pessoaQArquivou | Pessoa? (Opcional) | FK |
| suspenso_em | DateTime? (Opcional) |  |
| suspenso_por | Int? (Opcional) |  |
| pessoaQSuspendeu | Pessoa? (Opcional) | FK |
| restaurado_em | DateTime? (Opcional) |  |
| restaurado_por | Int? (Opcional) |  |
| pessoaQRestaurou | Pessoa? (Opcional) | FK |
| validado_em | DateTime? (Opcional) |  |
| validado_por | Int? (Opcional) |  |
| pessoaQValidado | Pessoa? (Opcional) | FK |
| finalizou_planejamento_em | DateTime? (Opcional) |  |
| finalizou_planejamento_por | Int? (Opcional) |  |
| pessoaQFinalizouPlan | Pessoa? (Opcional) | FK |
| cancelado_em | DateTime? (Opcional) |  |
| cancelado_por | Int? (Opcional) |  |
| pessoaQCancelou | Pessoa? (Opcional) | FK |
| reiniciado_em | DateTime? (Opcional) |  |
| reiniciado_por | Int? (Opcional) |  |
| pessoaQReiniciou | Pessoa? (Opcional) | FK |
| iniciado_em | DateTime? (Opcional) |  |
| iniciado_por | Int? (Opcional) |  |
| pessoaQIniciou | Pessoa? (Opcional) | FK |
| terminado_em | DateTime? (Opcional) |  |
| terminado_por | Int? (Opcional) |  |
| pessoaQTerminou | Pessoa? (Opcional) | FK |
| premissas | ProjetoPremissa[] (Lista) |  |
| restricoes | ProjetoRestricao[] (Lista) |  |
| licoes_aprendidas | ProjetoLicaoAprendida[] (Lista) |  |
| fonte_recursos | ProjetoFonteRecurso[] (Lista) |  |
| documentos | ProjetoDocumento[] (Lista) |  |
| TarefaCronograma | TarefaCronograma[] (Lista) |  |
| ProjetoRisco | ProjetoRisco[] (Lista) |  |
| ProjetoAcompanhamento | ProjetoAcompanhamento[] (Lista) |  |
| orgaos_participantes | ProjetoOrgaoParticipante[] (Lista) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ProjetoRegistroSei | ProjetoRegistroSei[] (Lista) |  |
| ProjetoNumerosSequenciais | ProjetoNumeroSequencial[] (Lista) |  |
| MetaOrcamento | OrcamentoPrevisto[] (Lista) |  |
| OrcamentoPlanejado | OrcamentoPlanejado[] (Lista) |  |
| OrcamentoRealizado | OrcamentoRealizado[] (Lista) |  |
| OrcamentoPlanejadoZerado | OrcamentoPrevistoZerado[] (Lista) |  |
| Diretorio | Diretorio[] (Lista) |  |
| ProjetoGrupoPortfolio | ProjetoGrupoPortfolio[] (Lista) |  |
| equipe | ProjetoEquipe[] (Lista) |  |
| GeoEnderecoReferencia | GeoLocalizacaoReferencia[] (Lista) |  |
| contratos | Contrato[] (Lista) |  |
| ProjetoRegiao | ProjetoRegiao[] (Lista) |  |
| PessoasRevisao | ProjetoPessoaRevisao[] (Lista) |  |
| vetores_busca | Unsupported("tsvector")? (Opcional) |  |
| ViewProjetoMDO | ViewProjetoMDO[] (Lista) |  |
| tags | Int[] (Lista) |  |
| ProjetoOrigem | CompromissoOrigem[] (Lista) |  |
| origem_cache | Json |  |

---

### ProjetoAcompanhamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| acompanhanmento_tipo_id | Int? (Opcional) |  |
| acompanhamento_tipo | AcompanhamentoTipo? (Opcional) | FK |
| ordem | Int |  |
| data_registro | DateTime |  |
| participantes | String |  |
| detalhamento | String? (Opcional) |  |
| observacao | String? (Opcional) |  |
| detalhamento_status | String? (Opcional) |  |
| pontos_atencao | String? (Opcional) |  |
| pauta | String? (Opcional) |  |
| apresentar_no_relatorio | Boolean? (Opcional) |  |
| cronograma_paralisado | Boolean |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| atualizado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ProjetoAcompanhamentoRisco | ProjetoAcompanhamentoRisco[] (Lista) |  |
| ProjetoAcompanhamentoItem | ProjetoAcompanhamentoItem[] (Lista) |  |

---

### ProjetoAcompanhamentoItem (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_acompanhamento_id | Int |  |
| projeto_acompanhamento | Relacionamento -> ProjetoAcompanhamento | FK |
| numero_identificador | String |  |
| encaminhamento | String? (Opcional) |  |
| responsavel | String? (Opcional) |  |
| prazo_encaminhamento | DateTime? (Opcional) |  |
| prazo_realizado | DateTime? (Opcional) |  |
| ordem | Int |  |
| criado_em | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ProjetoAcompanhamentoRisco (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_risco_id | Int |  |
| projeto_risco | Relacionamento -> ProjetoRisco | FK |
| projeto_acompanhamento_id | Int |  |
| projeto_acompanhamento | Relacionamento -> ProjetoAcompanhamento | FK |

---

### ProjetoDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| arquivo_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| arquivo | Relacionamento -> Arquivo | FK |
| descricao | String? (Opcional) |  |
| data | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ProjetoEquipe (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| pessoa_id | Int |  |
| orgao_id | Int |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| orgao | Relacionamento -> Orgao | FK |
| projeto | Relacionamento -> Projeto | FK |
| pessoa | Relacionamento -> Pessoa | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ProjetoEtapa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo_projeto | TipoProjeto |  |
| descricao | String |  |
| ordem_painel | Int? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |
| ViewPainelEstrategicoProjetos | ViewPainelEstrategicoProjetos[] (Lista) |  |

---

### ProjetoFonteRecurso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| fonte_recurso_cod_sof | String |  |
| fonte_recurso_ano | Int |  |
| valor_percentual | Float? (Opcional) |  |
| valor_nominal | Float? (Opcional) |  |
| requer_revisao_sof | Boolean |  |
| criado_em | DateTime |  |
| atualizado_em | DateTime |  |

---

### ProjetoGrupoPortfolio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| grupo_portfolio_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| GrupoPortfolio | Relacionamento -> GrupoPortfolio | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ProjetoLicaoAprendida (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| data_registro | DateTime |  |
| responsavel | String |  |
| sequencial | Int |  |
| projeto_id | Int |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| projeto | Relacionamento -> Projeto | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |
| descricao | String |  |
| observacao | String? (Opcional) |  |
| contexto | String? (Opcional) |  |
| resultado | String? (Opcional) |  |

---

### ProjetoNumeroSequencial (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| ano | Int |  |
| valor | Int |  |

---

### ProjetoOrgaoParticipante (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |

---

### ProjetoPessoaRevisao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| criado_em | DateTime |  |

---

### ProjetoPremissa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| premissa | String |  |

---

### ProjetoPrograma (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |

---

### ProjetoRegistroSei (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| categoria | CategoriaProcessoSei |  |
| processo_sei | String |  |
| descricao | String? (Opcional) |  |
| link | String? (Opcional) |  |
| comentarios | String? (Opcional) |  |
| observacoes | String? (Opcional) |  |
| registro_sei_info | Json |  |

---

### ProjetoRelatorioFila (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| congelado_em | DateTime? (Opcional) |  |
| executado_em | DateTime? (Opcional) |  |
| relatorio_id | Int? (Opcional) |  |
| motivado_relatorio | ProjetoMotivoRelatorio |  |

---

### ProjetoRestricao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| restricao | String |  |

---

### ProjetoRisco (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| titulo | String |  |
| codigo | Int |  |
| registrado_em | DateTime |  |
| descricao | String? (Opcional) |  |
| causa | String? (Opcional) |  |
| consequencia | String? (Opcional) |  |
| probabilidade | Int? (Opcional) |  |
| impacto | Int? (Opcional) |  |
| status_risco | StatusRisco |  |
| nivel | Int? (Opcional) |  |
| grau | Int? (Opcional) |  |
| resposta | String? (Opcional) |  |
| RiscoTarefa | RiscoTarefa[] (Lista) |  |
| ProjetoAcompanhamentoRisco | ProjetoAcompanhamentoRisco[] (Lista) |  |
| planos_de_acao | PlanoAcao[] (Lista) |  |
| planos_de_acao_sem_dt_term | Int[] (Lista) |  |
| risco_tarefa_outros | String? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| removedor | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |

---

### ProjetoTag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo_projeto | TipoProjeto |  |
| descricao | String |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### RiscoTarefa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tarefa_id | Int |  |
| tarefa | Relacionamento -> Tarefa | FK |
| projeto_risco_id | Int |  |
| risco | Relacionamento -> ProjetoRisco | FK |

---

### TipoAditivo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| habilita_valor | Boolean |  |
| habilita_valor_data_termino | Boolean |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |
| aditivos | ContratoAditivo[] (Lista) |  |

---

### TipoIntervencao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| conceito | String? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |

---

### ViewPainelEstrategicoProjetos (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| projeto_id | Int | PK |
| projeto | Relacionamento -> Projeto | FK |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| meta_id | Int? (Opcional) |  |
| meta | Meta? (Opcional) | FK |
| portfolio_id | Int? (Opcional) |  |
| portfolio | Portfolio? (Opcional) | FK |
| projeto_etapa_id | Int? (Opcional) |  |
| projeto_etapa | ProjetoEtapa? (Opcional) | FK |
| status | ProjetoStatus |  |

---

### ViewProjetoMDO (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| codigo | String? (Opcional) |  |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| portfolio_titulo | String |  |
| registrado_em | DateTime |  |
| projeto | Relacionamento -> Projeto | FK |
| grupo_tematico_id | Int |  |
| grupo_tematico_nome | String |  |
| tipo_intervencao_id | Int? (Opcional) |  |
| tipo_intervencao_nome | String? (Opcional) |  |
| equipamento_id | Int? (Opcional) |  |
| equipamento_nome | String? (Opcional) |  |
| empreendimento_id | Int? (Opcional) |  |
| empreendimento_nome | String? (Opcional) |  |
| empreendimento_identificador | String? (Opcional) |  |
| orgao_origem_id | Int |  |
| orgao_origem | Relacionamento -> Orgao | FK |
| regioes | String |  |
| status | ProjetoStatus |  |

---

### ViewProjetoV2 (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| codigo | String? (Opcional) |  |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| portfolio_titulo | String |  |
| registrado_em | DateTime |  |
| projeto | Relacionamento -> Projeto | FK |
| grupo_tematico_id | Int? (Opcional) |  |
| grupo_tematico_nome | String? (Opcional) |  |
| tipo_intervencao_id | Int? (Opcional) |  |
| tipo_intervencao_nome | String? (Opcional) |  |
| equipamento_id | Int? (Opcional) |  |
| equipamento_nome | String? (Opcional) |  |
| empreendimento_id | Int? (Opcional) |  |
| empreendimento_nome | String? (Opcional) |  |
| empreendimento_identificador | String? (Opcional) |  |
| orgao_origem_id | Int? (Opcional) |  |
| orgao_origem | Orgao? (Opcional) | FK |
| regioes | String |  |
| previsao_custo | Float? (Opcional) |  |
| previsao_termino | DateTime? (Opcional) |  |
| projeto_etapa | String? (Opcional) |  |
| orgao_gestor_id | Int? (Opcional) |  |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| orgao_responsavel_sigla | String? (Opcional) |  |
| orgao_responsavel_descricao | String? (Opcional) |  |
| status | ProjetoStatus |  |

---

## Transferências Voluntárias / Emendas

**Origem/Funcionalidade:** Módulo de Transferências Voluntárias (Frontend: /transferenciasVoluntarias, Backend: /transferencias-voluntarias). Integração com TransfereGov e gestão de recursos de emendas.

### Classificacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| transferencia_tipo_id | Int |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| transferencia_tipo | Relacionamento -> TransferenciaTipo | FK |
| transferencias | Transferencia[] (Lista) | FK |

---

### ComunicadoTransfereGov (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| numero | Int |  |
| ano | Int |  |
| titulo | String |  |
| link | String |  |
| publicado_em | DateTime |  |
| descricao | String? (Opcional) |  |
| tipo | ComunicadoTipo |  |
| criado_em | DateTime |  |
| atualizado_em | DateTime |  |

---

### DistribuicaoParlamentar (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| distribuicao_recurso_id | Int |  |
| distribuicao_recurso | Relacionamento -> DistribuicaoRecurso | FK |
| partido_id | Int? (Opcional) |  |
| partido | Partido? (Opcional) | FK |
| parlamentar_id | Int |  |
| parlamentar | Relacionamento -> Parlamentar | FK |
| cargo | ParlamentarCargo? (Opcional) |  |
| objeto | String? (Opcional) |  |
| valor | Decimal? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### DistribuicaoRecurso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| transferencia | Relacionamento -> Transferencia | FK |
| orgao_gestor_id | Int |  |
| orgao_gestor | Relacionamento -> Orgao | FK |
| nome | String? (Opcional) |  |
| objeto | String |  |
| valor | Decimal |  |
| valor_total | Decimal |  |
| valor_contrapartida | Decimal |  |
| custeio | Decimal |  |
| pct_custeio | Decimal? (Opcional) |  |
| investimento | Decimal |  |
| valor_empenho | Decimal? (Opcional) |  |
| valor_liquidado | Decimal |  |
| pct_investimento | Decimal? (Opcional) |  |
| empenho | Boolean? (Opcional) |  |
| data_empenho | DateTime? (Opcional) |  |
| programa_orcamentario_estadual | String? (Opcional) |  |
| programa_orcamentario_municipal | String? (Opcional) |  |
| dotacao | String? (Opcional) |  |
| proposta | String? (Opcional) |  |
| contrato | String? (Opcional) |  |
| convenio | String? (Opcional) |  |
| assinatura_termo_aceite | DateTime? (Opcional) |  |
| assinatura_municipio | DateTime? (Opcional) |  |
| assinatura_estado | DateTime? (Opcional) |  |
| vigencia | DateTime? (Opcional) |  |
| conclusao_suspensiva | DateTime? (Opcional) |  |
| nota_id | Int? (Opcional) |  |
| nota | Nota? (Opcional) | FK |
| aviso_email_id | Int? (Opcional) |  |
| aviso_email | AvisoEmail? (Opcional) | FK |
| distribuicao_banco | String? (Opcional) |  |
| distribuicao_conta | String? (Opcional) |  |
| distribuicao_agencia | String? (Opcional) |  |
| rubrica_de_receita | String? (Opcional) |  |
| finalidade | String? (Opcional) |  |
| gestor_contrato | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| registros_sei | DistribuicaoRecursoSei[] (Lista) |  |
| aditamentos | DistribuicaoRecursoAditamento[] (Lista) |  |
| status | DistribuicaoRecursoStatus[] (Lista) |  |
| tarefas | Tarefa[] (Lista) |  |
| parlamentares | DistribuicaoParlamentar[] (Lista) |  |

---

### DistribuicaoRecursoAditamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| distribuicao_recurso_id | Int |  |
| distribuicao_recurso | Relacionamento -> DistribuicaoRecurso | FK |
| data_vigencia | DateTime |  |
| data_vigencia_corrente | DateTime |  |
| justificativa | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| criador | Relacionamento -> Pessoa | FK |

---

### DistribuicaoRecursoSei (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| distribuicao_recurso_id | Int |  |
| distribuicao_recurso | Relacionamento -> DistribuicaoRecurso | FK |
| status_sei_id | Int? (Opcional) |  |
| status_sei | StatusSEI? (Opcional) | FK |
| nome | String? (Opcional) |  |
| processo_sei | String |  |
| registro_sei_info | Json |  |

---

### DistribuicaoRecursoStatus (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| distribuicao_id | Int |  |
| distribuicao | Relacionamento -> DistribuicaoRecurso | FK |
| status_base_id | Int? (Opcional) |  |
| status_base | DistribuicaoStatusBase? (Opcional) | FK |
| status_id | Int? (Opcional) |  |
| status | DistribuicaoStatus? (Opcional) | FK |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| nome_responsavel | String |  |
| motivo | String |  |
| data_troca | DateTime |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### DistribuicaoStatus (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| tipo | DistribuicaoStatusTipo |  |
| valor_distribuicao_contabilizado | Boolean |  |
| permite_novos_registros | Boolean |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| configWorflow | WorkflowDistribuicaoStatus[] (Lista) |  |
| distribuicoes | DistribuicaoRecursoStatus[] (Lista) |  |
| TransferenciaTipo | TransferenciaTipo? (Opcional) | FK |
| transferenciaTipoId | Int? (Opcional) |  |

---

### DistribuicaoStatusBase (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| tipo | DistribuicaoStatusTipo |  |
| valor_distribuicao_contabilizado | Boolean |  |
| permite_novos_registros | Boolean |  |
| configWorflow | WorkflowDistribuicaoStatus[] (Lista) |  |
| distribuicoes | DistribuicaoRecursoStatus[] (Lista) |  |

---

### Fluxo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| workflow_id | Int |  |
| workflow | Relacionamento -> Workflow | FK |
| fluxo_etapa_de_id | Int |  |
| fluxo_etapa_de | Relacionamento -> WorkflowEtapa | FK |
| fluxo_etapa_para_id | Int |  |
| fluxo_etapa_para | Relacionamento -> WorkflowEtapa | FK |
| ordem | Int |  |
| fases | FluxoFase[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### FluxoFase (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| fluxo_id | Int |  |
| fluxo | Relacionamento -> Fluxo | FK |
| fase_id | Int |  |
| fase | Relacionamento -> WorkflowFase | FK |
| ordem | Int |  |
| responsabilidade | WorkflowResponsabilidade |  |
| tarefas | FluxoTarefa[] (Lista) |  |
| situacoes | FluxoFaseSituacao[] (Lista) |  |
| marco | Boolean |  |
| duracao | Int? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### FluxoFaseSituacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| fluxo_fase_id | Int |  |
| fluxo_fase | Relacionamento -> FluxoFase | FK |
| situacao_id | Int |  |
| situacao | Relacionamento -> WorkflowSituacao | FK |

---

### FluxoTarefa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| workflow_tarefa_id | Int |  |
| workflow_tarefa | Relacionamento -> WorkflowTarefa | FK |
| fluxo_fase_id | Int |  |
| fluxo_fase | Relacionamento -> FluxoFase | FK |
| responsabilidade | WorkflowResponsabilidade |  |
| ordem | Int |  |
| marco | Boolean |  |
| duracao | Int? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### TransfereGovOportunidade (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| hash | String |  |
| tipo | TransfereGovOportunidadeTipo |  |
| avaliacao | TransfereGovOportunidadeAvaliacao? (Opcional) |  |
| id_programa | BigInt |  |
| natureza_juridica_programa | String |  |
| transferencia_incorporada | Boolean |  |
| cod_orgao_sup_programa | BigInt? (Opcional) |  |
| desc_orgao_sup_programa | String? (Opcional) |  |
| cod_programa | BigInt |  |
| nome_programa | String |  |
| sit_programa | String |  |
| ano_disponibilizacao | Int? (Opcional) |  |
| data_disponibilizacao | DateTime? (Opcional) |  |
| dt_ini_receb | DateTime? (Opcional) |  |
| dt_fim_receb | DateTime? (Opcional) |  |
| finalidades | String? (Opcional) |  |
| modalidade_programa | String |  |
| acao_orcamentaria | String |  |
| vetores_busca | Unsupported("tsvector")? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_em | DateTime? (Opcional) |  |

---

### Transferencia (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo_id | Int |  |
| tipo | Relacionamento -> TransferenciaTipo | FK |
| orgao_concedente_id | Int |  |
| orgao_concedente | Relacionamento -> Orgao | FK |
| secretaria_concedente_id | Int? (Opcional) |  |
| secretaria_concedente | Orgao? (Opcional) | FK |
| secretaria_concedente_str | String? (Opcional) |  |
| workflow_id | Int? (Opcional) |  |
| workflow | Workflow? (Opcional) | FK |
| objeto | String |  |
| interface | TransferenciaInterface? (Opcional) |  |
| identificador | String |  |
| identificador_nro | Int |  |
| esfera | TransferenciaTipoEsfera |  |
| clausula_suspensiva | Boolean? (Opcional) |  |
| clausula_suspensiva_vencimento | DateTime? (Opcional) |  |
| empenho | Boolean? (Opcional) |  |
| pendente_preenchimento_valores | Boolean |  |
| valor | Decimal? (Opcional) |  |
| valor_total | Decimal? (Opcional) |  |
| valor_contrapartida | Decimal? (Opcional) |  |
| custeio | Decimal? (Opcional) |  |
| pct_custeio | Decimal? (Opcional) |  |
| investimento | Decimal? (Opcional) |  |
| pct_investimento | Decimal? (Opcional) |  |
| ano | Int? (Opcional) |  |
| emenda | String? (Opcional) |  |
| dotacao | String? (Opcional) |  |
| demanda | String? (Opcional) |  |
| programa | String? (Opcional) |  |
| banco_fim | String? (Opcional) |  |
| normativa | String? (Opcional) |  |
| conta_fim | String? (Opcional) |  |
| agencia_fim | String? (Opcional) |  |
| observacoes | String? (Opcional) |  |
| detalhamento | String? (Opcional) |  |
| banco_aceite | String? (Opcional) |  |
| conta_aceite | String? (Opcional) |  |
| nome_programa | String? (Opcional) |  |
| agencia_aceite | String? (Opcional) |  |
| emenda_unitaria | String? (Opcional) |  |
| gestor_contrato | String? (Opcional) |  |
| ordenador_despesa | String? (Opcional) |  |
| numero_identificacao | String? (Opcional) |  |
| vetores_busca | Unsupported("tsvector")? (Opcional) |  |
| nivel_maximo_tarefa | Int |  |
| workflow_finalizado | Boolean |  |
| workflow_etapa_atual_id | Int? (Opcional) |  |
| workflow_etapa_atual | WorkflowEtapa? (Opcional) | FK |
| workflow_fase_atual_id | Int? (Opcional) |  |
| workflow_fase_atual | WorkflowFase? (Opcional) | FK |
| prejudicada | Boolean |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| classificacao_id | Int? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| anexos | TransferenciaAnexo[] (Lista) |  |
| diretorios | Diretorio[] (Lista) |  |
| TarefaCronograma | TarefaCronograma[] (Lista) |  |
| distribuicao_recursos | DistribuicaoRecurso[] (Lista) |  |
| andamentoWorkflow | TransferenciaAndamento[] (Lista) |  |
| TransferenciaStatusConsolidado | TransferenciaStatusConsolidado[] (Lista) |  |
| ViewNotasTransferencias | ViewNotasTransferencias[] (Lista) |  |
| ViewDashboardAnalise | ViewTransferenciaAnalise[] (Lista) |  |
| parlamentar | TransferenciaParlamentar[] (Lista) |  |
| classificacao | Classificacao? (Opcional) | FK |
| historico | TransferenciaHistorico[] (Lista) |  |

---

### TransferenciaAndamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| transferencia | Relacionamento -> Transferencia | FK |
| workflow_etapa_id | Int |  |
| workflow_etapa | Relacionamento -> WorkflowEtapa | FK |
| workflow_fase_id | Int |  |
| workflow_fase | Relacionamento -> WorkflowFase | FK |
| workflow_situacao_id | Int? (Opcional) |  |
| workflow_situacao | WorkflowSituacao? (Opcional) | FK |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| pessoa_responsavel_id | Int? (Opcional) |  |
| pessoa_responsavel | Pessoa? (Opcional) | FK |
| data_inicio | DateTime? (Opcional) |  |
| data_termino | DateTime? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| tarefas | TransferenciaAndamentoTarefa[] (Lista) |  |
| tarefaEspelhada | Tarefa[] (Lista) |  |

---

### TransferenciaAndamentoTarefa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_andamento_id | Int |  |
| transferencia_andamento | Relacionamento -> TransferenciaAndamento | FK |
| workflow_tarefa_fluxo_id | Int |  |
| workflow_tarefa | Relacionamento -> WorkflowTarefa | FK |
| orgao_responsavel_id | Int? (Opcional) |  |
| orgao_responsavel | Orgao? (Opcional) | FK |
| feito | Boolean |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| tarefaEspelhada | Tarefa[] (Lista) |  |

---

### TransferenciaAnexo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| arquivo_id | Int |  |
| transferencia | Relacionamento -> Transferencia | FK |
| arquivo | Relacionamento -> Arquivo | FK |
| descricao | String? (Opcional) |  |
| data | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### TransferenciaHistorico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| transferencia | Relacionamento -> Transferencia | FK |
| tipo_antigo_id | Int? (Opcional) |  |
| tipo_antigo | TransferenciaTipo? (Opcional) | FK |
| tipo_novo_id | Int? (Opcional) |  |
| tipo_novo | TransferenciaTipo? (Opcional) | FK |
| acao | TransferenciaHistoricoAcao |  |
| dados_extra | Json |  |

---

### TransferenciaParlamentar (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| transferencia | Relacionamento -> Transferencia | FK |
| partido_id | Int? (Opcional) |  |
| partido | Partido? (Opcional) | FK |
| parlamentar_id | Int |  |
| parlamentar | Relacionamento -> Parlamentar | FK |
| cargo | ParlamentarCargo? (Opcional) |  |
| objeto | String? (Opcional) |  |
| valor | Decimal? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### TransferenciaStatusConsolidado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_id | Int |  |
| situacao | String |  |
| orgaos_envolvidos | Int[] (Lista) |  |
| data | DateTime? (Opcional) |  |
| data_origem | String |  |
| atualizado_em | DateTime |  |
| transferencia | Relacionamento -> Transferencia | FK |

---

### TransferenciaTipo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| categoria | TransferenciaTipoCategoria |  |
| esfera | TransferenciaTipoEsfera |  |
| transferencias | Transferencia[] (Lista) |  |
| workflows | Workflow[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| statuses_distribuicao | DistribuicaoStatus[] (Lista) |  |
| Classificacao | Classificacao[] (Lista) | FK |
| transferenciasAntigas | TransferenciaHistorico[] (Lista) | FK |
| transferenciasNovas | TransferenciaHistorico[] (Lista) | FK |

---

### ViewNotasTransferencias (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bloco_nota_id | Int |  |
| data_nota | DateTime |  |
| nota | String |  |
| status | StatusNota |  |
| removido_em | DateTime? (Opcional) |  |
| data_ordenacao | DateTime |  |
| transferencia_id | Int |  |
| transferencia_identificador | String |  |
| notaReferencia | Relacionamento -> Nota | FK |
| bloco_nota | Relacionamento -> BlocoNota | FK |
| transferencia | Relacionamento -> Transferencia | FK |

---

### ViewRankingTransferenciaParlamentar (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| parlamentar_id | Int | PK |
| parlamentar | Relacionamento -> Parlamentar | FK |
| nome_popular | String |  |
| parlamentar_foto_id | Int? (Opcional) |  |
| count | Int |  |
| valor | Decimal |  |

---

### ViewTransferenciaAnalise (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| transferencia_id | Int | PK |
| transferencia | Relacionamento -> Transferencia | FK |
| workflow_finalizado | Boolean |  |
| ano | Int |  |
| partido_id | Int[] (Lista) |  |
| workflow_etapa_atual_id | Int? (Opcional) |  |
| workflow_fase_atual_id | Int? (Opcional) |  |
| parlamentar_id | Int[] (Lista) |  |
| valor_total | Decimal |  |
| distribuicao_orgao_id | Int? (Opcional) |  |
| distribuicao_valor_total | Decimal? (Opcional) |  |
| prejudicada | Boolean |  |
| esfera | TransferenciaTipoEsfera |  |

---

### Workflow (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| transferencia_tipo_id | Int |  |
| transferencia_tipo | Relacionamento -> TransferenciaTipo | FK |
| nome | String |  |
| ativo | Boolean |  |
| inicio | DateTime |  |
| termino | DateTime? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| etapasFluxo | Fluxo[] (Lista) |  |
| transferencias | Transferencia[] (Lista) |  |
| statusesDistribuicao | WorkflowDistribuicaoStatus[] (Lista) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### WorkflowDistribuicaoStatus (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| workflow_id | Int |  |
| workflow | Relacionamento -> Workflow | FK |
| status_base_id | Int? (Opcional) |  |
| status_base | DistribuicaoStatusBase? (Opcional) | FK |
| status_id | Int? (Opcional) |  |
| status | DistribuicaoStatus? (Opcional) | FK |

---

### WorkflowEtapa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| etapa_fluxo | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| fluxoSaida | Fluxo[] (Lista) | FK |
| fluxoDestino | Fluxo[] (Lista) | FK |
| transferenciaAndamento | TransferenciaAndamento[] (Lista) |  |
| transferencias | Transferencia[] (Lista) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### WorkflowFase (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| fase | String |  |
| fluxos | FluxoFase[] (Lista) |  |
| transferenciaAndamento | TransferenciaAndamento[] (Lista) |  |
| transferencias | Transferencia[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### WorkflowSituacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| situacao | String |  |
| tipo_situacao | WorkflowSituacaoTipo |  |
| fasesWorkflow | FluxoFaseSituacao[] (Lista) |  |
| transferenciaAndamento | TransferenciaAndamento[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### WorkflowTarefa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tarefa_fluxo | String |  |
| fluxoTarefas | FluxoTarefa[] (Lista) |  |
| transferenciaAndamentoTarefa | TransferenciaAndamentoTarefa[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

## PDM (Plano de Metas) / Metas

**Origem/Funcionalidade:** Módulo PDM - Plano de Metas (Frontend: /pdm, /metas, Backend: /pdm, /meta). Cadastro de metas, indicadores, variáveis e monitoramento de ciclos.

### AssuntoVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| categoria_assunto_variavel_id | Int? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| VariavelAssuntoVariavel | VariavelAssuntoVariavel[] (Lista) |  |
| categoria_assunto_variavel | CategoriaAssuntoVariavel? (Opcional) | FK |

---

### Atividade (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| iniciativa_id | Int |  |
| iniciativa | Relacionamento -> Iniciativa | FK |
| codigo | String |  |
| titulo | String |  |
| contexto | String? (Opcional) |  |
| complemento | String? (Opcional) |  |
| compoe_indicador_iniciativa | Boolean |  |
| status | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| ativo | Boolean |  |
| origem_cache | Json |  |

---

### AtividadeOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| atividade_id | Int |  |
| atividade | Relacionamento -> Atividade | FK |
| responsavel | Boolean |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |

---

### AtividadeResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| atividade_id | Int |  |
| atividade | Relacionamento -> Atividade | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| coordenador_responsavel_cp | Boolean |  |

---

### AtividadeTag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| atividade_id | Int |  |
| atividade | Relacionamento -> Atividade | FK |
| tag_id | Int |  |
| tag | Relacionamento -> Tag | FK |

---

### CategoriaAssuntoVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| assunto_variavel | AssuntoVariavel[] (Lista) | FK |

---

### CicloFasesBase (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ciclo_fase | CicloFase | Unique |
| n_dias_do_inicio_mes | Int |  |
| duracao | Int |  |

---

### CicloFasesPdmConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ciclo_fase | CicloFase |  |
| n_dias_do_inicio_mes | Int |  |
| duracao | Int |  |

---

### CicloFisico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| data_ciclo | DateTime |  |
| ciclo_fase_atual_id | Int? (Opcional) |  |
| CicloFaseAtual | CicloFisicoFase? (Opcional) | FK |
| ativo | Boolean |  |
| tipo | TipoCicloFisico |  |
| acordar_ciclo_em | DateTime? (Opcional) |  |
| acordar_ciclo_errmsg | String? (Opcional) |  |
| acordar_ciclo_executou_em | DateTime? (Opcional) |  |
| fases | CicloFisicoFase[] (Lista) | FK |
| metas | Meta[] (Lista) |  |
| StatusMetaCicloFisico | StatusMetaCicloFisico[] (Lista) |  |
| StatusVariavelCicloFisico | StatusVariavelCicloFisico[] (Lista) |  |
| VariavelCicloFisicoQualitativo | VariavelCicloFisicoQualitativo[] (Lista) |  |
| VariavelCicloFisicoDocumento | VariavelCicloFisicoDocumento[] (Lista) |  |
| PedidoComplementacao | PedidoComplementacao[] (Lista) |  |
| MetaCicloFisicoAnalise | MetaCicloFisicoAnalise[] (Lista) |  |
| MetaCicloFisicoAnaliseDocumento | MetaCicloFisicoAnaliseDocumento[] (Lista) |  |
| MetaCicloFisicoRisco | MetaCicloFisicoRisco[] (Lista) |  |
| MetaCicloFisicoFechamento | MetaCicloFisicoFechamento[] (Lista) |  |
| FormulaCompostaCicloFisicoQualitativo | FormulaCompostaCicloFisicoQualitativo[] (Lista) |  |
| FormulaCompostaCicloFisicoDocumento | FormulaCompostaCicloFisicoDocumento[] (Lista) |  |
| VariaveisSuspensasCicloBase | VariavelSuspensaControle[] (Lista) | FK |
| VariaveisSuspensasCicloCorrente | VariavelSuspensaControle[] (Lista) | FK |
| MetaStatusConsolidadoCf | MetaStatusConsolidadoCf[] (Lista) |  |

---

### CicloFisicoFase (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ciclo_fisico_id | Int |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| cf_estou_em_usos | CicloFisico[] (Lista) | FK |
| data_inicio | DateTime |  |
| data_fim | DateTime |  |
| ciclo_fase | CicloFase |  |
| metas | Meta[] (Lista) |  |

---

### FonteVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| criado_em | DateTime |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| Variavel | Variavel[] (Lista) |  |

---

### FormulaComposta (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| formula | String |  |
| formula_compilada | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| mostrar_monitoramento | Boolean |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| autogerenciavel | Boolean |  |
| calc_casas_decimais | Int |  |
| calc_periodicidade | Periodicidade? (Opcional) |  |
| calc_regionalizavel | Boolean |  |
| calc_inicio_medicao | DateTime? (Opcional) |  |
| calc_fim_medicao | DateTime? (Opcional) |  |
| calc_orgao_id | Int? (Opcional) |  |
| calc_orgao | Orgao? (Opcional) | FK |
| calc_codigo | String? (Opcional) |  |
| calc_unidade_medida_id | Int? (Opcional) |  |
| calc_unidade_medida | UnidadeMedida? (Opcional) | FK |
| calc_regiao_id | Int? (Opcional) |  |
| calc_regiao | Regiao? (Opcional) | FK |
| atualizar_calc | Boolean |  |
| tipo_pdm | TipoPdm |  |
| criar_variavel | Boolean |  |
| variavel_calc_erro | String? (Opcional) |  |
| variavel_calc_id | Int? (Opcional) |  |
| variavel_calc | Variavel? (Opcional) | FK |
| variavel_mae_id | Int? (Opcional) |  |
| variavel_mae | Variavel? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| FormulaCompostaVariavel | FormulaCompostaVariavel[] (Lista) |  |
| IndicadorFormulaComposta | IndicadorFormulaComposta[] (Lista) |  |
| IndicadorFormulaCompostaEmUso | IndicadorFormulaCompostaEmUso[] (Lista) |  |
| FormulaCompostaCicloFisicoQualitativo | FormulaCompostaCicloFisicoQualitativo[] (Lista) |  |
| FormulaCompostaCicloFisicoDocumento | FormulaCompostaCicloFisicoDocumento[] (Lista) |  |
| FormulaCompostaRelVariavel | FormulaCompostaRelVariavel[] (Lista) |  |

---

### FormulaCompostaCicloFisicoDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| formula_composta_id | Int |  |
| referencia_data | DateTime |  |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| formula_composta | Relacionamento -> FormulaComposta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### FormulaCompostaCicloFisicoQualitativo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| formula_composta_id | Int |  |
| referencia_data | DateTime |  |
| analise_qualitativa | String? (Opcional) |  |
| enviado_para_cp | Boolean |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| formula_composta | Relacionamento -> FormulaComposta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### FormulaCompostaRelVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| formula_composta_id | Int |  |
| formula_composta | Relacionamento -> FormulaComposta | FK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |

---

### FormulaCompostaVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| referencia | String |  |
| formula_composta_id | Int |  |
| formula_composta | Relacionamento -> FormulaComposta | FK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| janela | Int |  |
| usar_serie_acumulada | Boolean |  |

---

### GrupoResponsavelEquipe (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| titulo | String |  |
| perfil | PerfilResponsavelEquipe |  |
| planosSetoriais | PdmPerfil[] (Lista) |  |
| criado_em | DateTime |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| GrupoResponsavelEquipePessoa | GrupoResponsavelEquipeParticipante[] (Lista) |  |
| VariavelGrupoResponsavelEquipe | VariavelGrupoResponsavelEquipe[] (Lista) |  |
| GrupoResponsavelEquipeColaborador | GrupoResponsavelEquipeResponsavel[] (Lista) |  |

---

### GrupoResponsavelEquipeParticipante (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| grupo_responsavel_equipe_id | Int |  |
| grupo_responsavel_equipe | Relacionamento -> GrupoResponsavelEquipe | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |

---

### GrupoResponsavelEquipeResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| grupo_responsavel_equipe_id | Int |  |
| grupo_responsavel_equipe | Relacionamento -> GrupoResponsavelEquipe | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |

---

### Indicador (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int? (Opcional) |  |
| meta | Meta? (Opcional) | FK |
| iniciativa_id | Int? (Opcional) |  |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade_id | Int? (Opcional) |  |
| atividade | Atividade? (Opcional) | FK |
| formula | String? (Opcional) |  |
| formula_compilada | String? (Opcional) |  |
| indicador_tipo | IndicadorTipo |  |
| acumulado_valor_base | Decimal? (Opcional) |  |
| acumulado_usa_formula | Boolean |  |
| codigo | String |  |
| titulo | String |  |
| periodicidade | Periodicidade |  |
| polaridade | Polaridade |  |
| regionalizavel | Boolean |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| inicio_medicao | DateTime |  |
| fim_medicao | DateTime |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| contexto | String? (Opcional) |  |
| complemento | String? (Opcional) |  |
| casas_decimais | Int? (Opcional) |  |
| variavel_categoria_id | Int? (Opcional) |  |
| ha_avisos_data_fim | Boolean |  |
| recalculando | Boolean |  |
| recalculo_erro | String? (Opcional) |  |
| recalculo_tempo | Decimal? (Opcional) |  |
| meta_valor_nominal | Decimal? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| IndicadorVariavelOrigem | IndicadorVariavel[] (Lista) | FK |
| IndicadorVariavel | IndicadorVariavel[] (Lista) | FK |
| SerieIndicador | SerieIndicador[] (Lista) |  |
| formula_variaveis | IndicadorFormulaVariavel[] (Lista) |  |
| painel_conteudo | PainelConteudo[] (Lista) |  |
| FormulaCompostaOrigem | IndicadorFormulaComposta[] (Lista) | FK |
| FormulaComposta | IndicadorFormulaComposta[] (Lista) | FK |
| IndicadorFormulaCompostaEmUso | IndicadorFormulaCompostaEmUso[] (Lista) |  |
| view_etapa_rel_meta_indicador | view_etapa_rel_meta_indicador[] (Lista) |  |

---

### IndicadorFormulaComposta (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| indicador_id | Int |  |
| indicador | Relacionamento -> Indicador | FK |
| formula_composta_id | Int |  |
| formula_composta | Relacionamento -> FormulaComposta | FK |
| indicador_origem_id | Int? (Opcional) |  |
| indicador_origem | Indicador? (Opcional) | FK |
| desativado | Boolean |  |
| desativado_em | DateTime? (Opcional) |  |
| desativado_por | Int? (Opcional) |  |
| desativador | Pessoa? (Opcional) | FK |

---

### IndicadorFormulaCompostaEmUso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| indicador_id | Int |  |
| indicador | Relacionamento -> Indicador | FK |
| formula_composta_id | Int |  |
| formula_composta | Relacionamento -> FormulaComposta | FK |

---

### IndicadorFormulaVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| referencia | String |  |
| indicador_id | Int |  |
| indicador | Relacionamento -> Indicador | FK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| janela | Int |  |
| usar_serie_acumulada | Boolean |  |

---

### IndicadorVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| indicador_id | Int |  |
| indicador | Relacionamento -> Indicador | FK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| indicador_origem_id | Int? (Opcional) |  |
| indicador_origem | Indicador? (Opcional) | FK |
| desativado | Boolean |  |
| desativado_em | DateTime? (Opcional) |  |
| desativado_por | Int? (Opcional) |  |
| desativador | Pessoa? (Opcional) | FK |
| aviso_data_fim | Boolean |  |

---

### Iniciativa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| codigo | String |  |
| titulo | String |  |
| contexto | String? (Opcional) |  |
| complemento | String? (Opcional) |  |
| compoe_indicador_meta | Boolean |  |
| status | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| ativo | Boolean |  |
| origem_cache | Json |  |

---

### IniciativaOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| iniciativa_id | Int |  |
| iniciativa | Relacionamento -> Iniciativa | FK |
| responsavel | Boolean |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |

---

### IniciativaResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| iniciativa_id | Int |  |
| iniciativa | Relacionamento -> Iniciativa | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| coordenador_responsavel_cp | Boolean |  |

---

### IniciativaTag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| iniciativa_id | Int |  |
| iniciativa | Relacionamento -> Iniciativa | FK |
| tag_id | Int |  |
| tag | Relacionamento -> Tag | FK |

---

### MacroTema (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Meta | Meta[] (Lista) |  |

---

### Meta (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| status | String |  |
| codigo | String |  |
| titulo | String |  |
| contexto | String? (Opcional) |  |
| complemento | String? (Opcional) |  |
| macro_tema_id | Int? (Opcional) |  |
| macro_tema | MacroTema? (Opcional) | FK |
| tema_id | Int? (Opcional) |  |
| tema | Tema? (Opcional) | FK |
| sub_tema_id | Int? (Opcional) |  |
| sub_tema | SubTema? (Opcional) | FK |
| ativo | Boolean |  |
| origem_cache | Json |  |

---

### MetaCicloFisicoAnalise (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| referencia_data | DateTime |  |
| informacoes_complementares | String? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### MetaCicloFisicoAnaliseDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| referencia_data | DateTime |  |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| descricao | String? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### MetaCicloFisicoFechamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| referencia_data | DateTime |  |
| comentario | String? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### MetaCicloFisicoRisco (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| referencia_data | DateTime |  |
| detalhamento | String? (Opcional) |  |
| ponto_de_atencao | String? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### MetaOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| responsavel | Boolean |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |

---

### MetaResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| coordenador_responsavel_cp | Boolean |  |

---

### MetaStatusAtrasoConsolidadoMes (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| meta_id | Int |  |
| mes | DateTime |  |
| meta | Relacionamento -> Meta | FK |
| variaveis_atrasadas | Int |  |
| orcamento_atrasados | Int |  |

---

### MetaStatusAtrasoVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| meses_atrasados | DateTime[] (Lista) |  |

---

### MetaStatusConsolidadoCf (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| meta_id | Int | PK |
| meta | Relacionamento -> Meta | FK |
| ciclo_fisico_id | Int |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| fase | CicloFase |  |
| variaveis_total | Int[] (Lista) |  |
| variaveis_preenchidas | Int[] (Lista) |  |
| variaveis_enviadas | Int[] (Lista) |  |
| variaveis_conferidas | Int[] (Lista) |  |
| variaveis_aguardando_complementacao | Int[] (Lista) |  |
| cronograma_total | Int[] (Lista) |  |
| cronograma_atraso_fim | Int[] (Lista) |  |
| cronograma_atraso_inicio | Int[] (Lista) |  |
| orcamento_total | Int[] (Lista) |  |
| orcamento_pendentes | Int[] (Lista) |  |
| orcamento_preenchido | Int[] (Lista) |  |
| analise_qualitativa_enviada | Boolean? (Opcional) |  |
| risco_enviado | Boolean? (Opcional) |  |
| fechamento_enviado | Boolean? (Opcional) |  |
| pendente_cp | Boolean |  |
| pendente_cp_variavel | Boolean |  |
| pendente_cp_cronograma | Boolean |  |
| orcamento_pendente | Boolean |  |
| atualizado_em | DateTime |  |

---

### MetaTag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| tag_id | Int |  |
| tag | Relacionamento -> Tag | FK |

---

### Ods (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| numero | Int |  |
| titulo | String |  |
| descricao | String |  |
| eh_status_pdm | Boolean |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Tag | Tag[] (Lista) |  |

---

### Pdm (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| descricao | String? (Opcional) |  |
| data_inicio | DateTime? (Opcional) |  |
| data_fim | DateTime? (Opcional) |  |
| data_publicacao | DateTime? (Opcional) |  |
| periodo_do_ciclo_participativo_inicio | DateTime? (Opcional) |  |
| periodo_do_ciclo_participativo_fim | DateTime? (Opcional) |  |
| ativo | Boolean |  |
| prefeito | String |  |
| equipe_tecnica | String? (Opcional) |  |
| possui_macro_tema | Boolean |  |
| possui_tema | Boolean |  |
| possui_sub_tema | Boolean |  |
| possui_contexto_meta | Boolean |  |
| possui_complementacao_meta | Boolean |  |
| possui_iniciativa | Boolean |  |
| possui_atividade | Boolean |  |
| rotulo_macro_tema | String |  |
| rotulo_tema | String |  |
| rotulo_sub_tema | String |  |
| rotulo_contexto_meta | String |  |
| rotulo_complementacao_meta | String |  |
| rotulo_iniciativa | String |  |
| rotulo_atividade | String |  |
| nivel_orcamento | NivelOrcamento |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| desativado_por | Int? (Opcional) |  |
| desativado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| considerar_atraso_apos | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| desativador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Eixo | MacroTema[] (Lista) |  |
| Tag | Tag[] (Lista) |  |
| ObjetivoEstrategico | Tema[] (Lista) |  |
| ArquivoDocumento | PdmDocumento[] (Lista) |  |
| SubTema | SubTema[] (Lista) |  |
| Meta | Meta[] (Lista) |  |
| tipo | TipoPdm |  |
| sistema | ModuloSistema |  |
| paineis_de_meta | Painel[] (Lista) |  |
| ps_admin_cps | Json |  |
| orcamento_dia_abertura | Int |  |
| orcamento_dia_fechamento | Int |  |
| monitoramento_orcamento | Boolean |  |
| legislacao_de_instituicao | String? (Opcional) |  |
| pdm_anteriores | Int[] (Lista) |  |
| orgao_admin_id | Int? (Opcional) |  |
| orgao_admin | Orgao? (Opcional) | FK |
| logo | String? (Opcional) |  |
| arquivo_logo_id | Int? (Opcional) |  |
| ArquivoLogo | Arquivo? (Opcional) | FK |
| CicloFasesPdmConfig | CicloFasesPdmConfig[] (Lista) |  |
| CicloFisico | CicloFisico[] (Lista) |  |
| PdmOrcamentoConfig | PdmOrcamentoConfig[] (Lista) |  |
| Relatorio | Relatorio[] (Lista) |  |
| PdmDotacaoPlanejado | PdmDotacaoPlanejado[] (Lista) |  |
| PdmDotacaoRealizado | PdmDotacaoRealizado[] (Lista) |  |
| PdmDotacaoProcesso | PdmDotacaoProcesso[] (Lista) |  |
| PdmDotacaoProcessoNota | PdmDotacaoProcessoNota[] (Lista) |  |
| ImportacaoLog | ImportacaoOrcamento[] (Lista) |  |
| PdmPerfil | PdmPerfil[] (Lista) |  |
| Diretorio | Diretorio[] (Lista) |  |
| view_pdm_meta_iniciativa_atividade | view_pdm_meta_iniciativa_atividade[] (Lista) |  |
| PdmCicloConfig | PdmCicloConfig[] (Lista) |  |

---

### PdmCicloConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meses | Int[] (Lista) |  |
| data_inicio | DateTime? (Opcional) |  |
| data_fim | DateTime? (Opcional) |  |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ultima_revisao | Boolean? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |

---

### PdmDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| pdm_id | Int? (Opcional) |  |
| pdm | Pdm? (Opcional) | FK |
| descricao | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### PdmPerfil (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| meta_id | Int? (Opcional) |  |
| meta | Meta? (Opcional) | FK |
| atividade_id | Int? (Opcional) |  |
| atividade | Atividade? (Opcional) | FK |
| iniciativa_id | Int? (Opcional) |  |
| iniciativa | Iniciativa? (Opcional) | FK |
| etapa_id | Int? (Opcional) |  |
| etapa | Etapa? (Opcional) | FK |
| tipo | PdmPerfilTipo |  |
| relacionamento | PdmPerfilRelacionamento |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| equipe_id | Int |  |
| equipe | Relacionamento -> GrupoResponsavelEquipe | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### PedidoComplementacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ciclo_fisico_id | Int |  |
| variavel_id | Int |  |
| pedido | String |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| atendido | Boolean |  |
| atendido_em | DateTime? (Opcional) |  |
| atendido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaAtendeu | Pessoa? (Opcional) | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### PsDashboardConsolidado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| item_id | Int |  |
| tipo | PsDashboardConsolidadoTipo |  |
| pdm_id | Int |  |
| meta_id | Int |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| variaveis | Int[] (Lista) |  |
| meta | Relacionamento -> Meta | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| orcamento_total | Int[] (Lista) |  |
| orcamento_preenchido | Int[] (Lista) |  |
| pendencia_orcamento | Boolean |  |
| cronograma_total | Int |  |
| cronograma_atraso_inicio | Int |  |
| cronograma_atraso_fim | Int |  |
| cronograma_preenchido | Int |  |
| pendencia_cronograma | Boolean |  |
| variaveis_total | Int |  |
| variaveis_total_no_ciclo | Int |  |
| variaveis_a_coletar | Int |  |
| variaveis_a_coletar_atrasadas | Int |  |
| variaveis_coletadas_nao_conferidas | Int |  |
| variaveis_conferidas_nao_liberadas | Int |  |
| variaveis_liberadas | Int |  |
| fase_atual | CicloFase? (Opcional) |  |
| fase_analise_preenchida | Boolean |  |
| fase_risco_preenchida | Boolean |  |
| fase_fechamento_preenchida | Boolean |  |
| equipes_orgaos | Int[] (Lista) |  |
| equipes | Int[] (Lista) |  |
| pendente | Boolean |  |
| pendente_variavel | Boolean |  |
| pendente_cronograma | Boolean |  |
| pendente_orcamento | Boolean |  |
| atualizado_em | DateTime |  |
| ciclo_fisico_id | Int? (Opcional) |  |

---

### PsDashboardVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| variavel_id | Int | PK |
| variavel | Relacionamento -> Variavel | FK |
| pdm_id | Int[] (Lista) |  |
| pdm_id_completo | Int[] (Lista) |  |
| fase | VariavelFase |  |
| fase_preenchimento_preenchida | Boolean |  |
| fase_validacao_preenchida | Boolean |  |
| fase_liberacao_preenchida | Boolean |  |
| possui_atrasos | Boolean |  |
| equipes | Int[] (Lista) |  |
| equipes_orgaos | Int[] (Lista) |  |
| equipes_preenchimento | Int[] (Lista) |  |
| equipes_conferencia | Int[] (Lista) |  |
| equipes_liberacao | Int[] (Lista) |  |

---

### SerieIndicador (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| indicador_id | Int |  |
| indicador | Relacionamento -> Indicador | FK |
| serie | Serie |  |
| data_valor | DateTime |  |
| valor_nominal | Float |  |
| ha_conferencia_pendente | Boolean |  |

---

### SerieVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| serie | Serie |  |
| data_valor | DateTime |  |
| valor_nominal | Decimal |  |
| variavel_categorica_id | Int? (Opcional) |  |
| variavel_categorica | VariavelCategorica? (Opcional) | FK |
| variavel_categorica_valor_id | Int? (Opcional) |  |
| variavel_categorica_valor | VariavelCategoricaValor? (Opcional) | FK |
| atualizado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| conferida | Boolean |  |
| conferida_por | Int? (Opcional) |  |
| conferida_em | DateTime? (Opcional) |  |
| conferidor | Pessoa? (Opcional) | FK |
| ciclo_fisico_id | Int? (Opcional) |  |
| elementos | Json? (Opcional) |  |

---

### SerieVariavelHistorico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| serie_variavel_id | Int |  |
| variavel_id | Int |  |
| serie | Serie |  |
| data_valor | DateTime |  |
| valor_nominal | Decimal |  |
| variavel_categorica_id | Int? (Opcional) |  |
| variavel_categorica_valor_id | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| conferida | Boolean |  |
| conferida_por | Int? (Opcional) |  |
| conferida_em | DateTime? (Opcional) |  |
| ciclo_fisico_id | Int? (Opcional) |  |

---

### StatusMetaCicloFisico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| pessoa_id | Int |  |
| status_coleta | String |  |
| status_cronograma | String |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |

---

### StatusVariavelCicloFisico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| variavel_id | Int |  |
| aguarda_cp | Boolean |  |
| aguarda_complementacao | Boolean |  |
| conferida | Boolean |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| variavel | Relacionamento -> Variavel | FK |

---

### SubTema (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Meta | Meta[] (Lista) |  |

---

### Tag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| icone | String? (Opcional) |  |
| arquivo_icone_id | Int? (Opcional) |  |
| ArquivoIcone | Arquivo? (Opcional) | FK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ods_id | Int? (Opcional) |  |
| ods | Ods? (Opcional) | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| meta_tag | MetaTag[] (Lista) |  |
| iniciativa_tag | IniciativaTag[] (Lista) |  |
| atividade_tag | AtividadeTag[] (Lista) |  |

---

### Tema (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Meta | Meta[] (Lista) |  |

---

### UnidadeMedida (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| sigla | String |  |
| descricao | String |  |
| Variavel | Variavel[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| FormulaComposta | FormulaComposta[] (Lista) |  |

---

### Variavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| regiao_id | Int? (Opcional) |  |
| regiao | Regiao? (Opcional) | FK |
| titulo | String |  |
| ano_base | Int? (Opcional) |  |
| valor_base | Decimal |  |
| periodicidade | Periodicidade |  |
| unidade_medida_id | Int |  |
| unidade_medida | Relacionamento -> UnidadeMedida | FK |
| variavel_categorica_id | Int? (Opcional) |  |
| variavel_categorica | VariavelCategorica? (Opcional) | FK |
| medicao_orgao_id | Int? (Opcional) |  |
| medicao_orgao | Orgao? (Opcional) | FK |
| validacao_orgao_id | Int? (Opcional) |  |
| validacao_orgao | Orgao? (Opcional) | FK |
| liberacao_orgao_id | Int? (Opcional) |  |
| liberacao_orgao | Orgao? (Opcional) | FK |
| tipo | TipoVariavel |  |
| polaridade | Polaridade |  |
| codigo | String |  |
| supraregional | Boolean |  |
| mostrar_monitoramento | Boolean |  |
| suspendida_em | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| criador | Pessoa? (Opcional) | FK |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| atualizador | Pessoa? (Opcional) | FK |
| vetores_busca | Unsupported("tsvector")? (Opcional) |  |
| inicio_medicao | DateTime? (Opcional) |  |
| fim_medicao | DateTime? (Opcional) |  |
| casas_decimais | Int |  |
| acumulativa | Boolean |  |
| orgao_proprietario_id | Int? (Opcional) |  |
| orgao_proprietario | Orgao? (Opcional) | FK |
| metodologia | String? (Opcional) |  |
| descricao | String? (Opcional) |  |
| fonte_id | Int? (Opcional) |  |
| fonte | FonteVariavel? (Opcional) | FK |
| periodo_preenchimento | Int[] (Lista) |  |
| periodo_validacao | Int[] (Lista) |  |
| periodo_liberacao | Int[] (Lista) |  |
| dado_aberto | Boolean |  |
| equipes_configuradas | Boolean |  |
| possui_variaveis_filhas | Boolean |  |
| recalculando | Boolean |  |
| recalculo_erro | String? (Opcional) |  |
| recalculo_tempo | Decimal? (Opcional) |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| variavel_mae_id | Int? (Opcional) |  |
| variavel_mae | Variavel? (Opcional) | FK |
| variaveis_filhas | Variavel[] (Lista) | FK |
| serie_variavel | SerieVariavel[] (Lista) |  |
| variavel_responsavel | VariavelResponsavel[] (Lista) |  |
| indicador_variavel | IndicadorVariavel[] (Lista) |  |
| indicador_formula_variavel | IndicadorFormulaVariavel[] (Lista) |  |
| PainelConteudoDetalhe | PainelConteudoDetalhe[] (Lista) |  |
| StatusVariavelCicloFisico | StatusVariavelCicloFisico[] (Lista) |  |
| atraso_meses | Int |  |
| VariavelCicloFisicoQualitativo | VariavelCicloFisicoQualitativo[] (Lista) |  |
| VariavelCicloFisicoDocumento | VariavelCicloFisicoDocumento[] (Lista) |  |
| PedidoComplementacao | PedidoComplementacao[] (Lista) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| FormulaCompostaVariavel | FormulaCompostaVariavel[] (Lista) |  |
| suspensao_log | VariavelSuspensaoLog[] (Lista) |  |
| suspensao_controle | VariavelSuspensaControle[] (Lista) |  |
| MetaStatusAtrasoVariavel | MetaStatusAtrasoVariavel[] (Lista) |  |
| Etapa | Etapa[] (Lista) |  |
| VariavelAssuntoVariavel | VariavelAssuntoVariavel[] (Lista) |  |
| VariavelGrupoResponsavelEquipe | VariavelGrupoResponsavelEquipe[] (Lista) |  |
| ViewVariavelGlobal | ViewVariavelGlobal[] (Lista) |  |
| FormulaCompostaCalc | FormulaComposta[] (Lista) | FK |
| FormulaCompostaMae | FormulaComposta[] (Lista) | FK |
| FormulaCompostaRelVariavel | FormulaCompostaRelVariavel[] (Lista) |  |
| ViewVariavelGlobalFilhas | ViewVariavelGlobal[] (Lista) | FK |
| VariavelCicloCorrente | VariavelCicloCorrente? (Opcional) |  |
| VariavelGlobalCicloAnalise | VariavelGlobalCicloAnalise[] (Lista) |  |
| VariavelGlobalCicloDocumento | VariavelGlobalCicloDocumento[] (Lista) |  |
| VariavelGlobalPedidoComplementacao | VariavelGlobalPedidoComplementacao[] (Lista) |  |
| PsDashboardVariavel | PsDashboardVariavel[] (Lista) |  |

---

### VariavelAssuntoVariavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| assunto_variavel_id | Int |  |
| assunto_variavel | Relacionamento -> AssuntoVariavel | FK |

---

### VariavelCategorica (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | TipoVariavelCategorica |  |
| titulo | String |  |
| descricao | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| valores | VariavelCategoricaValor[] (Lista) |  |
| Variavel | Variavel[] (Lista) |  |
| SerieVariavel | SerieVariavel[] (Lista) |  |

---

### VariavelCategoricaValor (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| valor_variavel | Int |  |
| descricao | String? (Opcional) |  |
| ordem | Int |  |
| variavel_categorica_id | Int |  |
| variavel_categorica | Relacionamento -> VariavelCategorica | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| SerieVariavel | SerieVariavel[] (Lista) |  |

---

### VariavelCicloCorrente (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| fase | VariavelFase |  |
| proximo_periodo_abertura | DateTime |  |
| ultimo_periodo_valido | DateTime |  |
| pedido_complementacao | Boolean |  |
| eh_corrente | Boolean |  |
| atrasos | DateTime[] (Lista) |  |
| prazo | DateTime? (Opcional) |  |
| liberacao_enviada | Boolean |  |
| atualizado_em | DateTime |  |
| variavel | Relacionamento -> Variavel | FK |
| ViewVariavelGlobal | ViewVariavelGlobal[] (Lista) |  |
| view_dashboard_variavel_corrente | view_dashboard_variavel_corrente[] (Lista) |  |

---

### VariavelCicloFisicoDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| variavel_id | Int |  |
| referencia_data | DateTime |  |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### VariavelCicloFisicoQualitativo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| ciclo_fisico_id | Int |  |
| variavel_id | Int |  |
| referencia_data | DateTime |  |
| analise_qualitativa | String? (Opcional) |  |
| enviado_para_cp | Boolean |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| ciclo_fisico | Relacionamento -> CicloFisico | FK |
| meta | Relacionamento -> Meta | FK |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### VariavelGlobalCicloAnalise (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| fase | VariavelFase |  |
| referencia_data | DateTime |  |
| informacoes_complementares | String? (Opcional) |  |
| eh_liberacao_auto | Boolean |  |
| aprovada | Boolean |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| valores | Json |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| sincronizar_serie_variavel | Boolean |  |
| sv_sincronizado_em | DateTime? (Opcional) |  |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### VariavelGlobalCicloDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| fase | VariavelFase |  |
| referencia_data | DateTime |  |
| descricao | String? (Opcional) |  |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### VariavelGlobalPedidoComplementacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| referencia_data | DateTime |  |
| variavel_id | Int |  |
| pedido | String |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| ultima_revisao | Boolean |  |
| atendido | Boolean |  |
| atendido_em | DateTime? (Opcional) |  |
| atendido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| variavel | Relacionamento -> Variavel | FK |
| pessoaCriador | Relacionamento -> Pessoa | FK |
| pessoaAtendeu | Pessoa? (Opcional) | FK |
| pessoaRemovedor | Pessoa? (Opcional) | FK |

---

### VariavelGrupoResponsavelEquipe (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| grupo_responsavel_equipe_id | Int |  |
| grupo_responsavel_equipe | Relacionamento -> GrupoResponsavelEquipe | FK |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |

---

### VariavelNumeroSequencial (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ano_referencia | Int | Unique |
| sequencial | Int |  |

---

### VariavelResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| variavel | Relacionamento -> Variavel | FK |

---

### VariavelSuspensaControle (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| ciclo_fisico_base_id | Int |  |
| ciclo_fisico_corrente_id | Int |  |
| ciclo_fisico_base | Relacionamento -> CicloFisico | FK |
| ciclo_fisico_corrente | Relacionamento -> CicloFisico | FK |
| serie | Serie |  |
| valor_antigo | Decimal? (Opcional) |  |
| valor_novo | Decimal? (Opcional) |  |
| processado_em | DateTime |  |

---

### VariavelSuspensaoLog (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int |  |
| variavel | Relacionamento -> Variavel | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| suspendida | Boolean |  |
| criado_em | DateTime |  |
| previo_status_mostrar_monitoramento | Boolean |  |

---

### ViewVariavelGlobal (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel | Relacionamento -> Variavel | FK |
| titulo | String |  |
| codigo | String |  |
| orgao_id | Int? (Opcional) |  |
| orgao | Orgao? (Opcional) | FK |
| orgao_proprietario_id | Int? (Opcional) |  |
| orgao_proprietario | Orgao? (Opcional) | FK |
| regiao_id | Int? (Opcional) |  |
| regiao | Regiao? (Opcional) | FK |
| planos | Int[] (Lista) |  |
| periodicidade | Periodicidade |  |
| inicio_medicao | DateTime? (Opcional) |  |
| fim_medicao | DateTime? (Opcional) |  |
| criado_em | DateTime |  |
| assunto_ids | Int[] (Lista) |  |
| tipo | TipoVariavel |  |
| fonte_id | Int? (Opcional) |  |
| fonte_nome | String? (Opcional) |  |
| variavel_mae_id | Int? (Opcional) |  |
| variavel_mae | Variavel? (Opcional) | FK |
| possui_variaveis_filhas | Boolean |  |
| VariavelCicloCorrente | VariavelCicloCorrente? (Opcional) | FK |

---

### view_atividade_pessoa_responsavel (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| atividade_id | Int |  |
| iniciativa_id | Int |  |
| meta_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao_id | Int |  |

---

### view_dashboard_variavel_corrente (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| item_id | Int |  |
| tipo | String |  |
| variavel_ciclo_corrente_id | Int |  |
| variavel_ciclo_corrente | Relacionamento -> VariavelCicloCorrente | FK |
| pdm_id | Int |  |

---

### view_etapa_rel_meta (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| etapa_id | Int | PK |
| meta_id | Int |  |
| atividade_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |

---

### view_etapa_rel_meta_indicador (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| etapa_id | Int | PK |
| tipo | String |  |
| meta_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| indicador_id | Int? (Opcional) |  |
| indicador | Indicador? (Opcional) | FK |

---

### view_iniciativa_pessoa_responsavel (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| iniciativa_id | Int |  |
| meta_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao_id | Int |  |

---

### view_meta_pessoa_responsavel (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| meta | Relacionamento -> Meta | FK |
| orgao_id | Int |  |

---

### view_meta_pessoa_responsavel_na_cp (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| meta | Relacionamento -> Meta | FK |
| orgao_id | Int |  |

---

### view_meta_responsavel_orcamento (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| meta_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |

---

### view_pdm_meta_iniciativa_atividade (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| meta_id | Int | PK |
| pdm_id | Int |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| meta | Relacionamento -> Meta | FK |
| pdm | Relacionamento -> Pdm | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |

---

### view_ps_dashboard_consolidado (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| item_id | Int |  |
| tipo | PsDashboardConsolidadoTipo |  |
| pdm_id | Int |  |
| meta_id | Int |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| variaveis | Int[] (Lista) |  |
| orcamento_total | Int[] (Lista) |  |
| orcamento_preenchido | Int[] (Lista) |  |
| pendencia_orcamento | Boolean |  |
| cronograma_total | Int |  |
| cronograma_atraso_inicio | Int |  |
| cronograma_atraso_fim | Int |  |
| cronograma_preenchido | Int |  |
| pendencia_cronograma | Boolean |  |
| variaveis_total | Int |  |
| variaveis_total_no_ciclo | Int |  |
| variaveis_a_coletar | Int |  |
| variaveis_a_coletar_atrasadas | Int |  |
| variaveis_coletadas_nao_conferidas | Int |  |
| variaveis_conferidas_nao_liberadas | Int |  |
| variaveis_liberadas | Int |  |
| fase_atual | CicloFase? (Opcional) |  |
| fase_analise_preenchida | Boolean |  |
| fase_risco_preenchida | Boolean |  |
| fase_fechamento_preenchida | Boolean |  |
| equipes_orgaos | Int[] (Lista) |  |
| equipes | Int[] (Lista) |  |
| pendente | Boolean |  |
| pendente_variavel | Boolean |  |
| pendente_cronograma | Boolean |  |
| pendente_orcamento | Boolean |  |
| atualizado_em | DateTime |  |
| ciclo_fisico_id | Int? (Opcional) |  |
| meta | Relacionamento -> Meta | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| meta_codigo | String |  |
| meta_titulo | String |  |
| iniciativa_codigo | String? (Opcional) |  |
| iniciativa_titulo | String? (Opcional) |  |
| atividade_codigo | String? (Opcional) |  |
| atividade_titulo | String? (Opcional) |  |
| order_meta | String |  |
| order_iniciativa | String |  |
| order_atividade | String |  |

---

### view_ps_dashboard_meta_stats (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| pdm_id | Int |  |
| meta_id | Int |  |
| equipes | Int[] (Lista) |  |
| equipes_orgaos | Int[] (Lista) |  |
| pendente | Int |  |
| var_liberadas | Int |  |
| var_a_liberar | Int |  |
| crono_preenchido | Int |  |
| crono_a_preencher | Int |  |
| orc_preenchido | Int |  |
| orc_a_preencher | Int |  |
| qualif_preenchida | Int |  |
| qualif_a_preencher | Int |  |
| risco_preenchido | Int |  |
| risco_a_preencher | Int |  |
| fechadas | Int |  |
| a_fechar | Int |  |
| ciclo_fisico_id | Int? (Opcional) |  |
| meta | Relacionamento -> Meta | FK |

---

## Orçamento

**Origem/Funcionalidade:** Módulo Orçamentário (Frontend: /orcamento, Backend: /orcamento). Gestão de orçamento planejado vs realizado, integração com SOF.

### DotacaoPlanejado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| informacao_valida | Boolean |  |
| sincronizado_em | DateTime? (Opcional) |  |
| ano_referencia | Int |  |
| mes_utilizado | Int |  |
| dotacao | String |  |
| val_orcado_inicial | Decimal |  |
| val_orcado_atualizado | Decimal |  |
| saldo_disponivel | Decimal |  |

---

### DotacaoProcesso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| informacao_valida | Boolean |  |
| sincronizado_em | DateTime? (Opcional) |  |
| ano_referencia | Int |  |
| mes_utilizado | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| empenho_liquido | Decimal |  |
| valor_liquidado | Decimal |  |

---

### DotacaoProcessoNota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| informacao_valida | Boolean |  |
| sincronizado_em | DateTime? (Opcional) |  |
| ano_referencia | Int |  |
| mes_utilizado | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| dotacao_processo_nota | String |  |
| empenho_liquido | Decimal |  |
| valor_liquidado | Decimal |  |

---

### DotacaoRealizado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| informacao_valida | Boolean |  |
| sincronizado_em | DateTime? (Opcional) |  |
| ano_referencia | Int |  |
| mes_utilizado | Int |  |
| dotacao | String |  |
| empenho_liquido | Decimal |  |
| valor_liquidado | Decimal |  |

---

### FonteRecurso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| fonte | String |  |
| sigla | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ImportacaoOrcamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| arquivo_id | Int |  |
| arquivo | Relacionamento -> Arquivo | FK |
| saida_arquivo_id | Int? (Opcional) |  |
| saida_arquivo | Arquivo? (Opcional) | FK |
| modulo_sistema | ModuloSistema |  |
| pdm_id | Int? (Opcional) |  |
| pdm | Pdm? (Opcional) | FK |
| portfolio_id | Int? (Opcional) |  |
| portfolio | Portfolio? (Opcional) | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| congelado_em | DateTime? (Opcional) |  |
| processado_em | DateTime? (Opcional) |  |
| processado_errmsg | String? (Opcional) |  |
| linhas_importadas | Int? (Opcional) |  |
| linhas_recusadas | Int? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |

---

### OrcamentoPlanejado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| valor_planejado | Decimal |  |
| ano_referencia | Int |  |
| dotacao | String |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### OrcamentoPrevisto (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| versao_anterior_id | Int? (Opcional) | Unique |
| ultima_revisao | Boolean |  |
| ano_referencia | Int |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| atualizado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| custo_previsto | Float |  |
| parte_dotacao | String |  |
| projeto | Projeto? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| versao_anterior | OrcamentoPrevisto? (Opcional) | FK |
| versao_seguinte | OrcamentoPrevisto? (Opcional) | FK |

---

### OrcamentoPrevistoZerado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| ano_referencia | Int |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### OrcamentoRealizado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| ano_referencia | Int |  |
| mes_utilizado | Int |  |
| dotacao | String |  |
| processo | String? (Opcional) |  |
| nota_empenho | String? (Opcional) |  |
| dotacao_complemento | String? (Opcional) |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |
| itens | OrcamentoRealizadoItem[] (Lista) |  |
| criado_em | DateTime |  |
| criado_por | Int |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### OrcamentoRealizadoItem (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| valor_empenho | Decimal |  |
| valor_liquidado | Decimal |  |
| percentual_empenho | Decimal? (Opcional) |  |
| percentual_liquidado | Decimal? (Opcional) |  |
| mes | Int |  |
| mes_corrente | Boolean |  |
| data_referencia | DateTime |  |
| sobrescrito_em | DateTime? (Opcional) |  |
| sobrescrito_por | Int? (Opcional) |  |
| sobrescritor | Pessoa? (Opcional) | FK |
| OrcamentoRealizado | Relacionamento -> OrcamentoRealizado | FK |
| orcamento_realizado_id | Int |  |

---

### PdmDotacaoPlanejado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| pressao_orcamentaria | Boolean |  |
| soma_valor_planejado | Decimal |  |

---

### PdmDotacaoProcesso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### PdmDotacaoProcessoNota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| dotacao_processo_nota | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### PdmDotacaoRealizado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### PdmOrcamentoConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int |  |
| ano_referencia | Int |  |
| previsao_custo_disponivel | Boolean |  |
| planejado_disponivel | Boolean |  |
| execucao_disponivel | Boolean |  |
| execucao_disponivel_meses | Int[] (Lista) |  |
| pdm | Relacionamento -> Pdm | FK |

---

### PdmOrcamentoRealizadoConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ano_referencia | Int |  |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| ultima_revisao | Boolean? (Opcional) |  |
| atualizado_em | DateTime |  |
| atualizado_por | Int |  |
| atualizador | Relacionamento -> Pessoa | FK |
| execucao_concluida | Boolean |  |

---

### PdmOrcamentoRealizadoControleConcluido (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ano_referencia | Int |  |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| criado_em | DateTime |  |
| referencia_mes | Int? (Opcional) |  |
| referencia_dia_abertura | Int? (Opcional) |  |
| referencia_dia_fechamento | Int? (Opcional) |  |
| execucao_concluida | Boolean |  |

---

### PortfolioDotacaoPlanejado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| pressao_orcamentaria | Boolean |  |
| soma_valor_planejado | Decimal |  |

---

### PortfolioDotacaoProcesso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### PortfolioDotacaoProcessoNota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| dotacao_processo | String |  |
| dotacao_processo_nota | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### PortfolioDotacaoRealizado (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| portfolio_id | Int |  |
| portfolio | Relacionamento -> Portfolio | FK |
| ano_referencia | Int |  |
| dotacao | String |  |
| soma_valor_empenho | Decimal |  |
| soma_valor_liquidado | Decimal |  |

---

### SofEntidade (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| ano | Int | PK |
| atualizado_em | DateTime |  |
| dados | Json |  |

---

## Cronograma

**Origem/Funcionalidade:** Módulo Cronograma (Backend: /cronograma). Gestão de tempo, etapas e tarefas de projetos e metas.

### Cronograma (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| meta_id | Int? (Opcional) |  |
| meta | Meta? (Opcional) | FK |
| iniciativa_id | Int? (Opcional) |  |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade_id | Int? (Opcional) |  |
| atividade | Atividade? (Opcional) | FK |
| descricao | String? (Opcional) |  |
| observacao | String? (Opcional) |  |
| inicio_previsto | DateTime? (Opcional) |  |
| termino_previsto | DateTime? (Opcional) |  |
| inicio_real | DateTime? (Opcional) |  |
| termino_real | DateTime? (Opcional) |  |
| regionalizavel | Boolean |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| CronogramaOrgao | CronogramaOrgao[] (Lista) |  |
| CronogramaEtapa | CronogramaEtapa[] (Lista) |  |
| percentual_execucao | Int? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| ativo | Boolean |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| etapa | Etapa[] (Lista) |  |

---

### CronogramaEtapa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| cronograma_id | Int |  |
| cronograma | Relacionamento -> Cronograma | FK |
| etapa_id | Int |  |
| etapa | Relacionamento -> Etapa | FK |
| nivel | CronogramaEtapaNivel |  |
| ordem | Int |  |
| inativo | Boolean |  |
| data_inativacao | DateTime? (Opcional) |  |

---

### CronogramaOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| cronograma_id | Int |  |
| cronograma | Relacionamento -> Cronograma | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |

---

### CronogramaTerminoPlanejadoConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| modulo_sistema | ModuloSistema | Unique |
| para | String |  |
| texto_inicial | String |  |
| texto_final | String |  |
| assunto_global | String |  |
| assunto_orgao | String |  |

---

### Etapa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| etapa_pai_id | Int? (Opcional) |  |
| etapa_pai | Etapa? (Opcional) | FK |
| etapa_filha | Etapa[] (Lista) | FK |
| regiao_id | Int? (Opcional) |  |
| regiao | Regiao? (Opcional) | FK |
| cronograma_id | Int |  |
| cronograma | Relacionamento -> Cronograma | FK |
| titulo | String? (Opcional) |  |
| nivel | String? (Opcional) |  |
| descricao | String? (Opcional) |  |
| inicio_previsto | DateTime? (Opcional) |  |
| termino_previsto | DateTime? (Opcional) |  |
| inicio_real | DateTime? (Opcional) |  |
| termino_real | DateTime? (Opcional) |  |
| prazo_inicio | DateTime? (Opcional) |  |
| prazo_termino | DateTime? (Opcional) |  |
| status | String? (Opcional) |  |
| CronogramaEtapa | CronogramaEtapa[] (Lista) |  |
| peso | Int? (Opcional) |  |
| percentual_execucao | Int? (Opcional) |  |
| n_filhos_imediatos | Int? (Opcional) |  |
| endereco_obrigatorio | Boolean |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| variavel_id | Int? (Opcional) |  |
| variavel | Variavel? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| responsaveis | EtapaResponsavel[] (Lista) |  |
| GeoLocalizacaoReferencia | GeoLocalizacaoReferencia[] (Lista) |  |
| PdmPerfil | PdmPerfil[] (Lista) |  |

---

### EtapaResponsavel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| etapa_id | Int |  |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| etapa | Relacionamento -> Etapa | FK |

---

### Tarefa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tarefa_cronograma | Relacionamento -> TarefaCronograma | FK |
| tarefa_cronograma_id | Int |  |
| orgao_id | Int? (Opcional) |  |
| tarefa_pai_id | Int? (Opcional) |  |
| tarefa_pai | Tarefa? (Opcional) | FK |
| filhos | Tarefa[] (Lista) | FK |
| orgao | Orgao? (Opcional) | FK |
| tarefa | String |  |
| descricao | String |  |
| recursos | String |  |
| numero | Int |  |
| nivel | Int |  |
| inicio_planejado | DateTime? (Opcional) |  |
| termino_planejado | DateTime? (Opcional) |  |
| duracao_planejado | Int? (Opcional) |  |
| n_dep_inicio_planejado | Int |  |
| n_dep_termino_planejado | Int |  |
| ordem_topologica_inicio_planejado | Int[] (Lista) |  |
| ordem_topologica_termino_planejado | Int[] (Lista) |  |
| inicio_real | DateTime? (Opcional) |  |
| termino_real | DateTime? (Opcional) |  |
| duracao_real | Int? (Opcional) |  |
| inicio_planejado_calculado | Boolean |  |
| termino_planejado_calculado | Boolean |  |
| duracao_planejado_calculado | Boolean |  |
| db_projecao_inicio | DateTime? (Opcional) |  |
| db_projecao_termino | DateTime? (Opcional) |  |
| db_projecao_atraso | Int? (Opcional) |  |
| n_filhos_imediatos | Int |  |
| custo_estimado | Float? (Opcional) |  |
| custo_real | Float? (Opcional) |  |
| eh_marco | Boolean |  |
| percentual_concluido | Float? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| dependencias | TarefaDependente[] (Lista) | FK |
| ref_dependentes | TarefaDependente[] (Lista) | FK |
| RiscoTarefa | RiscoTarefa[] (Lista) |  |
| AvisoEmail | AvisoEmail[] (Lista) |  |
| transferencia_fase_id | Int? (Opcional) |  |
| transferencia_fase | TransferenciaAndamento? (Opcional) | FK |
| transferencia_tarefa_id | Int? (Opcional) |  |
| transferencia_tarefa | TransferenciaAndamentoTarefa? (Opcional) | FK |
| distribuicao_recurso_id | Int? (Opcional) |  |
| distribuicao_recurso | DistribuicaoRecurso? (Opcional) | FK |

---

### TarefaCronograma (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int? (Opcional) |  |
| transferencia_id | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| transferencia | Transferencia? (Opcional) | FK |
| previsao_inicio | DateTime? (Opcional) |  |
| previsao_termino | DateTime? (Opcional) |  |
| previsao_duracao | Int? (Opcional) |  |
| realizado_inicio | DateTime? (Opcional) |  |
| realizado_termino | DateTime? (Opcional) |  |
| realizado_duracao | Int? (Opcional) |  |
| realizado_custo | Float? (Opcional) |  |
| projecao_termino | DateTime? (Opcional) |  |
| tolerancia_atraso | Int |  |
| em_atraso | Boolean |  |
| atraso | Int? (Opcional) |  |
| percentual_concluido | Int? (Opcional) |  |
| percentual_atraso | Int? (Opcional) |  |
| status_cronograma | String? (Opcional) |  |
| previsao_custo | Float? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| tarefas_proximo_recalculo | DateTime |  |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Tarefa | Tarefa[] (Lista) |  |
| AvisoEmail | AvisoEmail[] (Lista) |  |

---

### TarefaDependente (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tarefa_id | Int |  |
| dependencia_tarefa_id | Int |  |
| tipo | TarefaDependenteTipo |  |
| latencia | Int |  |
| tarefa | Relacionamento -> Tarefa | FK |
| tarefas_dependente | Relacionamento -> Tarefa | FK |

---

### view_meta_cronograma (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| cronograma_id | Int | PK |
| meta_id | Int |  |

---

## Parlamentar / Política

**Origem/Funcionalidade:** Módulo Parlamentar (Frontend: /parlamentares, Backend: /parlamentar). Gestão de deputados, vereadores, bancadas e eleições.

### Bancada (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| sigla | String |  |
| descricao | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| partidos | BancadaPartido[] (Lista) |  |

---

### BancadaPartido (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bancada_id | Int |  |
| bancada | Relacionamento -> Bancada | FK |
| partido_id | Int |  |
| partido | Relacionamento -> Partido | FK |

---

### Eleicao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | EleicaoTipo |  |
| ano | Int |  |
| atual_para_mandatos | Boolean |  |
| removido_em | DateTime? (Opcional) |  |
| mandatos | ParlamentarMandato[] (Lista) |  |
| comparecimentos | EleicaoComparecimento[] (Lista) |  |

---

### EleicaoComparecimento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| eleicao_id | Int |  |
| eleicao | Relacionamento -> Eleicao | FK |
| nivel | DadosEleicaoNivel |  |
| valor | Int |  |
| regiao_id | Int |  |
| regiao | Relacionamento -> Regiao | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### MandatoRepresentatividade (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| regiao_id | Int |  |
| regiao | Relacionamento -> Regiao | FK |
| mandato_id | Int |  |
| mandato | Relacionamento -> ParlamentarMandato | FK |
| nivel | DadosEleicaoNivel |  |
| municipio_tipo | MunicipioTipo? (Opcional) |  |
| numero_votos | Int |  |
| ranking | Int? (Opcional) |  |
| pct_participacao | Float? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### Parlamentar (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| nome_popular | String |  |
| nascimento | DateTime? (Opcional) |  |
| telefone | String? (Opcional) |  |
| email | String? (Opcional) |  |
| em_atividade | Boolean |  |
| uf_nascimento | ParlamentarUF? (Opcional) |  |
| cpf | String? (Opcional) |  |
| vetores_busca | Unsupported("tsvector")? (Opcional) |  |
| foto_upload_id | Int? (Opcional) |  |
| foto | Arquivo? (Opcional) | FK |
| cargo_mais_recente | ParlamentarCargo? (Opcional) |  |
| partido_mais_recente | String? (Opcional) |  |
| tem_mandato | Boolean? (Opcional) |  |
| mandatos | ParlamentarMandato[] (Lista) |  |
| equipe | ParlamentarEquipe[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| transferencias | TransferenciaParlamentar[] (Lista) |  |
| distribuicoes | DistribuicaoParlamentar[] (Lista) |  |
| view_ranking_transferencias | ViewRankingTransferenciaParlamentar[] (Lista) |  |

---

### ParlamentarEquipe (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| parlamentar_id | Int |  |
| parlamentar | Relacionamento -> Parlamentar | FK |
| mandato_id | Int? (Opcional) |  |
| mandato | ParlamentarMandato? (Opcional) | FK |
| tipo | ParlamentarEquipeTipo |  |
| nome | String |  |
| telefone | String |  |
| email | String |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ParlamentarMandato (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| parlamentar_id | Int |  |
| parlamentar | Relacionamento -> Parlamentar | FK |
| eleicao_id | Int |  |
| eleicao | Relacionamento -> Eleicao | FK |
| partido_candidatura_id | Int |  |
| partido_candidatura | Relacionamento -> Partido | FK |
| partido_atual_id | Int |  |
| partido_atual | Relacionamento -> Partido | FK |
| atuacao | String? (Opcional) |  |
| biografia | String? (Opcional) |  |
| telefone | String? (Opcional) |  |
| email | String? (Opcional) |  |
| gabinete | String? (Opcional) |  |
| eleito | Boolean |  |
| cargo | ParlamentarCargo |  |
| uf | ParlamentarUF |  |
| suplencia | ParlamentarSuplente? (Opcional) |  |
| endereco | String? (Opcional) |  |
| votos_estado | BigInt? (Opcional) |  |
| votos_capital | BigInt? (Opcional) |  |
| votos_interior | BigInt? (Opcional) |  |
| codigo_identificador | String? (Opcional) |  |
| mandato_principal_id | Int? (Opcional) |  |
| mandato_principal | ParlamentarMandato? (Opcional) | FK |
| suplentes | ParlamentarMandato[] (Lista) | FK |
| representatividade | MandatoRepresentatividade[] (Lista) |  |
| equipe | ParlamentarEquipe[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### Partido (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| sigla | String |  |
| numero | Int |  |
| observacao | String? (Opcional) |  |
| fundacao | DateTime? (Opcional) |  |
| encerramento | DateTime? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime? (Opcional) |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| mandatos_candidatura | ParlamentarMandato[] (Lista) | FK |
| mandatos_atual | ParlamentarMandato[] (Lista) | FK |
| bancadas | BancadaPartido[] (Lista) |  |
| transferencias | TransferenciaParlamentar[] (Lista) |  |
| distribuicoes | DistribuicaoParlamentar[] (Lista) |  |

---

### view_parlamentares_mandatos_part_atual (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| virtual_id | String | Unique |
| id | Int |  |
| nome_civil | String |  |
| nome_parlamentar | String |  |
| partido_sigla | String |  |
| cargo | ParlamentarCargo |  |
| uf | ParlamentarUF |  |
| titular_suplente | String? (Opcional) |  |
| endereco | String? (Opcional) |  |
| gabinete | String? (Opcional) |  |
| telefone | String? (Opcional) |  |
| dia_aniversario | Int? (Opcional) |  |
| mes_aniversario | Int? (Opcional) |  |
| email | String? (Opcional) |  |
| zona_atuacao | String? (Opcional) |  |
| ano_eleicao | Int? (Opcional) |  |
| eleicao_id | Int? (Opcional) |  |
| partido_atual_id | Int? (Opcional) |  |

---

## Administração / Core

**Origem/Funcionalidade:** Módulo Administrativo / Core (Frontend: /users, /organs). Gestão de usuários, órgãos, perfis de acesso, relatórios gerais e configurações do sistema.

### Arquivo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | String |  |
| criador | Pessoa? (Opcional) | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizador | Pessoa? (Opcional) | FK |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| caminho | String |  |
| nome_original | String |  |
| mime_type | String? (Opcional) |  |
| tamanho_bytes | Int |  |
| descricao | String? (Opcional) |  |
| tipo_documento_id | Int? (Opcional) |  |
| diretorio_caminho | String? (Opcional) |  |
| TipoDocumento | TipoDocumento? (Opcional) | FK |
| Tag | Tag[] (Lista) |  |
| Regiao | Regiao[] (Lista) |  |
| ArquivoDocumento | PdmDocumento[] (Lista) |  |
| Pdm | Pdm[] (Lista) |  |
| VariavelCicloFisicoDocumento | VariavelCicloFisicoDocumento[] (Lista) |  |
| MetaCicloFisicoAnaliseDocumento | MetaCicloFisicoAnaliseDocumento[] (Lista) |  |
| Relatorio | Relatorio[] (Lista) |  |
| projeto_documentos | ProjetoDocumento[] (Lista) |  |
| fotosParlamentar | Parlamentar[] (Lista) |  |
| ImportacaoLogInput | ImportacaoOrcamento[] (Lista) | FK |
| ImportacaoLogOutput | ImportacaoOrcamento[] (Lista) | FK |
| FormulaCompostaCicloFisicoDocumento | FormulaCompostaCicloFisicoDocumento[] (Lista) |  |
| transferencia_anexos | TransferenciaAnexo[] (Lista) |  |
| VariavelGlobalCicloDocumento | VariavelGlobalCicloDocumento[] (Lista) |  |
| AtualizacaoEmLote | AtualizacaoEmLote[] (Lista) |  |

---

### Diretorio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| caminho | String |  |
| projeto_id | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| transferencia_id | Int? (Opcional) |  |
| transferencia | Transferencia? (Opcional) | FK |
| pdm_id | Int? (Opcional) |  |
| pdm | Pdm? (Opcional) | FK |

---

### GrupoTematico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| programa_habitacional | Boolean |  |
| unidades_habitacionais | Boolean |  |
| unidades_atendidas | Boolean |  |
| familias_beneficiadas | Boolean |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Projeto | Projeto[] (Lista) |  |

---

### LogGenerico (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| contexto | String |  |
| ip | String |  |
| log | String |  |
| pessoa_sessao_id | Int? (Opcional) |  |
| pessoa_id | Int? (Opcional) |  |
| pessoa | Pessoa? (Opcional) | FK |
| pessoa_sessao | PessoaSessao? (Opcional) | FK |
| criado_em | DateTime |  |

---

### Orgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| sigla | String |  |
| descricao | String |  |
| tipo_orgao_id | Int |  |
| tipo_orgao | Relacionamento -> TipoOrgao | FK |
| pessoa_fisica | PessoaFisica[] (Lista) |  |
| cnpj | String? (Opcional) |  |
| email | String? (Opcional) |  |
| secretario_responsavel | String? (Opcional) |  |
| oficial | Boolean |  |
| nivel | Int |  |
| parente_id | Int? (Opcional) |  |
| OrgaoAcima | Orgao? (Opcional) | FK |
| OrgaosAbaixo | Orgao[] (Lista) | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| meta_orgao | MetaOrgao[] (Lista) |  |
| meta_responsavel | MetaResponsavel[] (Lista) |  |
| Variavel | Variavel[] (Lista) |  |
| iniciativa_orgao | IniciativaOrgao[] (Lista) |  |
| iniciativa_responsavel | IniciativaResponsavel[] (Lista) |  |
| atividade_orgao | AtividadeOrgao[] (Lista) |  |
| atividade_responsavel | AtividadeResponsavel[] (Lista) |  |
| CronogramaOrgao | CronogramaOrgao[] (Lista) |  |
| tarefas | Tarefa[] (Lista) |  |
| PlanoAcao | PlanoAcao[] (Lista) |  |
| projetos_participando | ProjetoOrgaoParticipante[] (Lista) |  |
| PortifolioOrgao | PortfolioOrgao[] (Lista) |  |
| orgao_responsavel | Projeto[] (Lista) | FK |
| orgao_origem | Projeto[] (Lista) | FK |
| orgao_executor | Projeto[] (Lista) | FK |
| projetos_geridos | Projeto[] (Lista) | FK |
| projeto_colaborados | Projeto[] (Lista) | FK |
| GrupoPortfolio | GrupoPortfolio[] (Lista) |  |
| GrupoPortfolioPessoa | GrupoPortfolioPessoa[] (Lista) |  |
| ProjetoEquipe | ProjetoEquipe[] (Lista) |  |
| GrupoPainelExterno | GrupoPainelExterno[] (Lista) |  |
| GrupoPainelExternoPessoa | GrupoPainelExternoPessoa[] (Lista) |  |
| TransferenciasOrgao | Transferencia[] (Lista) | FK |
| TransferenciasSecretaria | Transferencia[] (Lista) | FK |
| distribuicao_recursos | DistribuicaoRecurso[] (Lista) |  |
| Nota | Nota[] (Lista) |  |
| NotaEnderecamento | NotaEnderecamento[] (Lista) |  |
| transferenciaAndamento | TransferenciaAndamento[] (Lista) |  |
| transferenciaAndamentoTarefa | TransferenciaAndamentoTarefa[] (Lista) |  |
| PdmOrcamentoRealizadoConfig | PdmOrcamentoRealizadoConfig[] (Lista) |  |
| ViewNotaComOrdem | ViewNotas[] (Lista) |  |
| PdmPerfil | PdmPerfil[] (Lista) |  |
| Pdm | Pdm[] (Lista) |  |
| statusDistribuicaoRecusro | DistribuicaoRecursoStatus[] (Lista) |  |
| ViewProjetoMDO | ViewProjetoMDO[] (Lista) |  |
| VariavelProprietario | Variavel[] (Lista) | FK |
| MedicaoOrgaoVariavel | Variavel[] (Lista) | FK |
| MalidacaoOrgaoVariavel | Variavel[] (Lista) | FK |
| MiberacaoOrgaoVariavel | Variavel[] (Lista) | FK |
| GrupoResponsavelEquipe | GrupoResponsavelEquipe[] (Lista) |  |
| GrupoResponsavelEquipePessoa | GrupoResponsavelEquipeParticipante[] (Lista) |  |
| contratos | Contrato[] (Lista) |  |
| ViewVariavelGlobalQSouResp | ViewVariavelGlobal[] (Lista) | FK |
| ViewVariavelGlobalQSouProp | ViewVariavelGlobal[] (Lista) | FK |
| GrupoResponsavelEquipeColaborador | GrupoResponsavelEquipeResponsavel[] (Lista) |  |
| FormulaComposta | FormulaComposta[] (Lista) |  |
| ViewPainelEstrategicoProjetos | ViewPainelEstrategicoProjetos[] (Lista) |  |
| ViewProjetoV2Resp | ViewProjetoV2[] (Lista) | FK |
| ViewProjetoV2Origem | ViewProjetoV2[] (Lista) | FK |
| AtualizacaoEmLote | AtualizacaoEmLote[] (Lista) |  |

---

### PerfilAcesso (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| descricao | String? (Opcional) |  |
| modulos_sistemas | ModuloSistema[] (Lista) |  |
| autogerenciavel | Boolean |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| perfil_privilegio | PerfilPrivilegio[] (Lista) |  |
| pessoa_perfil | PessoaPerfil[] (Lista) |  |

---

### PerfilPrivilegio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| perfil_acesso_id | Int |  |
| privilegio_id | Int |  |
| perfil_acesso | Relacionamento -> PerfilAcesso | FK |
| privilegio | Relacionamento -> Privilegio | FK |

---

### Pessoa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| email | String | Unique |
| senha | String |  |
| nome_exibicao | String |  |
| nome_completo | String |  |
| atualizado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| criado_por | Int? (Opcional) |  |
| qtde_senha_invalida | Int |  |
| senha_atualizada_em | DateTime? (Opcional) |  |
| senha_bloqueada | Boolean |  |
| senha_bloqueada_em | DateTime? (Opcional) |  |
| desativado | Boolean |  |
| desativado_em | DateTime? (Opcional) |  |
| desativado_por | Int? (Opcional) |  |
| desativado_motivo | String? (Opcional) |  |
| pessoa_fisica_id | Int? (Opcional) |  |
| equipe_pdm_tipos | TipoPdm[] (Lista) |  |
| perfis_equipe_pdm | PerfilResponsavelEquipe[] (Lista) |  |
| perfis_equipe_ps | PerfilResponsavelEquipe[] (Lista) |  |
| sobreescrever_modulos | Boolean |  |
| modulos_permitidos | ModuloSistema[] (Lista) |  |
| ProjetoOrigemQcriei | CompromissoOrigem[] (Lista) | FK |
| ProjetoOrigemQAtualizei | CompromissoOrigem[] (Lista) | FK |
| ProjetoOrigemQRemovi | CompromissoOrigem[] (Lista) | FK |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| desativador | Pessoa? (Opcional) | FK |
| pessoa_fisica | PessoaFisica? (Opcional) | FK |
| PessoasQueAtualizei | Pessoa[] (Lista) | FK |
| PessoasQueCriei | Pessoa[] (Lista) | FK |
| PessoasQueDesativei | Pessoa[] (Lista) | FK |
| PessoaPerfil | PessoaPerfil[] (Lista) |  |
| PessoaSessoesAtivas | PessoaSessaoAtiva[] (Lista) |  |
| OrgaoQueCriei | Orgao[] (Lista) | FK |
| OrgaoQueRemovi | Orgao[] (Lista) | FK |
| OrgaoQueAtualizei | Orgao[] (Lista) | FK |
| TipoOrgaoQueCriei | TipoOrgao[] (Lista) | FK |
| TipoOrgaoQueRemovi | TipoOrgao[] (Lista) | FK |
| TipoOrgaoQueAtualizei | TipoOrgao[] (Lista) | FK |
| PerfilAcessoQueCriei | PerfilAcesso[] (Lista) | FK |
| PerfilAcessoQueRemovi | PerfilAcesso[] (Lista) | FK |
| PerfilAcessoQueAtualizei | PerfilAcesso[] (Lista) | FK |
| OdsQueCriei | Ods[] (Lista) | FK |
| OdsQueRemovi | Ods[] (Lista) | FK |
| OdsQueAtualizei | Ods[] (Lista) | FK |
| SubTemaQueCriei | SubTema[] (Lista) | FK |
| SubTemaQueRemovi | SubTema[] (Lista) | FK |
| SubTemaQueAtualizei | SubTema[] (Lista) | FK |
| processoSeiQueCriei | ProjetoRegistroSei[] (Lista) | FK |
| processoSeiQueRemovi | ProjetoRegistroSei[] (Lista) | FK |
| processoSeiQueAtualizei | ProjetoRegistroSei[] (Lista) | FK |
| EixoQueCriei | MacroTema[] (Lista) | FK |
| EixoQueRemovi | MacroTema[] (Lista) | FK |
| EixoQueAtualizei | MacroTema[] (Lista) | FK |
| PDMQueCriei | Pdm[] (Lista) | FK |
| PDMQueDesativei | Pdm[] (Lista) | FK |
| PDMQueAtualizei | Pdm[] (Lista) | FK |
| PDMQueRemovi | Pdm[] (Lista) | FK |
| FormulaCompostaQueCriei | FormulaComposta[] (Lista) | FK |
| FormulaCompostaQueDesativei | FormulaComposta[] (Lista) | FK |
| FormulaCompostaQueAtualizei | FormulaComposta[] (Lista) | FK |
| OEQueCriei | Tema[] (Lista) | FK |
| OEQueDesativei | Tema[] (Lista) | FK |
| OEQueAtualizei | Tema[] (Lista) | FK |
| TagQueCriei | Tag[] (Lista) | FK |
| TagQueDesativei | Tag[] (Lista) | FK |
| TagQueAtualizei | Tag[] (Lista) | FK |
| FRQueCriei | FonteRecurso[] (Lista) | FK |
| FRQueDesativei | FonteRecurso[] (Lista) | FK |
| FRQueAtualizei | FonteRecurso[] (Lista) | FK |
| TipoDocQueCriei | TipoDocumento[] (Lista) | FK |
| TipoDocQueDesativei | TipoDocumento[] (Lista) | FK |
| TipoDocQueAtualizei | TipoDocumento[] (Lista) | FK |
| RegiaoQueCriei | Regiao[] (Lista) | FK |
| RegiaoQueDesativei | Regiao[] (Lista) | FK |
| RegiaoQueAtualizei | Regiao[] (Lista) | FK |
| ArquivoQueCriei | Arquivo[] (Lista) | FK |
| ArquivosQueAtualizei | Arquivo[] (Lista) | FK |
| ArquivoDocQueCriei | PdmDocumento[] (Lista) | FK |
| ArquivoDocQueDesativei | PdmDocumento[] (Lista) | FK |
| ArquivoDocQueAtualizei | PdmDocumento[] (Lista) | FK |
| PPArquivoDocQueCriei | ProjetoDocumento[] (Lista) | FK |
| PPArquivoDocQueDesativei | ProjetoDocumento[] (Lista) | FK |
| PPArquivoDocQueAtualizei | ProjetoDocumento[] (Lista) | FK |
| MetaQueCriei | Meta[] (Lista) | FK |
| MetaQueDesativei | Meta[] (Lista) | FK |
| MetaQueAtualizei | Meta[] (Lista) | FK |
| IndicadorQueCriei | Indicador[] (Lista) | FK |
| IndicadorQueRemovi | Indicador[] (Lista) | FK |
| IndicadorQueAtualizei | Indicador[] (Lista) | FK |
| UnidadeQueCriei | UnidadeMedida[] (Lista) | FK |
| UnidadeQueRemovi | UnidadeMedida[] (Lista) | FK |
| UnidadeQueAtualizei | UnidadeMedida[] (Lista) | FK |
| IndicadorVariavel | IndicadorVariavel[] (Lista) | FK |
| IniciativasQueCriei | Iniciativa[] (Lista) | FK |
| IniciativasQueRemovi | Iniciativa[] (Lista) | FK |
| IniciativasQueAtualizei | Iniciativa[] (Lista) | FK |
| IniciativasQueSouResp | IniciativaResponsavel[] (Lista) | FK |
| AtividadesQueCriei | Atividade[] (Lista) | FK |
| AtividadesQueRemovi | Atividade[] (Lista) | FK |
| AtividadesQueAtualizei | Atividade[] (Lista) | FK |
| AtividadesQueSouResp | AtividadeResponsavel[] (Lista) | FK |
| VariavelResponsavel | VariavelResponsavel[] (Lista) |  |
| AtualizouSerieVariavel | SerieVariavel[] (Lista) | FK |
| ConferiuSerieVariavel | SerieVariavel[] (Lista) | FK |
| CronogramaOrgao | CronogramaOrgao[] (Lista) |  |
| CronogramasQueCriei | Cronograma[] (Lista) | FK |
| CronogramasQueRemovi | Cronograma[] (Lista) | FK |
| CronogramasQueAtualizei | Cronograma[] (Lista) | FK |
| PortfolioQueCriei | Portfolio[] (Lista) | FK |
| PortfolioQueRemovi | Portfolio[] (Lista) | FK |
| PortfolioQueAtualizei | Portfolio[] (Lista) | FK |
| EtapasQueCriei | Etapa[] (Lista) | FK |
| EtapasQueRemovi | Etapa[] (Lista) | FK |
| EtapasQueAtualizei | Etapa[] (Lista) | FK |
| PlanoAcaoMonitoramentoQueCriei | PlanoAcaoMonitoramento[] (Lista) | FK |
| PlanoAcaoMonitoramentoQueAtualizei | PlanoAcaoMonitoramento[] (Lista) | FK |
| PlanoAcaoMonitoramentoQueRemovi | PlanoAcaoMonitoramento[] (Lista) | FK |
| TiposDeTransferenciaQueCriei | TransferenciaTipo[] (Lista) | FK |
| TiposDeTransferenciaQueAtualizei | TransferenciaTipo[] (Lista) | FK |
| TiposDeTransferenciaQueRemovi | TransferenciaTipo[] (Lista) | FK |
| WorkflowsQueCriei | Workflow[] (Lista) | FK |
| WorkflowsQueAtualizei | Workflow[] (Lista) | FK |
| WorkflowsQueRemovi | Workflow[] (Lista) | FK |
| EtapasDeWorkflowsQueCriei | WorkflowEtapa[] (Lista) | FK |
| EtapasDeWorkflowsQueAtualizei | WorkflowEtapa[] (Lista) | FK |
| EtapasDeWorkflowsQueRemovi | WorkflowEtapa[] (Lista) | FK |
| FasesDeWorkflowsQueCriei | WorkflowFase[] (Lista) | FK |
| FasesDeWorkflowsQueAtualizei | WorkflowFase[] (Lista) | FK |
| FasesDeWorkflowsQueRemovi | WorkflowFase[] (Lista) | FK |
| SituacoesDeWorkflowsQueCriei | WorkflowSituacao[] (Lista) | FK |
| SituacoesDeWorkflowsQueAtualizei | WorkflowSituacao[] (Lista) | FK |
| SituacoesDeWorkflowsQueRemovi | WorkflowSituacao[] (Lista) | FK |
| PaineisQueCriei | Painel[] (Lista) | FK |
| PaineisQueRemovi | Painel[] (Lista) | FK |
| PaineisQueAtualizei | Painel[] (Lista) | FK |
| PessoaAcessoPdm | PessoaAcessoPdm[] (Lista) |  |
| GruposDePaineisQueCriei | GrupoPainel[] (Lista) | FK |
| GruposDePaineisQueRemovi | GrupoPainel[] (Lista) | FK |
| GruposDePaineisQueParticipo | PessoaGrupoPainel[] (Lista) |  |
| VariavelCicloFisicoQualitativoCriador | VariavelCicloFisicoQualitativo[] (Lista) | FK |
| VariavelCicloFisicoQualitativoRemovedor | VariavelCicloFisicoQualitativo[] (Lista) | FK |
| VariavelCicloFisicoDocumentoCriador | VariavelCicloFisicoDocumento[] (Lista) | FK |
| VariavelCicloFisicoDocumentoRemovedor | VariavelCicloFisicoDocumento[] (Lista) | FK |
| PedidoComplementacaoCriador | PedidoComplementacao[] (Lista) | FK |
| PedidoComplementacaoAtendeu | PedidoComplementacao[] (Lista) | FK |
| PedidoComplementacaoRemovedor | PedidoComplementacao[] (Lista) | FK |
| MetaCicloFisicoAnaliseCriador | MetaCicloFisicoAnalise[] (Lista) | FK |
| MetaCicloFisicoAnaliseRemovedor | MetaCicloFisicoAnalise[] (Lista) | FK |
| MetaCicloFisicoFechamentoCriador | MetaCicloFisicoFechamento[] (Lista) | FK |
| MetaCicloFisicoFechamentoRemovedor | MetaCicloFisicoFechamento[] (Lista) | FK |
| FormulaCompostaCicloFisicoQualitativoCriador | FormulaCompostaCicloFisicoQualitativo[] (Lista) | FK |
| FormulaCompostaCicloFisicoQualitativoRemovedor | FormulaCompostaCicloFisicoQualitativo[] (Lista) | FK |
| FormulaCompostaCicloFisicoDocumentoCriador | FormulaCompostaCicloFisicoDocumento[] (Lista) | FK |
| FormulaCompostaCicloFisicoDocumentoRemovedor | FormulaCompostaCicloFisicoDocumento[] (Lista) | FK |
| MetaCicloFisicoRiscoCriador | MetaCicloFisicoRisco[] (Lista) | FK |
| MetaCicloFisicoRiscoRemovedor | MetaCicloFisicoRisco[] (Lista) | FK |
| MetaCicloFisicoAnaliseDocumentoCriador | MetaCicloFisicoAnaliseDocumento[] (Lista) | FK |
| MetaCicloFisicoAnaliseDocumentoRemovedor | MetaCicloFisicoAnaliseDocumento[] (Lista) | FK |
| EtapaResponsavel | EtapaResponsavel[] (Lista) |  |
| MetaOrcamentoCriados | OrcamentoPrevisto[] (Lista) | FK |
| MetaOrcamentoRemovidos | OrcamentoPrevisto[] (Lista) | FK |
| MetaOrcamentoAtualizados | OrcamentoPrevisto[] (Lista) | FK |
| OrcamentoPlanejadoCriados | OrcamentoPlanejado[] (Lista) | FK |
| OrcamentoPlanejadoRemovidos | OrcamentoPlanejado[] (Lista) | FK |
| OrcamentoRealizadoCriados | OrcamentoRealizado[] (Lista) | FK |
| OrcamentoRealizadoRemovidos | OrcamentoRealizado[] (Lista) | FK |
| OrcamentoRealizadoItem | OrcamentoRealizadoItem[] (Lista) | FK |
| RelatorioQueFiz | Relatorio[] (Lista) | FK |
| RelatorioQueRemovi | Relatorio[] (Lista) | FK |
| ProjetoLicoesAprendidasQCriei | ProjetoLicaoAprendida[] (Lista) | FK |
| ProjetoLicoesAprendidasQRemovi | ProjetoLicaoAprendida[] (Lista) | FK |
| AditamentosQueCriei | DistribuicaoRecursoAditamento[] (Lista) |  |
| ppResponsavel | Projeto[] (Lista) | FK |
| ppQueCriei | Projeto[] (Lista) | FK |
| ppSelecionado | Projeto[] (Lista) | FK |
| ppEm_planejamento | Projeto[] (Lista) | FK |
| ppArquivado | Projeto[] (Lista) | FK |
| ppSuspenso | Projeto[] (Lista) | FK |
| ppRestaurou | Projeto[] (Lista) | FK |
| ppValidado | Projeto[] (Lista) | FK |
| ppFinalizouPlan | Projeto[] (Lista) | FK |
| ppCancelou | Projeto[] (Lista) | FK |
| ppReiniciou | Projeto[] (Lista) | FK |
| ppIniciou | Projeto[] (Lista) | FK |
| ppTerminou | Projeto[] (Lista) | FK |
| RiscosQueCriei | ProjetoRisco[] (Lista) | FK |
| RiscosQueRemovi | ProjetoRisco[] (Lista) | FK |
| RiscosQueEditei | ProjetoRisco[] (Lista) | FK |
| PlanosDeAcaoQueCriei | PlanoAcao[] (Lista) | FK |
| PlanosDeAcaoQueRemovi | PlanoAcao[] (Lista) | FK |
| PlanosDeAcaoQueEditei | PlanoAcao[] (Lista) | FK |
| EncaminhamentosQueCriei | ProjetoAcompanhamentoItem[] (Lista) | FK |
| EncaminhamentosQueRemovi | ProjetoAcompanhamentoItem[] (Lista) | FK |
| EncaminhamentosQueEditei | ProjetoAcompanhamentoItem[] (Lista) | FK |
| ProjetoEquipeQueEstou | ProjetoEquipe[] (Lista) | FK |
| ProjetoEquipeQueRemovi | ProjetoEquipe[] (Lista) | FK |
| ProjetoEquipeQueCriei | ProjetoEquipe[] (Lista) | FK |
| OrcamentoPrevistoZeradoQCriei | OrcamentoPrevistoZerado[] (Lista) | FK |
| OrcamentoPrevistoZeradoQRemovi | OrcamentoPrevistoZerado[] (Lista) | FK |
| ImportacaoLog | ImportacaoOrcamento[] (Lista) |  |
| IndicadorFormulaComposta | IndicadorFormulaComposta[] (Lista) | FK |
| TiposAcompanhamentoQueCriei | AcompanhamentoTipo[] (Lista) | FK |
| TiposAcompanhamentoQueAtualizei | AcompanhamentoTipo[] (Lista) | FK |
| TiposAcompanhamentoQueRemovi | AcompanhamentoTipo[] (Lista) | FK |
| PessoaAcessoPdmValido | PessoaAcessoPdmValido? (Opcional) |  |
| MetasQueSouResp | view_meta_pessoa_responsavel[] (Lista) |  |
| MetasQueSouRespNaCp | view_meta_pessoa_responsavel_na_cp[] (Lista) |  |
| MetasQueSouRespOuNao | MetaResponsavel[] (Lista) | FK |
| PdmOrcamentoRealizadoConfig | PdmOrcamentoRealizadoConfig[] (Lista) |  |
| view_meta_responsavel_orcamento | view_meta_responsavel_orcamento[] (Lista) |  |
| variavel_suspensa_log | VariavelSuspensaoLog[] (Lista) |  |
| PessoaSessao | PessoaSessao[] (Lista) |  |
| PessoaAtividadeLog | PessoaAtividadeLog[] (Lista) |  |
| GrupoPortfolioQueCriei | GrupoPortfolio[] (Lista) | FK |
| GrupoPortfolioQueAtualizei | GrupoPortfolio[] (Lista) | FK |
| GrupoPortfoliQueRemovi | GrupoPortfolio[] (Lista) | FK |
| ProjetoGrupoPortfolioQueCriei | ProjetoGrupoPortfolio[] (Lista) | FK |
| ProjetoGrupoPortfolioQueRemovi | ProjetoGrupoPortfolio[] (Lista) | FK |
| PortfolioGrupoPortfolioQueCriei | PortfolioGrupoPortfolio[] (Lista) | FK |
| PortfolioGrupoPortfolioQueRemovi | PortfolioGrupoPortfolio[] (Lista) | FK |
| GrupoPortfolioPessoa | GrupoPortfolioPessoa[] (Lista) |  |
| projetosCompartilhadosEmPortfolioQueCriei | PortfolioProjetoCompartilhado[] (Lista) | FK |
| projetosCompartilhadosEmPortfolioQueRemovi | PortfolioProjetoCompartilhado[] (Lista) | FK |
| projetosCompartilhadosEmPortfolioQueAtualizei | PortfolioProjetoCompartilhado[] (Lista) | FK |
| partidosQueCriei | Partido[] (Lista) | FK |
| partidosQueAtualizei | Partido[] (Lista) | FK |
| partidosQueRemovi | Partido[] (Lista) | FK |
| bancadasQueCriei | Bancada[] (Lista) | FK |
| bancadasQueAtualizei | Bancada[] (Lista) | FK |
| bancadasQueRemovi | Bancada[] (Lista) | FK |
| parlamentaresQueCriei | Parlamentar[] (Lista) | FK |
| parlamentaresQueAtualizei | Parlamentar[] (Lista) | FK |
| parlamentaresQueRemovi | Parlamentar[] (Lista) | FK |
| mandatosQueCriei | ParlamentarMandato[] (Lista) | FK |
| mandatosQueAtualizei | ParlamentarMandato[] (Lista) | FK |
| mandatosQueRemovi | ParlamentarMandato[] (Lista) | FK |
| equipeParlamentarQueCriei | ParlamentarEquipe[] (Lista) | FK |
| equipeParlamentarQueAtualizei | ParlamentarEquipe[] (Lista) | FK |
| equipeParlamentarQueRemovi | ParlamentarEquipe[] (Lista) | FK |
| eleicaoComparecimentoQueCriei | EleicaoComparecimento[] (Lista) | FK |
| eleicaoComparecimentoQueAtualizei | EleicaoComparecimento[] (Lista) | FK |
| eleicaoComparecimentoQueRemovi | EleicaoComparecimento[] (Lista) | FK |
| mandatoRepresentatividadesQueCriei | MandatoRepresentatividade[] (Lista) | FK |
| mandatoRepresentatividadesQueAtualizei | MandatoRepresentatividade[] (Lista) | FK |
| mandatoRepresentatividadesQueRemovi | MandatoRepresentatividade[] (Lista) | FK |
| transferenciasQueCriei | Transferencia[] (Lista) | FK |
| transferenciasQueAtualizei | Transferencia[] (Lista) | FK |
| transferenciasQueRemovi | Transferencia[] (Lista) | FK |
| transferenciaAnexoQueCriei | TransferenciaAnexo[] (Lista) | FK |
| transferenciaAnexoQueAtualizei | TransferenciaAnexo[] (Lista) | FK |
| transferenciaAnexoQueRemovi | TransferenciaAnexo[] (Lista) | FK |
| distribuicoesRecursoQueCriei | DistribuicaoRecurso[] (Lista) | FK |
| distribuicoesRecursoQueAtualizei | DistribuicaoRecurso[] (Lista) | FK |
| distribuicoesRecursoQueRemovi | DistribuicaoRecurso[] (Lista) | FK |
| distribuicoesRecursoSEIQueCriei | DistribuicaoRecursoSei[] (Lista) | FK |
| distribuicoesRecursoSEIQueAtualizei | DistribuicaoRecursoSei[] (Lista) | FK |
| distribuicoesRecursoSEIQueRemovi | DistribuicaoRecursoSei[] (Lista) | FK |
| fluxosWorkflowQueCriei | Fluxo[] (Lista) | FK |
| fluxosWorkflowQueAtualizei | Fluxo[] (Lista) | FK |
| fluxosWorkflowQueRemovi | Fluxo[] (Lista) | FK |
| fasesFluxoWorkflowQueCriei | FluxoFase[] (Lista) | FK |
| fasesFluxoWorkflowQueAtualizei | FluxoFase[] (Lista) | FK |
| fasesFluxoWorkflowQueRemovi | FluxoFase[] (Lista) | FK |
| tarefasFluxoWorkflowQueCriei | FluxoTarefa[] (Lista) | FK |
| tarefasFluxoWorkflowQueAtualizei | FluxoTarefa[] (Lista) | FK |
| tarefasFluxoWorkflowQueRemovi | FluxoTarefa[] (Lista) | FK |
| tarefasWorkflowQueCriei | WorkflowTarefa[] (Lista) | FK |
| tarefasWorkflowQueAtualizei | WorkflowTarefa[] (Lista) | FK |
| tarefasWorkflowQueRemovi | WorkflowTarefa[] (Lista) | FK |
| transferenciaAndamentoQueCriei | TransferenciaAndamento[] (Lista) | FK |
| transferenciaAndamentoQueAtualizei | TransferenciaAndamento[] (Lista) | FK |
| transferenciaAndamentoQueRemovi | TransferenciaAndamento[] (Lista) | FK |
| transferenciaAndamentoQueSouResponsavel | TransferenciaAndamento[] (Lista) |  |
| transferenciaAndamentoTarefaQueCriei | TransferenciaAndamentoTarefa[] (Lista) | FK |
| transferenciaAndamentoTarefaQueAtualizei | TransferenciaAndamentoTarefa[] (Lista) | FK |
| transferenciaAndamentoTarefaQueRemovi | TransferenciaAndamentoTarefa[] (Lista) | FK |
| task_queue | task_queue[] (Lista) |  |
| GeoEnderecoReferenciaqQueCriei | GeoLocalizacaoReferencia[] (Lista) | FK |
| GeoEnderecoReferenciaqQueRemovid | GeoLocalizacaoReferencia[] (Lista) | FK |
| GrupoPainelExternoQueCriei | GrupoPainelExterno[] (Lista) | FK |
| GrupoPainelExternoQueAtualizei | GrupoPainelExterno[] (Lista) | FK |
| GrupoPainelExternoQueRemovi | GrupoPainelExterno[] (Lista) | FK |
| GrupoPainelExternoPessoa | GrupoPainelExternoPessoa[] (Lista) |  |
| PainelExternoGrupoPainelExternoQueRemovi | PainelExternoGrupoPainelExterno[] (Lista) | FK |
| PainelExternoGrupoPainelExternoQueCriei | PainelExternoGrupoPainelExterno[] (Lista) | FK |
| PainelExternoQueCriei | PainelExterno[] (Lista) | FK |
| PainelExternoQueAtualizei | PainelExterno[] (Lista) | FK |
| PainelExternoQueRemovi | PainelExterno[] (Lista) | FK |
| LogGenerico | LogGenerico[] (Lista) |  |
| TarefaCronogramaQCriei | TarefaCronograma[] (Lista) | FK |
| TarefaCronogramaQRemovi | TarefaCronograma[] (Lista) | FK |
| ProjetoEtapaQCriei | ProjetoEtapa[] (Lista) | FK |
| ProjetoEtapaQRemovi | ProjetoEtapa[] (Lista) | FK |
| ProjetoEtapaQAtualizei | ProjetoEtapa[] (Lista) | FK |
| Nota | Nota[] (Lista) | FK |
| NotaEnderecamentoQSouEnderecado | NotaEnderecamento[] (Lista) | FK |
| NotaEnderecamentoQCriei | NotaEnderecamento[] (Lista) | FK |
| NotaEnderecamentoQRemovi | NotaEnderecamento[] (Lista) | FK |
| NotaEnderecamentoRespostaQCriei | NotaEnderecamentoResposta[] (Lista) | FK |
| NotaEnderecamentoRespostaQRemovi | NotaEnderecamentoResposta[] (Lista) | FK |
| NotaQCriei | Nota[] (Lista) | FK |
| NotaQRemovi | Nota[] (Lista) | FK |
| BlocoNotaQCriei | BlocoNota[] (Lista) | FK |
| BlocoNotaQRemovi | BlocoNota[] (Lista) | FK |
| BlocoNotaQAtualizei | BlocoNota[] (Lista) | FK |
| VariavelCategoricaQCriei | VariavelCategorica[] (Lista) | FK |
| VariavelCategoricaQRemovi | VariavelCategorica[] (Lista) | FK |
| VariavelCategoricaQAtualizei | VariavelCategorica[] (Lista) | FK |
| VariavelCategoricaValorQCriei | VariavelCategoricaValor[] (Lista) | FK |
| VariavelCategoricaValorQRemovi | VariavelCategoricaValor[] (Lista) | FK |
| VariavelCategoricaValorQAtualizei | VariavelCategoricaValor[] (Lista) | FK |
| GruposTematicosQueCriei | GrupoTematico[] (Lista) | FK |
| GruposTematicosQueRemovi | GrupoTematico[] (Lista) | FK |
| GruposTematicosQueAtualizei | GrupoTematico[] (Lista) | FK |
| TipoIntervencaoQueCriei | TipoIntervencao[] (Lista) | FK |
| TipoIntervencaoQueRemovi | TipoIntervencao[] (Lista) | FK |
| TipoIntervencaoQueAtualizei | TipoIntervencao[] (Lista) | FK |
| EmpreendimentosQueCriei | Empreendimento[] (Lista) | FK |
| EmpreendimentosQueDesativei | Empreendimento[] (Lista) | FK |
| EmpreendimentosQueAtualizei | Empreendimento[] (Lista) | FK |
| EquipamentosQueCriei | Equipamento[] (Lista) | FK |
| EquipamentosQueRemovi | Equipamento[] (Lista) | FK |
| EquipamentosQueAtualizei | Equipamento[] (Lista) | FK |
| StatusesDistribuicaoQueCriei | DistribuicaoStatus[] (Lista) | FK |
| StatusesDistribuicaoQueRemovi | DistribuicaoStatus[] (Lista) | FK |
| StatusesDistribuicaoQueAtualizei | DistribuicaoStatus[] (Lista) | FK |
| view_atividade_pessoa_responsavel | view_atividade_pessoa_responsavel[] (Lista) |  |
| view_iniciativa_pessoa_responsavel | view_iniciativa_pessoa_responsavel[] (Lista) |  |
| ViewNotaComOrdemQCriei | ViewNotas[] (Lista) | FK |
| ViewNotaComOrdemQRemovi | ViewNotas[] (Lista) | FK |
| ViewNotaComOrdemQSouResp | ViewNotas[] (Lista) | FK |
| PdmPerfilQueDesativei | PdmPerfil[] (Lista) | FK |
| PdmPerfilQueCriei | PdmPerfil[] (Lista) | FK |
| ProjetoRegiaoQCriei | ProjetoRegiao[] (Lista) | FK |
| ProjetoRegiaoQAtualizei | ProjetoRegiao[] (Lista) | FK |
| ProjetoRegiaoQRemovi | ProjetoRegiao[] (Lista) | FK |
| RegistroStatusDistribuicaoQueCriei | DistribuicaoRecursoStatus[] (Lista) | FK |
| RegistroStatusDistribuicaoQueRemovi | DistribuicaoRecursoStatus[] (Lista) | FK |
| RegistroStatusDistribuicaoQueAtualizei | DistribuicaoRecursoStatus[] (Lista) | FK |
| ProjetoTagQCriei | ProjetoTag[] (Lista) | FK |
| ProjetoTagQAtualizei | ProjetoTag[] (Lista) | FK |
| ProjetoTagQRemovi | ProjetoTag[] (Lista) | FK |
| TipoAditivoQCriei | TipoAditivo[] (Lista) | FK |
| TipoAditivoQAtualizei | TipoAditivo[] (Lista) | FK |
| TipoAditivoQRemovi | TipoAditivo[] (Lista) | FK |
| ModalidadeContratacaoQCriei | ModalidadeContratacao[] (Lista) | FK |
| ModalidadeContratacaoQAtualizei | ModalidadeContratacao[] (Lista) | FK |
| ModalidadeContratacaoQRemovi | ModalidadeContratacao[] (Lista) | FK |
| ProjetoProgramaQCriei | ProjetoPrograma[] (Lista) | FK |
| ProjetoProgramaQAtualizei | ProjetoPrograma[] (Lista) | FK |
| ProjetoProgramaQRemovi | ProjetoPrograma[] (Lista) | FK |
| ContratosQCriei | Contrato[] (Lista) | FK |
| ContratosQAtualizei | Contrato[] (Lista) | FK |
| ContratosQRemovi | Contrato[] (Lista) | FK |
| AditivosQCriei | ContratoAditivo[] (Lista) | FK |
| AditivosQAtualizei | ContratoAditivo[] (Lista) | FK |
| AditivosQRemovi | ContratoAditivo[] (Lista) | FK |
| RelacaoParlamentarTransferenciaQCriei | TransferenciaParlamentar[] (Lista) | FK |
| RelacaoParlamentarTransferenciaQAtualizei | TransferenciaParlamentar[] (Lista) | FK |
| RelacaoParlamentarTransferenciaQRemovi | TransferenciaParlamentar[] (Lista) | FK |
| RelacaoParlamentarDistribuicaoQCriei | DistribuicaoParlamentar[] (Lista) | FK |
| RelacaoParlamentarDistribuicaoQAtualizei | DistribuicaoParlamentar[] (Lista) | FK |
| RelacaoParlamentarDistribuicaoQRemovi | DistribuicaoParlamentar[] (Lista) | FK |
| AssuntoVariavelQCriei | AssuntoVariavel[] (Lista) | FK |
| AssuntoVariavelQAtualizei | AssuntoVariavel[] (Lista) | FK |
| AssuntoVariavelQRemovi | AssuntoVariavel[] (Lista) | FK |
| GrupoResponsavelEquipePessoa | GrupoResponsavelEquipeParticipante[] (Lista) |  |
| VariavelQCriei | Variavel[] (Lista) | FK |
| VariavelQAtualizei | Variavel[] (Lista) | FK |
| GrupoResponsavelEquipeColaborador | GrupoResponsavelEquipeResponsavel[] (Lista) |  |
| VariavelCicloAnaliseQCrei | VariavelGlobalCicloAnalise[] (Lista) | FK |
| VariavelCicloAnaliseQRemovi | VariavelGlobalCicloAnalise[] (Lista) | FK |
| VariavelCicloFisicoDocumentoQCrei | VariavelGlobalCicloDocumento[] (Lista) | FK |
| VariavelCicloFisicoDocumentoQRemovi | VariavelGlobalCicloDocumento[] (Lista) | FK |
| VarGlobPedidoComplementacaoCriador | VariavelGlobalPedidoComplementacao[] (Lista) | FK |
| VarGlobPedidoComplementacaoAtendeu | VariavelGlobalPedidoComplementacao[] (Lista) | FK |
| VarGlobPedidoComplementacaoRemovedor | VariavelGlobalPedidoComplementacao[] (Lista) | FK |
| ClassificacaoQCriei | Classificacao[] (Lista) | FK |
| ClassificacaoQAtualizei | Classificacao[] (Lista) | FK |
| ClassificacaoQRemovi | Classificacao[] (Lista) | FK |
| entradasLogTransferencias | TransferenciaHistorico[] (Lista) |  |
| projetosRevisao | ProjetoPessoaRevisao[] (Lista) |  |
| CategoriaAssuntoVariavelQCriei | CategoriaAssuntoVariavel[] (Lista) | FK |
| CategoriaAssuntoVariavelQAtualizei | CategoriaAssuntoVariavel[] (Lista) | FK |
| CategoriaAssuntoVariavelQRemovi | CategoriaAssuntoVariavel[] (Lista) | FK |
| AtualizacoesEmLoteCriadas | AtualizacaoEmLote[] (Lista) | FK |
| AtualizacoesEmLoteRemovidas | AtualizacaoEmLote[] (Lista) | FK |

---

### PessoaAcessoPdm (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int | Unique |
| metas_cronograma | Int[] (Lista) |  |
| metas_variaveis | Int[] (Lista) |  |
| variaveis | Int[] (Lista) |  |
| cronogramas_etapas | Int[] (Lista) |  |
| data_ciclo | DateTime? (Opcional) |  |
| perfil | String |  |
| pessoa | Relacionamento -> Pessoa | FK |

---

### PessoaAcessoPdmValido (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int | Unique |
| pessoa | Relacionamento -> Pessoa | FK |

---

### PessoaAtividadeLog (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| ip | String |  |
| pessoa_sessao_id | Int |  |
| pessoa_sessao | Relacionamento -> PessoaSessao | FK |
| criado_em | DateTime |  |

---

### PessoaFisica (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| cargo | String? (Opcional) |  |
| lotacao | String? (Opcional) |  |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| pessoa | Pessoa[] (Lista) |  |
| registro_funcionario | String? (Opcional) |  |
| cpf | String? (Opcional) |  |

---

### PessoaPerfil (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int |  |
| perfil_acesso_id | Int |  |
| perfil_acesso | Relacionamento -> PerfilAcesso | FK |
| pessoa | Relacionamento -> Pessoa | FK |

---

### PessoaSessao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| criado_em | DateTime |  |
| criado_ip | String |  |
| removido_em | DateTime? (Opcional) |  |
| removido_ip | String? (Opcional) |  |
| PessoaSessaoAtiva | PessoaSessaoAtiva[] (Lista) |  |
| PessoaAtividadeLog | PessoaAtividadeLog[] (Lista) |  |
| LogGenerico | LogGenerico[] (Lista) |  |

---

### PessoaSessaoAtiva (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| pessoa_sessao | Relacionamento -> PessoaSessao | FK |

---

### Privilegio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| codigo | String | Unique |
| modulo_id | Int |  |
| modulo | Relacionamento -> PrivilegioModulo | FK |
| perfil_privilegio | PerfilPrivilegio[] (Lista) |  |

---

### PrivilegioModulo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| codigo | String | Unique |
| descricao | String |  |
| privilegio | Privilegio[] (Lista) |  |
| modulo_sistema | ModuloSistema[] (Lista) |  |

---

### Relatorio (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pdm_id | Int? (Opcional) |  |
| parametros | Json |  |

---

### RelatorioFila (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| relatorio_id | Int |  |
| relatorio | Relacionamento -> Relatorio | FK |
| err_msg | String? (Opcional) |  |
| criado_em | DateTime |  |
| congelado_em | DateTime? (Opcional) |  |
| executado_em | DateTime? (Opcional) |  |

---

### SmaeConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| key | String | PK |
| value | String |  |
| criado_em | DateTime |  |

---

### TextoConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bemvindo_email | String |  |
| tos | String |  |

---

### TipoDocumento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| codigo | String |  |
| titulo | String |  |
| descricao | String? (Opcional) |  |
| extensoes | String? (Opcional) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| Arquivo | Arquivo[] (Lista) |  |

---

### TipoOrgao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| orgao | Orgao[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### WikiLink (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| chave_smae | String | Unique |
| url_wiki | String |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |

---

### feature_flag (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| panorama | Boolean |  |
| mf_v2 | Boolean |  |
| pp_pe | Boolean |  |
| ps_cp_readonly_pdm_config | Boolean |  |
| mostrar_pdm_antigo | Boolean |  |

---

## Geolocalização

**Origem/Funcionalidade:** Módulo Geolocalização (Backend: /geo-loc). Gestão de coordenadas, camadas geográficas e regiões.

### GeoCamada (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo_camada | String |  |
| codigo | String |  |
| titulo | String |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| geo_camada_config | Int |  |
| config | Relacionamento -> GeoCamadaConfig | FK |
| geom_geojson_original | Json |  |
| geom_geojson | Json |  |
| GeoCamadaRegiao | GeoCamadaRegiao[] (Lista) |  |
| GeoEnderecoCamada | GeoLocalizacaoCamada[] (Lista) |  |

---

### GeoCamadaConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo_camada | String |  |
| chave_camada | String |  |
| titulo_camada | String |  |
| descricao | String |  |
| nivel_regionalizacao | Int? (Opcional) |  |
| cor | String? (Opcional) |  |
| simplificar_em | Float? (Opcional) |  |
| GeoCamada | GeoCamada[] (Lista) |  |

---

### GeoCamadaRegiao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| regiao_id | Int |  |
| geo_camada_id | Int |  |
| geo_camada | Relacionamento -> GeoCamada | FK |
| regiao | Relacionamento -> Regiao | FK |

---

### GeoLocalizacao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | GeoReferenciaTipo |  |
| endereco_exibicao | String |  |
| geom_geojson | Json |  |
| metadata | Json |  |
| lat | Float |  |
| lon | Float |  |
| criado_em | DateTime |  |
| GeoEnderecoCamada | GeoLocalizacaoCamada[] (Lista) |  |
| GeoEnderecoReferencia | GeoLocalizacaoReferencia[] (Lista) |  |

---

### GeoLocalizacaoCamada (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| geo_localizacao_id | Int |  |
| geo_camada_id | Int |  |
| geo_localizacao | Relacionamento -> GeoLocalizacao | FK |
| geo_camada | Relacionamento -> GeoCamada | FK |

---

### GeoLocalizacaoReferencia (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| geo_localizacao_id | Int |  |
| criador_por | Int? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| tipo | GeoReferenciaTipo |  |
| projeto_id | Int? (Opcional) |  |
| iniciativa_id | Int? (Opcional) |  |
| atividade_id | Int? (Opcional) |  |
| meta_id | Int? (Opcional) |  |
| etapa_id | Int? (Opcional) |  |
| projeto | Projeto? (Opcional) | FK |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade | Atividade? (Opcional) | FK |
| meta | Meta? (Opcional) | FK |
| etapa | Etapa? (Opcional) | FK |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |
| geo_localizacao | Relacionamento -> GeoLocalizacao | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### ProjetoRegiao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| projeto_id | Int |  |
| projeto | Relacionamento -> Projeto | FK |
| regiao_id | Int |  |
| regiao | Relacionamento -> Regiao | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| removedor | Pessoa? (Opcional) | FK |

---

### Regiao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| descricao | String |  |
| shapefile | String? (Opcional) |  |
| nivel | Int |  |
| codigo | String? (Opcional) |  |
| parente_id | Int? (Opcional) |  |
| pdm_codigo_sufixo | String? (Opcional) |  |
| arquivo_shapefile_id | Int? (Opcional) |  |
| ArquivoShapefile | Arquivo? (Opcional) | FK |
| RegiaoAcima | Regiao? (Opcional) | FK |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| RegioesAbaixo | Regiao[] (Lista) | FK |
| Variavel | Variavel[] (Lista) |  |
| VariavelGlobalView | ViewVariavelGlobal[] (Lista) |  |
| Etapa | Etapa[] (Lista) |  |
| Projetos | Projeto[] (Lista) |  |
| GeoCamadaRegiao | GeoCamadaRegiao[] (Lista) |  |
| eleicoesComparecimento | EleicaoComparecimento[] (Lista) |  |
| mandatoRepresentatividade | MandatoRepresentatividade[] (Lista) |  |
| ProjetoRegiao | ProjetoRegiao[] (Lista) |  |
| FormulaComposta | FormulaComposta[] (Lista) |  |

---

## Sistema SEI

**Origem/Funcionalidade:** Integração SEI (Backend: /sei-api). Controle de status de processos no Sistema Eletrônico de Informações.

### StatusSEI (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| ativo | Boolean |  |
| processo_sei | String | Unique |
| link | String |  |
| status_code | Int? (Opcional) |  |
| resumo_status_code | Int? (Opcional) |  |
| json_resposta | Json? (Opcional) |  |

---

## Email

**Origem/Funcionalidade:** Serviço de Email (Backend: /aviso-email). Configuração e fila de envio de emails.

### AvisoEmail (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | TipoAviso |  |
| tarefa_cronograma_id | Int? (Opcional) |  |
| tarefa_id | Int? (Opcional) |  |
| nota_id | Int? (Opcional) |  |
| tarefa_cronograma | TarefaCronograma? (Opcional) | FK |
| tarefa | Tarefa? (Opcional) | FK |
| nota | Nota? (Opcional) | FK |
| com_copia | String[] (Lista) |  |
| numero | Int |  |
| numero_periodo | AvisoPeriodo |  |
| recorrencia_dias | Int |  |
| ativo | Boolean |  |
| executou_em | DateTime |  |
| executou_em_ts | DateTime |  |
| ultimo_envio_em | DateTime? (Opcional) |  |
| AvisoEmailDisparos | AvisoEmailDisparos[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| DistribuicaoRecurso | DistribuicaoRecurso[] (Lista) |  |

---

### AvisoEmailDisparos (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| para | String |  |
| com_copia | String[] (Lista) |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| aviso_email_id | Int |  |
| aviso_email | Relacionamento -> AvisoEmail | FK |
| emaildb_queue_id | String |  |
| emaildb_queue | Relacionamento -> EmaildbQueue | FK |

---

### EmaildbConfig (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| from | String |  |
| template_resolver_class | String |  |
| template_resolver_config | Json |  |

---

### EmaildbQueue (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | String | PK |
| config_id | Int |  |
| created_at | DateTime |  |
| template | String |  |
| to | String |  |
| subject | String |  |
| variables | Json |  |
| sent | Boolean? (Opcional) |  |
| updated_at | DateTime? (Opcional) |  |
| visible_after | DateTime? (Opcional) |  |
| errmsg | String? (Opcional) |  |
| emaildb_config | Relacionamento -> EmaildbConfig | FK |
| AvisoEmailDisparos | AvisoEmailDisparos[] (Lista) |  |

---

## Painéis

**Origem/Funcionalidade:** Módulo de Painéis (Frontend: /paineis). Configuração de dashboards e painéis de visualização.

### GrupoPainel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String | Unique |
| ativo | Boolean |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| pessoas | PessoaGrupoPainel[] (Lista) |  |
| paineis | PainelGrupoPainel[] (Lista) |  |

---

### GrupoPainelExterno (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| modulo_sistema | ModuloSistema |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| orgao_id | Int |  |
| orgao | Relacionamento -> Orgao | FK |
| GrupoPainelExternoPessoa | GrupoPainelExternoPessoa[] (Lista) |  |
| PainelExternoGrupoPainelExterno | PainelExternoGrupoPainelExterno[] (Lista) |  |

---

### GrupoPainelExternoPessoa (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| grupo_painel_externo_id | Int |  |
| orgao_id | Int |  |
| pessoa_id | Int |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| grupo_painel_externo | Relacionamento -> GrupoPainelExterno | FK |
| pessoa | Relacionamento -> Pessoa | FK |
| orgao | Relacionamento -> Orgao | FK |

---

### MetabasePermissao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| permissao | String |  |
| configuracao | Json |  |

---

### Painel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nome | String |  |
| periodicidade | Periodicidade |  |
| ativo | Boolean |  |
| pdm_id | Int |  |
| pdm | Relacionamento -> Pdm | FK |
| mostrar_planejado_por_padrao | Boolean |  |
| mostrar_acumulado_por_padrao | Boolean |  |
| mostrar_indicador_por_padrao | Boolean |  |
| criado_por | Int? (Opcional) |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| atualizador | Pessoa? (Opcional) | FK |
| criador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| painel_conteudo | PainelConteudo[] (Lista) |  |
| grupos | PainelGrupoPainel[] (Lista) |  |

---

### PainelConteudo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| painel_id | Int |  |
| painel | Relacionamento -> Painel | FK |
| meta_id | Int |  |
| meta | Relacionamento -> Meta | FK |
| periodicidade | Periodicidade |  |
| periodo | Periodo |  |
| periodo_valor | Int? (Opcional) |  |
| periodo_inicio | DateTime? (Opcional) |  |
| periodo_fim | DateTime? (Opcional) |  |
| mostrar_planejado | Boolean |  |
| mostrar_acumulado | Boolean |  |
| mostrar_indicador | Boolean |  |
| mostrar_acumulado_periodo | Boolean |  |
| ordem | Int? (Opcional) |  |
| detalhes | PainelConteudoDetalhe[] (Lista) |  |
| indicador | Indicador? (Opcional) | FK |
| indicador_id | Int? (Opcional) |  |

---

### PainelConteudoDetalhe (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| variavel_id | Int? (Opcional) |  |
| variavel | Variavel? (Opcional) | FK |
| iniciativa_id | Int? (Opcional) |  |
| iniciativa | Iniciativa? (Opcional) | FK |
| atividade_id | Int? (Opcional) |  |
| atividade | Atividade? (Opcional) | FK |
| painel_conteudo_id | Int |  |
| painel_conteudo | Relacionamento -> PainelConteudo | FK |
| pai_id | Int? (Opcional) |  |
| pai | PainelConteudoDetalhe? (Opcional) | FK |
| mostrar_indicador | Boolean |  |
| ordem | Int? (Opcional) |  |
| tipo | PainelConteudoTipoDetalhe |  |
| filhos | PainelConteudoDetalhe[] (Lista) | FK |

---

### PainelExterno (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| titulo | String |  |
| descricao | String? (Opcional) |  |
| modulo_sistema | ModuloSistema |  |
| link | String |  |
| link_dominio | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| PainelExternoGrupoPainelExterno | PainelExternoGrupoPainelExterno[] (Lista) |  |

---

### PainelExternoGrupoPainelExterno (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| painel_externo_id | Int |  |
| grupo_painel_externo_id | Int |  |
| PainelExterno | Relacionamento -> PainelExterno | FK |
| GrupoPainelExterno | Relacionamento -> GrupoPainelExterno | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### PainelGrupoPainel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| painel_id | Int |  |
| painel | Relacionamento -> Painel | FK |
| grupo_painel_id | Int |  |
| grupo_painel | Relacionamento -> GrupoPainel | FK |

---

### PessoaGrupoPainel (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| pessoa_id | Int |  |
| pessoa | Relacionamento -> Pessoa | FK |
| grupo_painel_id | Int |  |
| grupo_painel | Relacionamento -> GrupoPainel | FK |

---

## Notas / Comunicação

**Origem/Funcionalidade:** Módulo de Notas (Backend: /bloco-nota). Sistema de comunicação interna e notas.

### BlocoNota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bloco | String |  |
| Nota | Nota[] (Lista) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| atualizado_por | Int? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| criador | Relacionamento -> Pessoa | FK |
| atualizador | Pessoa? (Opcional) | FK |
| removedor | Pessoa? (Opcional) | FK |
| ViewNotaComOrdem | ViewNotas[] (Lista) |  |
| ViewNotasTransferencias | ViewNotasTransferencias[] (Lista) |  |

---

### Nota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bloco_nota_id | Int |  |
| tipo_nota_id | Int |  |
| data_nota | DateTime |  |
| orgao_responsavel_id | Int? (Opcional) |  |
| pessoa_responsavel_id | Int |  |
| nota | String |  |
| titulo | String? (Opcional) |  |
| dados | Json? (Opcional) |  |
| rever_em | DateTime? (Opcional) |  |
| dispara_email | Boolean |  |
| status | StatusNota |  |
| usuarios_lidos | Int[] (Lista) |  |
| n_enderecamentos | Int |  |
| n_repostas | Int |  |
| ultima_resposta | DateTime? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| tipo_nota | Relacionamento -> TipoNota | FK |
| bloco_nota | Relacionamento -> BlocoNota | FK |
| orgao_responsavel | Orgao? (Opcional) | FK |
| pessoa_responsavel | Relacionamento -> Pessoa | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |
| NotaEnderecamento | NotaEnderecamento[] (Lista) |  |
| NotaEnderecamentoResposta | NotaEnderecamentoResposta[] (Lista) |  |
| revisoes | NotaRevisao[] (Lista) |  |
| AvisoEmail | AvisoEmail[] (Lista) |  |
| ViewNotasTransferencias | ViewNotasTransferencias[] (Lista) |  |
| DistribuicaoRecurso | DistribuicaoRecurso[] (Lista) |  |

---

### NotaEnderecamento (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nota_id | Int |  |
| orgao_enderecado_id | Int |  |
| pessoa_enderecado_id | Int? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| nota | Relacionamento -> Nota | FK |
| orgao_enderecado | Orgao? (Opcional) | FK |
| pessoa_enderecado | Pessoa? (Opcional) | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |
| NotaEnderecamentoResposta | NotaEnderecamentoResposta[] (Lista) |  |

---

### NotaEnderecamentoResposta (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nota_id | Int |  |
| nota_enderecamento_id | Int |  |
| resposta | String |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| nota | Relacionamento -> Nota | FK |
| nota_enderecamento | Relacionamento -> NotaEnderecamento | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

### NotaRevisao (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| nota_id | Int |  |
| nota | String |  |
| nota_fk | Relacionamento -> Nota | FK |
| criado_por | Int |  |
| criado_em | DateTime |  |

---

### TipoNota (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| codigo | String | Unique |
| permite_revisao | Boolean |  |
| permite_enderecamento | Boolean |  |
| permite_email | Boolean |  |
| permite_replica | Boolean |  |
| visivel_resp_orgao | Boolean |  |
| eh_publico | Boolean |  |
| autogerenciavel | Boolean |  |
| TipoNotaModulo | TipoNotaModulo[] (Lista) |  |
| Nota | Nota[] (Lista) |  |
| criado_em | DateTime |  |
| removido_em | DateTime? (Opcional) |  |
| atualizado_em | DateTime? (Opcional) |  |
| ViewNotaComOrdem | ViewNotas[] (Lista) |  |

---

### TipoNotaModulo (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| modulo_sistema | ModuloSistema |  |
| tipo_nota_id | Int |  |
| tipo_nota | Relacionamento -> TipoNota | FK |

---

### ViewNotas (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| bloco_nota_id | Int |  |
| tipo_nota_id | Int |  |
| data_nota | DateTime |  |
| orgao_responsavel_id | Int |  |
| pessoa_responsavel_id | Int |  |
| nota | String |  |
| rever_em | DateTime? (Opcional) |  |
| dispara_email | Boolean |  |
| status | StatusNota |  |
| n_enderecamentos | Int |  |
| n_repostas | Int |  |
| ultima_resposta | DateTime? (Opcional) |  |
| criado_por | Int |  |
| criado_em | DateTime |  |
| removido_por | Int? (Opcional) |  |
| removido_em | DateTime? (Opcional) |  |
| data_ordenacao | DateTime |  |
| tipo_nota | Relacionamento -> TipoNota | FK |
| bloco_nota | Relacionamento -> BlocoNota | FK |
| orgao_responsavel | Relacionamento -> Orgao | FK |
| pessoa_responsavel | Relacionamento -> Pessoa | FK |
| criador | Relacionamento -> Pessoa | FK |
| removedor | Pessoa? (Opcional) | FK |

---

## Tarefas de Sistema (Background Tasks)

**Origem/Funcionalidade:** Sistema de Tarefas em Segundo Plano. Tabelas técnicas para controle de jobs assíncronos e logs.

### ApiRequestLogControl (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| log_date | DateTime | PK |
| status | ApiRequestLogControlStatus |  |
| task_id | Int? (Opcional) |  |
| backup_location | String? (Opcional) |  |
| last_error | String? (Opcional) |  |
| created_at | DateTime |  |
| updated_at | DateTime |  |
| task | task_queue? (Opcional) | FK |

---

### AtualizacaoEmLote (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| tipo | TipoAtualizacaoEmLote |  |
| status | StatusAtualizacaoEmLote |  |
| target_ids | Int[] (Lista) |  |
| operacao | Json |  |

---

### api_request_log (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| created_at | DateTime |  |
| cf_ray | String |  |
| request_num | Int |  |
| ip | String |  |
| response_time | Int |  |
| response_size | Int |  |
| req_method | String |  |
| req_path | String |  |
| req_host | String |  |
| req_headers | String? (Opcional) |  |
| req_query | String? (Opcional) |  |
| req_body | String? (Opcional) |  |
| req_body_size | Int? (Opcional) |  |
| res_code | Int |  |
| created_pessoa_id | Int? (Opcional) |  |

---

### task_buffer (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| task_id | Int |  |
| task | Relacionamento -> task_queue | FK |
| data | Json |  |

---

### task_queue (Tabela)

| Coluna | Tipo | Detalhes |
|---|---|---|
| id | Int | PK |
| type | task_type |  |
| status | task_status |  |
| params | Json |  |

---

### view_api_request_log (View (Visualização))

| Coluna | Tipo | Detalhes |
|---|---|---|
| created_at | DateTime |  |
| cf_ray | String |  |
| request_num | Int |  |
| request_date | DateTime |  |
| req_path_clean | String |  |
| ip | String |  |
| response_time | Int |  |
| response_size | Int |  |
| req_method | String |  |
| req_path | String |  |
| req_host | String |  |
| req_headers | String? (Opcional) |  |
| req_query | String? (Opcional) |  |
| req_body | String? (Opcional) |  |
| req_body_size | Int? (Opcional) |  |
| res_code | Int |  |
| created_pessoa_id | Int? (Opcional) |  |

---
