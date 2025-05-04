class CriarPedido:
    def __init__(self, pedido_service):
        self.pedido_service = pedido_service

    def execute(self, data: dict) -> None:
        codigo_pedido = data.get("codigoPedido")
        codigo_cliente = data.get("codigoCliente")
        itens = data.get("itens", [])

        if not codigo_pedido or not codigo_cliente:
            raise ValueError("Código do pedido e do cliente são obrigatórios.")
        
        if not isinstance(itens, list) or not itens:
            raise ValueError("O pedido deve conter ao menos um item válido.")

        self.pedido_service.criar_pedido(codigo_pedido, codigo_cliente, itens)
