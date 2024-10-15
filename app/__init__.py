import os
import logging
from flask import Flask
from flask_socketio import SocketIO

logger = logging.getLogger(__name__)


socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    redis_host = os.environ.get("REDISHOST")
    redis_port = os.environ.get("REDISPORT")

    kwargs = {"cors_allowed_origins": "*"}
    if redis_host and redis_port:
        redis_connection = f'redis://{redis_host}:{redis_port}'
        kwargs["message_queue"] = redis_connection
        kwargs["async_mode"] = "eventlet"

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app, **kwargs)
    return app

