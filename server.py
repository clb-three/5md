# noinspection PyPackageRequirements
import asyncio

import socketio
import uvicorn as uvicorn

import mylog
from model import table_factory
from model.message import Message

log = mylog.getLogger(__name__)

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

import types


async def emit_message(m):
    async def do_emit(msg):
        log.info('emit_message %s', msg)
        await sio.emit('gameevent', str(msg))

    if m:
        if isinstance(m, types.GeneratorType) or isinstance(m, list):
            for subm in m:
                await do_emit(subm)
        else:
            await do_emit(m)


table = table_factory.get_table(emit_message)


async def once_per_second():
    while True:
        # log.debug('stepping environment...')
        table.gamestate.step()
        await asyncio.sleep(1)


async def startup():
    asyncio.get_event_loop().create_task(once_per_second())


app = socketio.ASGIApp(sio, on_startup=startup)


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
    await sio.send(f'queued command {cmd}', to=sid)
    await table.process_command(cmd)


if __name__ == '__main__':
    log.info('Starting up the server at http://%s:%d', "127.0.0.1", 8080)
    uvicorn.run(app, host="127.0.0.1", port=8080)
