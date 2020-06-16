import contextlib
from logs import globallog
from core.gameloop import GameLoop
import time
import asyncio
from threading import Thread


commands = None
gameloop = None
shouldrun = None


def get_command():
    globallog.info('waiting for command')
    while shouldrun and not any(commands):
        time.sleep(1 / 100)
    if not shouldrun:
        return 'quit'
    globallog.info('getting command')
    return commands.pop()


@contextlib.contextmanager
def gib():
    '''
    GIB: Game loop running In Background.
    The game loop runs in a background thread.
    '''

    loop = asyncio.new_event_loop()
    shouldrun = True
    commands = []
    gameloop = GameLoop()

    t = Thread(target=gameloop.loop, args=(get_command,))
    t.start()

    yield gameloop

    shouldrun = False
    t.join()
