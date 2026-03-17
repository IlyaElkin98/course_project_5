FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libpg-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirement.txt

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8000