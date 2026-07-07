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

# Copia e instala os requisitos (permanece pertencendo ao root, apenas leitura)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# CORREÇÃO SONAR: Copia como root. O django-user conseguirá ler e executar, mas não modificar os arquivos fonte.
COPY manage.py /app/
COPY config/ /app/config/
COPY finance_cookie/ /app/finance_cookie/

# Altera para o usuário não-root antes de rodar o comando principal
USER django-user

EXPOSE 8000

# Sintaxe baseada em vetor para o CMD conforme exigido pelas regras do Sonar
CMD ["/bin/sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]