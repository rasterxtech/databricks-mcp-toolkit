---
description: Executa testes estatisticos e analises avancadas via SQL no Databricks
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, mcp__databricks__list_tables
---

O usuario quer uma analise estatistica avancada de dados no Databricks.

## Instrucoes

### 1. Entender os dados
- Use `describe_table` para entender colunas e tipos
- Use `table_stats` para visao geral
- Identifique colunas numericas e categoricas relevantes

### 2. Executar analises via SQL

Dependendo do pedido do usuario, execute uma ou mais das analises abaixo usando `run_sql`:

#### Estatisticas descritivas avancadas
```sql
SELECT
  COUNT(*) as n,
  AVG(coluna) as media,
  STDDEV(coluna) as desvio_padrao,
  VARIANCE(coluna) as variancia,
  SKEWNESS(coluna) as assimetria,
  KURTOSIS(coluna) as curtose,
  MIN(coluna) as minimo,
  PERCENTILE(coluna, 0.25) as q1,
  PERCENTILE(coluna, 0.50) as mediana,
  PERCENTILE(coluna, 0.75) as q3,
  MAX(coluna) as maximo
FROM tabela
```

#### Correlacao entre variaveis
```sql
SELECT
  CORR(col_a, col_b) as correlacao
FROM tabela
```

#### Deteccao de outliers (IQR)
```sql
WITH stats AS (
  SELECT
    PERCENTILE(coluna, 0.25) as q1,
    PERCENTILE(coluna, 0.75) as q3
  FROM tabela
)
SELECT COUNT(*) as outliers
FROM tabela, stats
WHERE coluna < q1 - 1.5 * (q3 - q1)
   OR coluna > q3 + 1.5 * (q3 - q1)
```

#### Distribuicao de frequencia
```sql
SELECT
  coluna,
  COUNT(*) as frequencia,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as percentual
FROM tabela
GROUP BY coluna
ORDER BY frequencia DESC
```

#### Teste de normalidade aproximado
- Use skewness e kurtosis para avaliar normalidade
- Skewness proximo de 0 e kurtosis proximo de 3 indicam distribuicao normal

### 3. Formato de saida

- Apresente resultados organizados com headers markdown
- Interprete os resultados estatisticamente (o que significam os numeros)
- Inclua recomendacoes baseadas nos achados
- Se relevante, sugira proximos passos de analise

## Entrada do usuario

$ARGUMENTS
