import json
from infrastructure.messaging.broker import connect
from domain.repositories.pedido_repository import PgPedidoRepository
from domain.services.pedido_service import PedidoService
from application.criar_pedido import CriarPedido

def start_consuming():
    conn = connect()
    channel = conn.channel()
    channel.queue_declare(queue='pedidos')

    def callback(ch, method, properties, body):
        print("Mensagem recebida da fila 'pedidos'")
        try:
            data = json.loads(body)
            repo = PgPedidoRepository()
            service = PedidoService(repo)
            CriarPedido(service).execute(data)
            print(f"Pedido processado com sucesso: {data['codigoPedido']}")
        except Exception as e:
            print(f"Erro ao processar pedido: {e}")

    channel.basic_consume(queue='pedidos', on_message_callback=callback, auto_ack=True)
    print("Consumindo mensagens da fila 'pedidos'...")
    channel.start_consuming()

if __name__ == "__main__":
    start_consuming()
