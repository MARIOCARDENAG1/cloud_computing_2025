FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala MongoDB
RUN apt-get update && apt-get install -y mongodb && \
    mkdir -p /data/db && rm -rf /var/lib/apt/lists/*

VOLUME /data/db
EXPOSE 27017

CMD ["mongod", "--bind_ip", "0.0.0.0", "--dbpath", "/data/db"]

