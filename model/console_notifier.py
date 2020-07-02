
from datetime import datetime

from .basenotifier import BaseNotifier


class ConsoleNotifier(BaseNotifier):
    def info(self, msg):
        print(f'[inf] {self.now()} {msg}')

    def error(self, msg):
        print(f'[err] {self.now()} {msg}')

    def log(self, msg):
        print(f'[log] {self.now()} {msg}')

    def state(self, msg):
        print(f'[state] {self.now()} {msg}')

    def now(self):
        return datetime.now().strftime("%H:%M:%S")
