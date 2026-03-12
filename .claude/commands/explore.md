---
description: Explora catálogos, schemas e tabelas do Unity Catalog
allowed-tools: mcp__databricks__list_catalogs, mcp__databricks__list_schemas, mcp__databricks__list_tables, mcp__databricks__describe_table
---

O usuário quer explorar o Unity Catalog do Databricks.

## Instruções

1. Se nenhum argumento foi fornecido, comece listando os catálogos com `list_catalogs`
2. Se um catálogo foi especificado, liste os schemas dele com `list_schemas`
3. Se catalog.schema foi especificado, liste as tabelas com `list_tables`
4. Se uma tabela completa foi especificada, descreva-a com `describe_table`

Apresente os resultados formatados e sugira próximos passos de exploração.

## Entrada do usuário

$ARGUMENTS
