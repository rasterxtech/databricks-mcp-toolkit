---
description: Gerencia e inspeciona experimentos, runs, modelos e endpoints MLflow
allowed-tools: mcp__databricks__list_experiments, mcp__databricks__get_experiment_runs, mcp__databricks__get_run_details, mcp__databricks__compare_runs, mcp__databricks__get_metric_history, mcp__databricks__list_registered_models, mcp__databricks__get_model_versions, mcp__databricks__list_serving_endpoints, mcp__databricks__get_serving_endpoint, mcp__databricks__run_sql
---

O usuario quer inspecionar ou gerenciar recursos de ML no Databricks (MLflow experiments, runs, modelos, endpoints).

## Instrucoes

Interprete o comando do usuario e execute a acao apropriada:

### Listar experimentos
- Use `list_experiments` para mostrar experimentos disponiveis
- Exemplo: `/model list experiments`

### Explorar runs de um experimento
- Use `get_experiment_runs` com o ID do experimento
- Mostre metricas e parametros resumidos
- Exemplo: `/model runs <experiment_id>`

### Detalhes de um run
- Use `get_run_details` para ver parametros, metricas, tags e artifacts
- Exemplo: `/model run <run_id>`

### Comparar runs
- Use `compare_runs` com IDs separados por virgula
- Destaque o melhor modelo baseado nas metricas
- Exemplo: `/model compare <run_id1>,<run_id2>`

### Historico de metrica
- Use `get_metric_history` para ver evolucao de uma metrica
- Analise convergencia e overfitting
- Exemplo: `/model history <run_id> loss`

### Listar modelos registrados
- Use `list_registered_models` para ver modelos no Registry
- Exemplo: `/model list models`

### Versoes de um modelo
- Use `get_model_versions` para ver versoes de um modelo especifico
- Exemplo: `/model versions <catalog.schema.model_name>`

### Serving endpoints
- Use `list_serving_endpoints` para listar endpoints
- Use `get_serving_endpoint` para detalhes de um endpoint especifico
- Exemplo: `/model endpoints` ou `/model endpoint <nome>`

## Formato de saida

- Formate resultados em tabelas markdown
- Ao comparar runs, destaque o melhor resultado
- Ao analisar historico de metricas, comente sobre convergencia
- Sugira proximos passos quando relevante

## Entrada do usuario

$ARGUMENTS
