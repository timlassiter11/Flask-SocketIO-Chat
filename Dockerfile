# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.12.7

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True
ENV GCR_ENV=production

# Copy local code to the container image.
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD exec gunicorn --worker-class eventlet --bind :$PORT --workers 1 --timeout 0 main:app