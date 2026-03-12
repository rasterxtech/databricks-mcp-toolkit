---
description: Analise de series temporais e geracao de notebook de forecasting
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, mcp__databricks__list_tables, mcp__databricks__list_experiments
---

O usuario quer analisar uma serie temporal ou criar um notebook de forecasting.

## Instrucoes

### 1. Entender os dados temporais
- Use `describe_table` para identificar colunas de data e metricas
- Use `sample_table` para ver o formato dos dados
- Identifique a granularidade temporal (diaria, semanal, mensal)

### 2. Analise exploratoria temporal via SQL

Execute as seguintes analises com `run_sql`:

#### Periodo e cobertura
```sql
SELECT
  MIN(data_col) as inicio,
  MAX(data_col) as fim,
  COUNT(*) as registros,
  COUNT(DISTINCT data_col) as periodos_unicos
FROM tabela
```

#### Tendencia (medias moveis)
```sql
SELECT
  data_col,
  valor,
  AVG(valor) OVER (ORDER BY data_col ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as mm3,
  AVG(valor) OVER (ORDER BY data_col ROWS BETWEEN 11 PRECEDING AND CURRENT ROW) as mm12
FROM tabela
ORDER BY data_col
```

#### Sazonalidade
```sql
SELECT
  MONTH(data_col) as mes,
  AVG(valor) as media,
  STDDEV(valor) as desvio
FROM tabela
GROUP BY MONTH(data_col)
ORDER BY mes
```

#### Variacao periodo a periodo
```sql
SELECT
  data_col,
  valor,
  LAG(valor) OVER (ORDER BY data_col) as valor_anterior,
  valor - LAG(valor) OVER (ORDER BY data_col) as variacao,
  ROUND((valor - LAG(valor) OVER (ORDER BY data_col)) / LAG(valor) OVER (ORDER BY data_col) * 100, 2) as var_pct
FROM tabela
ORDER BY data_col
```

#### Deteccao de anomalias temporais
```sql
WITH stats AS (
  SELECT AVG(valor) as media, STDDEV(valor) as desvio
  FROM tabela
)
SELECT t.*, (t.valor - s.media) / s.desvio as z_score
FROM tabela t, stats s
WHERE ABS((t.valor - s.media) / s.desvio) > 2
ORDER BY t.data_col
```

### 3. Gerar notebook de forecasting (se solicitado)

Crie um notebook `.py` no formato Databricks com:

- **Celula 1**: Imports (pandas, prophet ou statsmodels, mlflow, matplotlib)
- **Celula 2**: Carregamento e preparacao dos dados
- **Celula 3**: Visualizacao da serie (tendencia, sazonalidade)
- **Celula 4**: Decomposicao (trend, seasonal, residual)
- **Celula 5**: Modelo de forecasting com logging no MLflow
- **Celula 6**: Previsoes e intervalos de confianca
- **Celula 7**: Metricas de avaliacao (RMSE, MAE, MAPE)

### 4. Formato de saida

- Apresente os achados sobre tendencia, sazonalidade e anomalias
- Interprete os padroes encontrados
- Se gerar notebook, salve como `.py` com formato Databricks

## Entrada do usuario

$ARGUMENTS
