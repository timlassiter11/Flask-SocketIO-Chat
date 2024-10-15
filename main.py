import eventlet
eventlet.monkey_patch()

from app import create_app, socketio

app = create_app(debug=False)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080)
