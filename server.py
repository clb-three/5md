# noinspection PyPackageRequirements
import socketio
import uvicorn as uvicorn

import mylog
from model import table_factory
from model.message import Message

log = mylog.getLogger(__name__)

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)


async def emit_message(m):
    if m:
        log.info('emit_message %s', m)
        await sio.emit('gameevent', str(m))


table = table_factory.get_table(emit_message)


@sio.event
def connect(sid, _):
    log.info('client %s connected', sid)


@sio.event
def connect_error(sid):
    log.error('client %s could not connect', sid)


@sio.event
def disconnect(sid):
    log.info('client %s disconnected', sid)


@sio.event
def message(sid, msg):
    log.info('client %s sent a message: %s', sid, msg)


@sio.on('hello')
async def hello(sid):
    log.info('initialize %s', sid)
    await emit_message(Message('state', table.gamestate))


@sio.on('command')
async def command(sid, cmd):
    log.info('queue command: %s', cmd)
    await sio.send('queued command', to=sid)
    await table.process_command(cmd)


if __name__ == '__main__':
    log.info('Starting up the server at http://%s:%d', "127.0.0.1", 8080)
    uvicorn.run(app, host="127.0.0.1", port=8080)
