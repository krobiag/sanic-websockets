import socketio

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
