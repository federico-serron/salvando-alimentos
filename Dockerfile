FROM python:3.11-slim

WORKDIR /app

# Instala gcc y dependencias para compilar paquetes como numpy
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Asegura que existan los directorios para uploads
RUN mkdir -p web/static/storage/users web/static/storage/products

# Asegura que Python busque módulos en /app
ENV PYTHONPATH=/app

EXPOSE 5001 5002

CMD ["gunicorn", "--help"]