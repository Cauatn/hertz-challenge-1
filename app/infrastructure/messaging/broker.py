import pika
import time
from config.settings import RABBITMQ_URL

def connect(max_retries=5, delay=5):
    """
    Tenta se conectar ao RabbitMQ com múltiplas tentativas.
    """
    for attempt in range(max_retries):
        try:
            connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"Falha na conexão com RabbitMQ. Tentativa {attempt+1}/{max_retries}")
            time.sleep(delay)
    raise ConnectionError("Não foi possível conectar ao RabbitMQ após múltiplas tentativas.")
