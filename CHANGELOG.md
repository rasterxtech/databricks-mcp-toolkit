# Changelog

Todas as alterações relevantes deste projeto são documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.2.0] - 2026-03-13

### Novidades

- feat: substitui diagrama Mermaid por SVG visual
- feat: traduz MCP server para inglês
- feat: traduz skills para inglês
- feat: traduz agentes para inglês
- feat: adiciona post-release.sh para publicar GitHub Releases
- feat: script de release automatizado com changelog e PR
- feat: instaladores salvam versão e configuram auto-update
- feat: sistema de auto-update com verificação em background
- feat: adiciona instalador remoto via curl | bash
- feat: credenciais globais e instalação global/por-projeto
- feat: adiciona agente data-scientist e 5 novas skills
- feat: adiciona 9 ferramentas MCP para MLflow e Model Registry

### Correções

- fix: corrige acentos faltantes no README e docs/
- fix: adiciona checagem de python3-venv e git nos instaladores
- fix: corrige caracteres Unicode escapados no README
- fix: carrega .env automaticamente via python-dotenv

### Documentação

- docs: reescreve README como landing page com links para docs/
- docs: cria pasta docs/ com documentação detalhada
- docs: adiciona convenções de desenvolvimento ao CLAUDE.md
- docs: atualiza README com fluxo de post-release
- docs: reescreve changelog v0.1.0 como anúncio de lançamento
- docs: adiciona seção de versionamento e releases ao README
- docs: documenta sistema de atualização automática
- docs: adiciona python3-venv aos pré-requisitos e troubleshooting
- docs: atualiza README com instalação via curl | bash
- docs: atualiza CLAUDE.md e README para novo fluxo de instalação
- docs: atualiza install.sh, CLAUDE.md e README com novo agente e ferramentas
- docs: ajustes de formatação e URL do repositório no README
- docs: reescreve README com foco comercial e estrutura de produto
- docs: consolida variáveis do .env e documenta WAREHOUSE_ID

### Outros

- Merge pull request #1 from rasterxdev/develop
- refactor: move scripts para scripts/ e atualiza referências

**Diff completo:** [9ef5bd02feffa63da46730ca79498f134bb4a0fa...v0.2.0](https://github.com/rasterxdev/databricks-mcp-toolkit/compare/9ef5bd02feffa63da46730ca79498f134bb4a0fa...v0.2.0)

Todas as alterações relevantes deste projeto são documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2026-03-13

Release inicial do Databricks MCP Toolkit.

### Novidades

- MCP Server com 18 ferramentas para interação com Databricks (SQL, Unity Catalog, MLflow, Model Registry, Serving Endpoints)
- Agente **databricks-analyst** para exploração de dados, SQL e criação de notebooks PySpark
- Agente **data-scientist** para ML lifecycle, análise estatística, feature engineering e séries temporais
- 9 skills: `/sql`, `/analyze`, `/notebook`, `/explore`, `/predict`, `/stats`, `/timeseries`, `/model`, `/feature`
- Instalação remota via `curl | bash` (sem clonar o repositório)
- Instalação global ou por projeto com detecção automática de SQL Warehouse
- Sistema de auto-update com verificação em background e notificação na sessão
- Gerenciamento de credenciais com prioridade: `.env` do projeto > config global > perfil CLI

**Diff completo:** [v0.1.0](https://github.com/rasterxdev/databricks-mcp-toolkit/releases/tag/v0.1.0)
