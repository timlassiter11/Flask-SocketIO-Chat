FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-cloud-logging

COPY . .

CMD gunicorn --worker-class eventlet --bind :$PORT -w 1 --timeout 0 main:app
