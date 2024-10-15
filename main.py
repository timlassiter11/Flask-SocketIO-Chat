app = None

if __name__ == '__main__':
    from app import create_app, socketio
    app = create_app(debug=True)
    socketio.run(app, host='127.0.0.1', port=8080, debug=True)
else:
    import eventlet
    eventlet.monkey_patch()
    from app import create_app, socketio
    app = create_app(debug=False)
