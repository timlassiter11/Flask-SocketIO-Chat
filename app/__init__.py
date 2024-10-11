from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(message_queue='redis://10.225.231.3:6379')


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app, cors_allowed_origins="*")
    return app

