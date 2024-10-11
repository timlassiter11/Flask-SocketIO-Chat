FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-cloud-logging

COPY . .

#CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "main:app", "-k", "eventlet.wsgi.server"]
#CMD gunicorn --bind 0.0.0.0:$PORT main:app -k eventlet.wsgi.server
CMD exec gunicorn --worker-class eventlet --bind :$PORT --workers 1 --timeout 0 main:app
