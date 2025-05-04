FROM python:3.13-alpine

WORKDIR /app

# Instalar dependências do sistema para compilar pacotes Python
RUN apk add --no-cache gcc musl-dev libffi-dev

# Instalar dependências do Python
COPY app/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copie o restante do app
COPY app/ .
ENV PYTHONPATH=/app

# Comando para rodar o Flask
CMD ["python", "main.py"]