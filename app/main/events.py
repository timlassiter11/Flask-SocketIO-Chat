from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

ROOM = "1"

@socketio.on("joined", namespace="/chat")
def joined_handler(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    session["name"] = message["name"]
    join_room(ROOM)
    emit(
        "status",
        {
            "msg": f"{message['name']} has entered the room.",
        },
        to="1",
    )


@socketio.on("message", namespace="/chat")
def message_handler(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    emit(
        "message",
        {
            "msg": f"{session.get('name')}: {message['msg']}",
        },
        to=ROOM,
    )


@socketio.on("left", namespace="/chat")
def left_handler(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    leave_room(ROOM)
    emit(
        "status",
        {
            "msg": f"{session.get('name')} has left the room.",
        },
        to=ROOM,
    )
