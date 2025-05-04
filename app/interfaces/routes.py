from flask import Blueprint
from interfaces.http.controllers import pedido_controller

routes_bp = Blueprint("routes", __name__)

# Rotas de Pedido
routes_bp.route("/pedido", methods=["POST"])(pedido_controller.criar_pedido_controller)
routes_bp.route("/pedido/<int:codigo_pedido>", methods=["GET"])(pedido_controller.get_valor_pedido_controller)
routes_bp.route("/cliente/<int:codigo_cliente>/quantidade_pedidos", methods=["GET"])(pedido_controller.get_quantidade_pedidos_cliente_controller)
routes_bp.route("/cliente/<int:codigo_cliente>/pedidos", methods=["GET"])(pedido_controller.get_pedidos_cliente_controller)
