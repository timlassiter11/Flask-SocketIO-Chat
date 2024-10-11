import eventlet
eventlet.monkey_patch()

# Imports the Cloud Logging client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()

#!/bin/env python
from app import create_app, socketio

app = create_app(debug=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
