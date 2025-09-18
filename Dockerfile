FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd && rm -rf /var/lib/apt/lists/*
ENV PATH="/usr/games:${PATH}"
WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh && sed -i 's/\r$//' wisecow.sh
EXPOSE 4499
CMD ["bash", "./wisecow.sh"]
