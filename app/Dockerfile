FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala Python y pip
RUN apt-get update && apt-get install -y \
    python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copia dependencias y las instala
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia el código de la app
COPY . .

EXPOSE 5000
CMD ["python3", "app.py"]

