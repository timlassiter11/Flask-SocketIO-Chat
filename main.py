import eventlet
eventlet.monkey_patch()

import redis
#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080, debug=False)
