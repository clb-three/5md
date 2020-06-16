from io import StringIO
import contextlib
from logs import globallog
from core.gameloop import GameLoop
import time
import asyncio
from threading import Thread


commands = []
shouldrun = True


def get_command():
    globallog.info('waiting for command')
    while shouldrun and not any(commands):
        time.sleep(1 / 100)

    if not shouldrun:
        return 'quit'

    globallog.info('getting command')
    return commands.pop()


def run(gameloop, command_getter, echo_func):
    with readit(echo_func) as stream:
        with contextlib.redirect_stdout(stream):
            gameloop.loop(command_getter)


class MyStringIO(StringIO):
    def __init__(self, echo_func):
        super().__init__()
        self.echo_func = echo_func

    def write(self, str):
        self.echo_func(str)
        super().write(str)


@contextlib.contextmanager
def readit(echo_func):
    sio = MyStringIO(echo_func)
    yield sio
    sio.close()


@contextlib.contextmanager
def gib(echo_func):
    '''
    GIB: Game loop running In Background.
    The game loop runs in a background thread.
    '''

    loop = asyncio.new_event_loop()
    shouldrun = True
    commands.clear()
    gameloop = GameLoop()

    t = Thread(target=run, args=(gameloop, get_command, echo_func))
    t.start()

    yield gameloop

    shouldrun = False
    t.join()
