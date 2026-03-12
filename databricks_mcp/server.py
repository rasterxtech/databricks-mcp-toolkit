"""
MCP Server para Databricks.

Fornece ferramentas para executar SQL, explorar catálogos,
descrever tabelas e interagir com o workspace Databricks.

Uso:
    python databricks_mcp/server.py
"""

import os
from functools import lru_cache
from textwrap import dedent

from databricks.sdk import WorkspaceClient
from mcp.server.fastmcp import FastMCP

# ── Inicialização ────────────────────────────────────────────────────────────

mcp = FastMCP(
    "Databricks",
    instructions=dedent("""
        Servidor MCP para interação com Databricks.
        Permite executar SQL, explorar catálogos/schemas/tabelas,
        e gerenciar recursos do workspace.
    """).strip(),
)


@lru_cache(maxsize=1)
def _get_client() -> WorkspaceClient:
    """Cria um WorkspaceClient (cacheado) usando variáveis de ambiente ou ~/.databrickscfg."""
    host = os.environ.get("DATABRICKS_HOST")
    token = os.environ.get("DATABRICKS_TOKEN")
    if host and token:
        return WorkspaceClient(host=host, token=token)
    # fallback para perfil do CLI
    return WorkspaceClient(profile="vscode_databricks")


@lru_cache(maxsize=1)
def _get_warehouse_id() -> str:
    """Retorna o warehouse_id configurado ou o primeiro disponível (cacheado)."""
    wh_id = os.environ.get("DATABRICKS_WAREHOUSE_ID")
    if wh_id:
        return wh_id
    client = _get_client()
    warehouses = list(client.warehouses.list())
    # prefere warehouse que já esteja RUNNING
    for wh in warehouses:
        if str(wh.state) == "State.RUNNING":
            return wh.id
    # senão, retorna o primeiro (será iniciado sob demanda)
    if warehouses:
        return warehouses[0].id
    raise RuntimeError("Nenhum SQL Warehouse encontrado no workspace.")


# ── Ferramentas ──────────────────────────────────────────────────────────────


@mcp.tool()
def run_sql(query: str, max_rows: int = 100) -> str:
    """Executa uma query SQL no Databricks e retorna os resultados.

    Args:
        query: Query SQL a ser executada.
        max_rows: Número máximo de linhas a retornar (padrão: 100).
    """
    client = _get_client()
    wh_id = _get_warehouse_id()

    result = client.statement_execution.execute_statement(
        warehouse_id=wh_id,
        statement=query,
        wait_timeout="50s",
        row_limit=max_rows,
    )

    status = result.status
    if status and status.error:
        return f"ERRO: {status.error.message}"

    if not result.manifest or not result.manifest.schema:
        return "Query executada com sucesso (sem resultados)."

    columns = [col.name for col in result.manifest.schema.columns]
    rows = result.result.data_array if result.result and result.result.data_array else []

    # Formata como tabela markdown
    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        lines.append("| " + " | ".join(str(v) if v is not None else "NULL" for v in row) + " |")

    total = result.manifest.total_row_count
    if total and total > max_rows:
        lines.append(f"\n*Mostrando {max_rows} de {total} linhas. Use max_rows para ver mais.*")

    return "\n".join(lines)


@mcp.tool()
def list_catalogs() -> str:
    """Lista todos os catálogos disponíveis no Unity Catalog."""
    client = _get_client()
    catalogs = list(client.catalogs.list())
    if not catalogs:
        return "Nenhum catálogo encontrado."
    lines = ["| Catálogo | Tipo | Comentário |", "| --- | --- | --- |"]
    for cat in catalogs:
        comment = (cat.comment or "")[:80]
        cat_type = str(cat.catalog_type) if cat.catalog_type else "-"
        lines.append(f"| {cat.name} | {cat_type} | {comment} |")
    return "\n".join(lines)


@mcp.tool()
def list_schemas(catalog: str) -> str:
    """Lista todos os schemas de um catálogo.

    Args:
        catalog: Nome do catálogo.
    """
    client = _get_client()
    schemas = list(client.schemas.list(catalog_name=catalog))
    if not schemas:
        return f"Nenhum schema encontrado no catálogo '{catalog}'."
    lines = ["| Schema | Comentário |", "| --- | --- |"]
    for s in schemas:
        comment = (s.comment or "")[:80]
        lines.append(f"| {s.name} | {comment} |")
    return "\n".join(lines)


