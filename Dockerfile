FROM python:3.11-slim

# Impede que o Python escreva os arquivos .pyc e bufferize o output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema necessárias para o PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala os requisitos do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Cria um usuário de sistema sem privilégios para rodar o app de forma segura
RUN useradd -u 5678 --disabled-password --gecos "" django-user

# Copia o restante do código e define o dono como o novo usuário
COPY --chown=django-user:django-user . /app/

# Altera para o usuário não-root antes de rodar o comando principal
USER django-user

EXPOSE 8000

# Executa as migrações e sobe o servidor de desenvolvimento
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]