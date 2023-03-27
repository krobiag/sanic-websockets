import socketio
import datetime
import json
sio = socketio.AsyncServer(async_mode='sanic', cors_allowed_origins="*")


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.event
async def received_random_country(sid, data):
    print('message from received_random_country', sid, data)


@sio.event
async def ping_server(sid):
    now = datetime.datetime.now()
    dt_str = now.strftime("%Y-%m-%d %H:%M:%S")
    await sio.emit("pong_server", {
        "type": "pong",
        "message": "Pong",
        "timestamp": dt_str,
    })
