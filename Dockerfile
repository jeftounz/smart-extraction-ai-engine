# Usamos una imagen oficial de Python ligera
FROM python:3.12-slim

# Evita que Python escriba archivos .pyc y fuerza que la salida estándar vaya a la terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalamos dependencias del sistema operativo:
# PostgreSQL (libpq-dev) y el navegador Chromium para que Selenium funcione
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias y las instalamos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código de tu proyecto al contenedor
COPY . /app/

# Exponemos el puerto de Django
EXPOSE 8000