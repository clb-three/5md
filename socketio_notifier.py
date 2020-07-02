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
        self.echo_func(f'inf {msg}')

    def error(self, msg):
        self.echo_func(f'err {msg}')

    def state(self, msg):
        self.echo_func(f'state {msg}')

    def log(self, msg):
        GLOBAL_LOG.info(f'log {msg}')

    def now(self):
        return datetime.now().strftime("%H:%M:%S")
