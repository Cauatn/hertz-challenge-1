import os
from psycopg2 import pool, connect
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.getenv("DATABASE_URL")
_min_conn = 1
_max_conn = 10
_pg_pool = None

def init_db_pool(minconn: int = _min_conn, maxconn: int = _max_conn):
    global _pg_pool
    if _pg_pool is None:
        if not DATABASE_URL:
            raise RuntimeError("DATABASE_URL não configurado")
        _pg_pool = pool.SimpleConnectionPool(
            minconn,
            maxconn,
            dsn=DATABASE_URL,
            cursor_factory=RealDictCursor
        )
    return _pg_pool

def get_db_connection():
    """
    Retorna uma conexão do pool. Lembre de chamar release_db_connection().
    """
    if _pg_pool is None:
        init_db_pool()
    try:
        return _pg_pool.getconn()
    except Exception as e:
        raise RuntimeError(f"Erro ao obter conexão do pool: {e}")

def release_db_connection(conn):
    """
    Devolve a conexão ao pool.
    """
    if _pg_pool and conn:
        _pg_pool.putconn(conn)

def close_all_connections():
    """
    Para usar em shutdown: fecha todas as conexões do pool.
    """
    if _pg_pool:
        _pg_pool.closeall()
