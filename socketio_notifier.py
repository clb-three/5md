from datetime import datetime

from logs import GLOBAL_LOG
from model.basenotifier import BaseNotifier


class SocketIoNotifier(BaseNotifier):
    '''A notifier to emit SocketIO events.'''

    def __init__(self, app, socketio):
        with app.app_context():
            self.echo_func = lambda message: socketio.emit(
                'gameevent', message, broadcast=True)

    def info(self, msg):
        self.echo_func(f'[inf] {self.now()} {msg}')

    def error(self, msg):
        self.echo_func(f'[err] {self.now()} {msg}')

    def log(self, msg):
        GLOBAL_LOG.info('[log] %s %s', self.now(), msg)

    def now(self):
        return datetime.now().strftime("%H:%M:%S")
