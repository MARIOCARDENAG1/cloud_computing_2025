FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala HAProxy
RUN apt-get update && apt-get install -y haproxy && \
    rm -rf /var/lib/apt/lists/*

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

EXPOSE 80
CMD ["haproxy", "-db", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

