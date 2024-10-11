FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GOOGLE_CLOUD_PROJECT="autter-438312"
RUN gcloud components install beta -q && \
    gcloud beta functions deploy my-background-function --trigger-http --runtime python39 --source . --entry-point=hello_http --project $GOOGLE_CLOUD_PROJECT --allow-unauthenticated

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
