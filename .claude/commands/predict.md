---
description: Cria notebook com pipeline ML completo (EDA, features, treino, avaliacao, MLflow)
allowed-tools: mcp__databricks__run_sql, mcp__databricks__describe_table, mcp__databricks__sample_table, mcp__databricks__table_stats, mcp__databricks__list_tables, mcp__databricks__list_schemas, mcp__databricks__list_experiments, mcp__databricks__get_experiment_runs
---

O usuario quer criar um pipeline de Machine Learning completo como notebook Databricks.

## Instrucoes

### 1. Entender o problema
- Identifique a tabela de dados, a variavel alvo (target) e o tipo de problema (classificacao ou regressao)
- Se o usuario nao especificou a tabela, pergunte
- Use `describe_table` e `sample_table` para entender os dados

### 2. Gerar notebook com pipeline completo

Crie um arquivo `.py` no formato notebook Databricks com as seguintes celulas:

#### Celula 1: Setup e imports
```python
# Databricks notebook source
import mlflow
import mlflow.sklearn
from pyspark.sql import functions as F
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import pandas as pd
import numpy as np
```

#### Celula 2: Carregamento de dados
- Leia a tabela com Spark
- Mostre schema e contagem

#### Celula 3: EDA (Analise Exploratoria)
- Estatisticas descritivas
- Distribuicao da variavel alvo
- Verificacao de nulos e balanceamento

#### Celula 4: Feature Engineering
- Tratamento de nulos
- Encoding de categoricas
- Scaling de numericas
- Selecao de features

#### Celula 5: Split treino/teste
- Split estratificado (se classificacao)
- Proporcao 80/20 ou temporal se dados tem componente de tempo

#### Celula 6: Treinamento com MLflow
- Configurar experimento MLflow
- Treinar modelo(s) com logging de parametros e metricas
- Usar `mlflow.autolog()` ou logging manual

#### Celula 7: Avaliacao
- Metricas no conjunto de teste
- Matriz de confusao (classificacao) ou scatter plot (regressao)
- Feature importance

#### Celula 8: Registro do modelo (opcional)
- Registrar no Unity Catalog Model Registry se o resultado for satisfatorio

### 3. Formato do notebook

- Use `# COMMAND ----------` entre celulas
- Use `# MAGIC %md` para celulas de documentacao
- Documente cada etapa com markdown cells
- Inclua `display()` para visualizacoes no Databricks

## Entrada do usuario

$ARGUMENTS
