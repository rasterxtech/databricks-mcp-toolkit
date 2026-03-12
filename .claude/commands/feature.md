---
description: Analise de features e geracao de pipelines de feature engineering
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, mcp__databricks__list_tables, mcp__databricks__list_schemas
---

O usuario quer analisar features de uma tabela ou gerar um pipeline de feature engineering.

## Instrucoes

### 1. Entender os dados
- Use `describe_table` para listar colunas e tipos
- Use `table_stats` para cardinalidade e nulos
- Use `sample_table` para ver dados reais
- Identifique a variavel alvo se informada

### 2. Analise de features via SQL

Execute as seguintes analises com `run_sql`:

#### Tipagem e cardinalidade
- Classifique cada coluna: numerica continua, numerica discreta, categorica, temporal, texto
- Avalie cardinalidade para decidir estrategia de encoding

#### Correlacao com target (se informado)
```sql
SELECT CORR(feature_numerica, target) as correlacao
FROM tabela
```

#### Distribuicao de categoricas
```sql
SELECT coluna, COUNT(*) as freq,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) as pct
FROM tabela
GROUP BY coluna
ORDER BY freq DESC
LIMIT 20
```

#### Analise de nulos
```sql
SELECT
  COUNT(*) as total,
  SUM(CASE WHEN col IS NULL THEN 1 ELSE 0 END) as nulos,
  ROUND(SUM(CASE WHEN col IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as pct_nulos
FROM tabela
```

#### Power de cada feature (Information Value aproximado)
- Para cada feature, calcule a separacao entre classes do target
- Identifique features com maior poder preditivo

### 3. Recomendar transformacoes

Com base na analise, recomende:

- **Numericas**: scaling (StandardScaler, MinMaxScaler), log transform para skewed, binning
- **Categoricas**: one-hot (baixa cardinalidade), target encoding (alta cardinalidade), frequency encoding
- **Temporais**: extrair ano, mes, dia, dia da semana, trimestre, feriados
- **Window features**: medias moveis, lags, diffs, rolling min/max/std
- **Interacoes**: ratios entre features, multiplicacoes, features polinomiais
- **Nulos**: imputacao por media/mediana/moda, flag de missing

### 4. Gerar notebook de feature engineering (se solicitado)

Crie um notebook `.py` no formato Databricks com:

- **Celula 1**: Imports e carregamento dos dados
- **Celula 2**: Analise exploratoria das features
- **Celula 3**: Tratamento de nulos
- **Celula 4**: Encoding de categoricas
- **Celula 5**: Transformacoes numericas
- **Celula 6**: Features temporais e window features
- **Celula 7**: Selecao de features (correlation filter, variance threshold)
- **Celula 8**: Salvar dataset de features como tabela Delta

### 5. Formato de saida

- Apresente analise organizada por tipo de feature
- Classifique features por relevancia (se target informado)
- Liste transformacoes recomendadas em formato de tabela
- Se gerar notebook, use formato Databricks

## Entrada do usuario

$ARGUMENTS
