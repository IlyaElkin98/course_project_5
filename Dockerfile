FROM python:3.12-slim

WORKDIR /app

RUN sudo apt-get update && \
    sudo apt-get install -y gcc libpg-dev && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

COPY requirement.txt /app/

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8000
