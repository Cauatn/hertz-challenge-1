from flask import jsonify, request
from domain.services.pedido_service import PedidoService
from domain.repositories.pedido_repository import PgPedidoRepository

pedido_service = PedidoService(PgPedidoRepository())

def criar_pedido_controller():
    """
    Endpoint para criar um novo pedido.
    Espera JSON com os campos: codigoPedido, codigoCliente, itens.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    try:
        codigo_pedido = data["codigoPedido"]
        codigo_cliente = data["codigoCliente"]
        itens = data["itens"]
        pedido_service.criar_pedido(codigo_pedido, codigo_cliente, itens)
        return jsonify({"msg": "Pedido criado com sucesso"}), 201
    except KeyError:
        return jsonify({"error": "JSON deve conter codigoPedido, codigoCliente e itens"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_valor_pedido_controller(codigo_pedido: int):
    """
    Retorna o valor total de um pedido.
    """
    valor = pedido_service.consultar_valor_pedido(codigo_pedido)
    if valor is not None:
        return jsonify({"codigo_pedido": codigo_pedido, "valor_total": valor})
    return jsonify({"error": "Pedido não encontrado"}), 404

def get_quantidade_pedidos_cliente_controller(codigo_cliente: int):
    """
    Retorna a quantidade de pedidos de um cliente.
    """
    quantidade = pedido_service.contar_pedidos_por_cliente(codigo_cliente)
    return jsonify({"codigo_cliente": codigo_cliente, "quantidade_pedidos": quantidade})

def get_pedidos_cliente_controller(codigo_cliente: int):
    """
    Retorna a lista de pedidos de um cliente.
    """
    pedidos = pedido_service.listar_pedidos_por_cliente(codigo_cliente)
    if pedidos:
        return jsonify({"codigo_cliente": codigo_cliente, "pedidos": pedidos})
    return jsonify({"error": "Cliente não encontrado ou sem pedidos"}), 404