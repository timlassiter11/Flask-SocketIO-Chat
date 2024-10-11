import os
from flask import Flask
from flask_socketio import SocketIO

from gevent import monkey
monkey.patch_all()

redis_host = os.environ.get("REDISHOST")
redis_port = os.environ.get("REDISPORT")

socketio = SocketIO(message_queue=f'redis://{redis_host}:{redis_port}', async_mode='gevent')


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app, cors_allowed_origins="*")
    return app

