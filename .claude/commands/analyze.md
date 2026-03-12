---
description: Análise exploratória completa de uma tabela Databricks
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, mcp__databricks__list_tables, mcp__databricks__list_schemas
---

O usuário quer uma análise exploratória de dados (EDA) de uma tabela no Databricks.

## Instruções

Execute a análise na seguinte ordem:

1. **Schema**: Use `describe_table` para listar colunas, tipos e comentários
2. **Estatísticas**: Use `table_stats` para contagem, nulos e cardinalidade
3. **Amostra**: Use `sample_table` para visualizar registros reais
4. **Distribuições**: Execute queries SQL para:
   - Distribuição de valores em colunas categóricas (GROUP BY + COUNT)
   - MIN, MAX, AVG, STDDEV em colunas numéricas
   - Distribuição temporal se houver colunas de data
5. **Data Quality**: Verifique:
   - Percentual de nulos por coluna
   - Possíveis duplicatas
   - Valores fora do esperado

## Formato de saída

Apresente os resultados organizados com headers markdown claros.
Inclua uma seção final "Observações" com insights encontrados.

## Entrada do usuário

$ARGUMENTS