@mcp.tool()
def list_tables(catalog: str, schema: str) -> str:
    """Lista todas as tabelas de um schema.

    Args:
        catalog: Nome do catálogo.
        schema: Nome do schema.
    """
    client = _get_client()
    tables = list(client.tables.list(catalog_name=catalog, schema_name=schema))
    if not tables:
        return f"Nenhuma tabela encontrada em '{catalog}.{schema}'."
    lines = ["| Tabela | Tipo | Comentário |", "| --- | --- | --- |"]
    for t in tables:
        ttype = str(t.table_type).split(".")[-1] if t.table_type else "-"
        comment = (t.comment or "")[:80]
        lines.append(f"| {t.name} | {ttype} | {comment} |")
    return "\n".join(lines)


@mcp.tool()
def describe_table(full_table_name: str) -> str:
    """Retorna o schema detalhado de uma tabela (colunas, tipos, comentários).

    Args:
        full_table_name: Nome completo da tabela (catalog.schema.table).
    """
    client = _get_client()
    table = client.tables.get(full_name=full_table_name)

    lines = [f"## {table.full_name}\n"]

    if table.comment:
        lines.append(f"**Descrição:** {table.comment}\n")

    ttype = str(table.table_type).split(".")[-1] if table.table_type else "-"
    lines.append(f"**Tipo:** {ttype}")

    if table.storage_location:
        lines.append(f"**Storage:** {table.storage_location}")

    lines.append("")
    lines.append("| Coluna | Tipo | Nullable | Comentário |")
    lines.append("| --- | --- | --- | --- |")

    if table.columns:
        for col in table.columns:
            nullable = "Sim" if col.nullable else "Não"
            comment = (col.comment or "")[:60]
            lines.append(f"| {col.name} | {col.type_name} | {nullable} | {comment} |")

    return "\n".join(lines)


@mcp.tool()
def sample_table(full_table_name: str, rows: int = 10) -> str:
    """Retorna uma amostra de dados de uma tabela.

    Args:
        full_table_name: Nome completo da tabela (catalog.schema.table).
        rows: Número de linhas a retornar (padrão: 10).
    """
    query = f"SELECT * FROM `{full_table_name.replace('.', '`.`')}` LIMIT {rows}"
    return run_sql(query, max_rows=rows)


@mcp.tool()
def table_stats(full_table_name: str) -> str:
    """Retorna estatísticas básicas de uma tabela (contagem, nulos, distinct).

    Args:
        full_table_name: Nome completo da tabela (catalog.schema.table).
    """
    client = _get_client()
    table = client.tables.get(full_name=full_table_name)

    if not table.columns:
        return "Tabela sem colunas definidas."

    escaped = f"`{full_table_name.replace('.', '`.`')}`"

    # Conta total de linhas
    count_result = run_sql(f"SELECT COUNT(*) as total FROM {escaped}", max_rows=1)

    # Monta query de stats por coluna
    col_stats = []
    for col in table.columns[:20]:  # limita a 20 colunas para não estourar
        name = col.name
        col_stats.append(
            f"COUNT(DISTINCT `{name}`) as `{name}_distinct`, "
            f"SUM(CASE WHEN `{name}` IS NULL THEN 1 ELSE 0 END) as `{name}_nulls`"
        )

    stats_query = f"SELECT {', '.join(col_stats)} FROM {escaped}"
    stats_result = run_sql(stats_query, max_rows=1)

    return f"### Contagem\n{count_result}\n\n### Estatísticas por coluna\n{stats_result}"


@mcp.tool()
def list_warehouses() -> str:
    """Lista todos os SQL Warehouses disponíveis no workspace."""
    client = _get_client()
    warehouses = list(client.warehouses.list())
    if not warehouses:
        return "Nenhum SQL Warehouse encontrado."
    lines = ["| ID | Nome | Estado | Tipo |", "| --- | --- | --- | --- |"]
    for wh in warehouses:
        state = str(wh.state).split(".")[-1] if wh.state else "-"
        wh_type = str(wh.warehouse_type).split(".")[-1] if wh.warehouse_type else "-"
        lines.append(f"| {wh.id} | {wh.name} | {state} | {wh_type} |")
    return "\n".join(lines)


@mcp.tool()
def query_history(max_results: int = 10) -> str:
    """Lista as queries recentes executadas no workspace.

    Args:
        max_results: Número máximo de queries a retornar (padrão: 10).
    """
    client = _get_client()
    from databricks.sdk.service.sql import ListQueryHistoryRequest

    history = client.query_history.list(request=ListQueryHistoryRequest())

    lines = ["| Query ID | Status | Duração (ms) | Warehouse |", "| --- | --- | --- | --- |"]
    count = 0
    for q in history:
        if count >= max_results:
            break
        status = str(q.status).split(".")[-1] if q.status else "-"
        duration = q.execution_end_time_ms - q.query_start_time_ms if q.execution_end_time_ms and q.query_start_time_ms else "-"
        lines.append(f"| {q.query_id} | {status} | {duration} | {q.warehouse_id} |")
        count += 1

    return "\n".join(lines)


# ── Entrypoint ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run(transport="stdio")
