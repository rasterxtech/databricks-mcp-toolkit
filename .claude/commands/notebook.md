---
description: Cria um notebook Python/PySpark no formato Databricks
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, Read, Write, Edit
---

O usuário quer criar um notebook Python ou PySpark no formato Databricks.

## Instruções

1. Se o usuário referenciou tabelas, use `describe_table` para entender os schemas
2. Crie o notebook como arquivo `.py` usando o formato Databricks:
   - Primeira linha: `# Databricks notebook source`
   - Separador de células: `# COMMAND ----------`
3. Estruture o notebook com:
   - Célula de imports e configuração
   - Célula de documentação (markdown com `# MAGIC %md`)
   - Células de lógica com comentários explicativos
   - Célula de validação/verificação ao final
4. Salve o arquivo no diretório do projeto

## Padrões de código

- Use `spark.read.table("catalog.schema.table")` para ler tabelas
- Prefira DataFrame API para transformações complexas
- Use `display()` para mostrar resultados
- Adicione `# MAGIC %md` para células markdown de documentação
- Trate erros com try/except onde necessário

## Entrada do usuário

$ARGUMENTS
