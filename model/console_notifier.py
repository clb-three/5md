
from datetime import datetime


class ConsoleNotifier():
    def info(self, msg):
        print(f'[inf] {self.now()} {msg}')

    def error(self, msg):
        print(f'[err] {self.now()} {msg}')

    def log(self, msg):
        print(f'[log] {self.now()} {msg}')

    def now(self):
        return datetime.now().strftime("%H:%M:%S")
