# noinspection PyPackageRequirements
import socketio
import uvicorn as uvicorn

import mylog
from model.doorcards import factory as doorcard_factory
from model.gamestate import GameState
from model.heroes import factory as hero_factory
from model.table import Table

log = mylog.getLogger(__name__)

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './ui/dist/index.html',
    '/static': './ui/dist',
})


async def emit_message(m):
    if m:
        log.info(f'emit_message{m=}')
        await sio.emit('gameevent', str(m))


def get_gameloop():
    heroes = {
        'benji': hero_factory.hero('benji', 'barbarian'),
        'austin': hero_factory.hero('austin', 'healer'),
    }
    # Draws the hero's initial hand
    for _ in range(0, 5):
        for hero in heroes.values():
            hero.draw_card()

    # Deal boss mat and door deck
    boss = doorcard_factory.create_boss()
    doordeck = doorcard_factory.deal_deck(
        boss.num_door_cards, len(heroes))

    game = GameState(heroes, doordeck, boss)
    return Table(game, emit_message, mylog)


table = get_gameloop()


@sio.event
def connect(sid, _):
    log.info('client %s connected', sid)


@sio.event
def connect_error(sid):
    log.error('client %s could not connect', sid)


@sio.event
def disconnect(sid):
    log.info('client %s disconnected', sid)


@sio.on('hello')
async def hello(sid, message):
    log.info('received message: %s', message)
    await sio.emit('state', str(table.gamestate), to=sid)


@sio.on('command')
async def command(sid, cmd):
    log.info('queue command: %s', cmd)
    await sio.send('queued command', to=sid)
    await table.process_command(cmd)


if __name__ == '__main__':
    log.info('Starting up the server at http://%s:%d', "127.0.0.1", 8080)
    uvicorn.run(app, host="127.0.0.1", port=8080)
