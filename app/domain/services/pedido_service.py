class PedidoService:
    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def criar_pedido(self, codigo_pedido: int, codigo_cliente: int, itens: list) -> None:
        if not itens:
            raise ValueError("Pedido deve conter ao menos um item.")
        self.pedido_repository.insert_pedido(codigo_pedido, codigo_cliente, itens)

    def consultar_valor_pedido(self, codigo_pedido: int) -> float | None:
        return self.pedido_repository.get_valor_pedido(codigo_pedido)

    def contar_pedidos_por_cliente(self, codigo_cliente: int) -> int:
        return self.pedido_repository.count_by_cliente(codigo_cliente)

    def listar_pedidos_por_cliente(self, codigo_cliente: int) -> list:
        return self.pedido_repository.list_by_cliente(codigo_cliente)