# Desafio Engenheiro de Software - HERTZ

## [Relatório Técnico](app/RELATORIO.md)

## Descrição

Este é um projeto de software desenvolvido como parte do desafio para a vaga de Engenheiro de Software na HERTZ. A aplicação processa pedidos de clientes, gera relatórios e disponibiliza uma API RESTful para consultar informações sobre pedidos e clientes.

Rotas (Simplificado):
- API flask - http://localhost:5000/
- RabbitMQ - http://localhost:15672/#/
   - login: guest
   - senha: guest


## Tecnologias Utilizadas

- **Flask**: Framework para a construção da API REST.
- **PostgreSQL**: Banco de dados relacional para armazenar os pedidos.
- **RabbitMQ**: Fila de mensagens para processar os pedidos.
- **Docker**: Contêineres para facilitar o desenvolvimento e deploy.

## Como Rodar a Aplicação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Cauatn/hertz-challenge-1.git
   cd hertz-challenge-1
   ```

2. **Configure o arquivo de variáveis de ambiente:**
   Copie o arquivo `.env.example` para `.env` no mesmo diretório e configure as variáveis conforme necessário.

   ```bash
   cp .env.example .env
   ```

3. **Inicie a aplicação com Docker Compose:**
   ```bash
   docker-compose up --build
   ```

Isso irá levantar todos os containers necessários para o funcionamento da aplicação.

## Estrutura de Pastas

- **`/app`**: Contém o código da aplicação Flask.
- **`/infrastructure`**: Implementações de conexão com o banco de dados e outros serviços.
- **`/infrastructure/messaging/consumer/py`**: Arquivo responsavel por escutar o serviço RabbitMQ e salvar no banco os pedidos.

## Endpoints da API

### **POST** `/pedido`

Cria um novo pedido.

**Exemplo de uso:**

```bash
curl -X POST http://localhost:5000/pedido -H "Content-Type: application/json" -d '{
    "codigoPedido": 1001,
    "codigoCliente": 1,
    "itens": [
        {"produto": "lápis", "quantidade": 100, "preco": 1.10},
        {"produto": "caderno", "quantidade": 10, "preco": 1.00}
    ]
}'
```

### **GET** `/pedido/<int:codigo_pedido>`

Retorna o valor total de um pedido.

**Exemplo de uso:**

```bash
curl http://localhost:5000/pedido/1001
```

### **GET** `/cliente/<int:codigo_cliente>/quantidade_pedidos`

Retorna a quantidade de pedidos realizados por um cliente.

**Exemplo de uso:**

```bash
curl http://localhost:5000/cliente/1/quantidade_pedidos
```

### **GET** `/cliente/<int:codigo_cliente>/pedidos`

Lista todos os pedidos realizados por um cliente.

**Exemplo de uso:**

```bash
curl http://localhost:5000/cliente/1/pedidos
```

## Exemplo de Mensagem no RabbitMQ

A aplicação consome mensagens no RabbitMQ com o seguinte formato:

```json
{
  "codigoPedido": 1001,
  "codigoCliente": 1,
  "itens": [
    {
      "produto": "lápis",
      "quantidade": 100,
      "preco": 1.1
    },
    {
      "produto": "caderno",
      "quantidade": 10,
      "preco": 1.0
    }
  ]
}
```

### O que acontece com a mensagem:

- O serviço recebe a mensagem do RabbitMQ.
- Calcula o valor total do pedido.
- Insere o pedido no banco de dados PostgreSQL.

## Requisitos

- Python 3.x
- Docker
- Docker Compose

## Padrão de Arquitetura

A aplicação segue o padrão de **Domain-Driven Design (DDD)**, estruturando o código em torno dos domínios da aplicação e mantendo a separação de responsabilidades entre as camadas de serviço, repositório e controle de fluxo.

- **`PedidoService`**: Camada de serviço que gerencia a lógica de criação e consulta de pedidos.
- **`PgPedidoRepository`**: Camada de repositório que gerencia a persistência dos pedidos no PostgreSQL.
- **`routes_bp`**: Camada de controle, onde são definidas as rotas da API.

## Tecnologias e Ferramentas

- **Flask**: Para a construção da API RESTful.
- **Psycopg2**: Para a conexão com o banco de dados PostgreSQL.
- **Pika**: Para a comunicação com RabbitMQ.
- **Docker**: Para a orquestração dos containers (API, RabbitMQ e PostgreSQL).

## Considerações Finais

- As variáveis de ambiente devem ser configuradas corretamente para que a aplicação funcione.
- O uso do Docker permite que o ambiente seja facilmente reproduzido em qualquer máquina.
