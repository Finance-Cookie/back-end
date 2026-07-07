FROM python:3.11-slim

# Impede que o Python escreva os arquivos .pyc e bufferize o output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências do sistema e cria o usuário não-root em uma única camada
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -u 5678 --create-home django-user

# Copia e instala os requisitos do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia explicitamente apenas os arquivos e pastas necessários do Django
COPY --chown=django-user:django-user manage.py /app/
COPY --chown=django-user:django-user config/ /app/config/
COPY --chown=django-user:django-user finance_cookie/ /app/finance_cookie/

# Altera para o usuário não-root antes de rodar o comando principal
USER django-user

EXPOSE 8000

# CORREÇÃO SONAR: Sintaxe baseada em vetor para o CMD
CMD ["/bin/sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]