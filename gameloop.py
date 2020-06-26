from io import StringIO
import contextlib
from logs import globallog
from model.gameloop import GameLoop
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
        self.echo_func(f'[log] {self.now()} {msg}')

    def now(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")


@contextlib.contextmanager
def gib(echo_func):
    '''
    GIB: Game loop running In Background.
    The game loop runs in a background thread.
    '''

    loop = asyncio.new_event_loop()
    shouldrun = True
    commands.clear()
    notifier = SocketIoNotifier(echo_func)
    gameloop = GameLoop(notifier)

    t = Thread(target=run, args=(gameloop, get_command))
    t.start()

    yield gameloop

    shouldrun = False
    t.join()
