CREATE TABLE IF NOT EXISTS pedidos (
  id SERIAL PRIMARY KEY,
  codigo_pedido INT,
  codigo_cliente INT, 
  valor_total FLOAT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);