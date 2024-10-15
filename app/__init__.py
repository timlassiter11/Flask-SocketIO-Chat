import os
import redis
import logging
from flask import Flask
from flask_socketio import SocketIO

logger = logging.getLogger(__name__)


redis_host = os.environ.get("REDISHOST", '127.0.0.1')
redis_port = os.environ.get("REDISPORT", 6379)

redis_connection = f'redis://{redis_host}:{redis_port}'

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app, cors_allowed_origins="*", message_queue=redis_connection, async_mode='eventlet')
    return app

