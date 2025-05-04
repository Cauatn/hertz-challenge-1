class ListarPedidosCliente:
    def __init__(self, pedido_service):
        self.pedido_service = pedido_service

    def execute(self, codigo_cliente: int) -> list:
        if not codigo_cliente:
            raise ValueError("Código do cliente é obrigatório.")
        
        return self.pedido_service.listar_pedidos_por_cliente(codigo_cliente)
