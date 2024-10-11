FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-cloud-logging

COPY . .

ENV GOOGLE_CLOUD_PROJECT="autter-438312"
RUN gcloud components install beta -q && \
    gcloud beta functions deploy my-background-function --trigger-http --runtime python39 --source . --entry-point=hello_http --project $GOOGLE_CLOUD_PROJECT --allow-unauthenticated

CMD exec gunicorn --worker-class eventlet --bind :$PORT --workers 1 --timeout 0 main:app
