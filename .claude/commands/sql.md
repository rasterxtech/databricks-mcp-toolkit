---
description: Executa uma query SQL no Databricks e analisa os resultados
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__list_tables
---

O usuário quer executar uma query SQL no Databricks.

## Instruções

1. Se o usuário forneceu uma query SQL completa, execute-a diretamente com `mcp__databricks__run_sql`
2. Se o usuário descreveu o que quer em linguagem natural, primeiro entenda as tabelas envolvidas usando `describe_table`, depois construa e execute a query SQL
3. Apresente os resultados formatados em tabela markdown
4. Se relevante, adicione observações sobre os dados retornados (tendências, outliers, totais)

## Entrada do usuário

$ARGUMENTS
