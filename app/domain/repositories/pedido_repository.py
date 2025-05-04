from infrastructure.db.connection import get_db_connection, release_db_connection

class PgPedidoRepository:
    def insert_pedido(self, codigo_pedido: int, codigo_cliente: int, itens: list) -> None:
        valor_total = sum(item["quantidade"] * item["preco"] for item in itens)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO pedidos (codigo_pedido, codigo_cliente, valor_total)
            VALUES (%s, %s, %s)
        """, (codigo_pedido, codigo_cliente, valor_total))
        conn.commit()
        cur.close()
        release_db_connection(conn)

    def get_valor_pedido(self, codigo_pedido: int) -> float | None:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT valor_total FROM pedidos WHERE codigo_pedido = %s", (codigo_pedido,))
        result = cur.fetchone()
        cur.close()
        release_db_connection(conn)
        return result["valor_total"] if result else None

    def count_by_cliente(self, codigo_cliente: int) -> int:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) as qtde FROM pedidos WHERE codigo_cliente = %s", (codigo_cliente,))
        result = cur.fetchone()
        cur.close()
        release_db_connection(conn)
        return result["qtde"] if result else 0

    def list_by_cliente(self, codigo_cliente: int) -> list:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM pedidos WHERE codigo_cliente = %s", (codigo_cliente,))
        results = cur.fetchall()
        cur.close()
        release_db_connection(conn)
        return results
