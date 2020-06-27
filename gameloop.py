import contextlib
import time
from datetime import datetime
from threading import Thread

from logs import GLOBAL_LOG
from model.gameloop import GameLoop

commands = []
SHOULD_RUN = True


def get_command():
    GLOBAL_LOG.info('waiting for command')
    while SHOULD_RUN and not any(commands):
        time.sleep(1 / 100)

    if not SHOULD_RUN:
        return 'quit'

    GLOBAL_LOG.info('getting command')
    return commands.pop()


def run(gameloop, command_getter):
    gameloop.loop(command_getter)


class SocketIoNotifier():

    def __init__(self, echo_func):
        self.echo_func = echo_func

    def info(self, msg):
        self.echo_func(f'[inf] {self.now()} {msg}')

    def error(self, msg):
        self.echo_func(f'[err] {self.now()} {msg}')

    def log(self, msg):
        GLOBAL_LOG.info('[log] %s %s', self.now(), msg)

    def now(self):
        return datetime.now().strftime("%H:%M:%S")


@contextlib.contextmanager
def gib(echo_func):
    '''
    GIB: Game loop running In Background.
    The game loop runs in a background thread.
    '''

    global SHOULD_RUN

    SHOULD_RUN = True
    commands.clear()
    notifier = SocketIoNotifier(echo_func)
    gameloop = GameLoop(notifier)

    t = Thread(target=run, args=(gameloop, get_command))
    t.start()

    yield gameloop

    SHOULD_RUN = False
    t.join()
