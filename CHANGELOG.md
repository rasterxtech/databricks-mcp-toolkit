# Changelog

Todas as alterações relevantes deste projeto são documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2026-03-13

### Novidades

- feat: instaladores salvam versão e configuram auto-update
- feat: sistema de auto-update com verificação em background
- feat: adiciona instalador remoto via curl | bash
- feat: credenciais globais e instalação global/por-projeto
- feat: adiciona agente data-scientist e 5 novas skills
- feat: adiciona 9 ferramentas MCP para MLflow e Model Registry

### Correções

- fix: adiciona checagem de python3-venv e git nos instaladores
- fix: corrige caracteres Unicode escapados no README
- fix: carrega .env automaticamente via python-dotenv

### Documentação

- docs: documenta sistema de atualização automática
- docs: adiciona python3-venv aos pré-requisitos e troubleshooting
- docs: atualiza README com instalação via curl | bash
- docs: atualiza CLAUDE.md e README para novo fluxo de instalação
- docs: atualiza install.sh, CLAUDE.md e README com novo agente e ferramentas
- docs: consolida variáveis do .env e documenta WAREHOUSE_ID
- docs: reescreve README com foco comercial e estrutura de produto
- docs: ajustes de formatação e URL do repositório no README

### Outros

- Initial commit: Databricks MCP Toolkit

**Diff completo:** [v0.1.0](https://github.com/rasterxdev/databricks-mcp-toolkit/releases/tag/v0.1.0)
