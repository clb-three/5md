import time
from threading import Thread

from logs import GLOBAL_LOG
from model.gameloop import GameLoop


class Looper:
    def __init__(self, notifier, commands):
        '''
        Emit the 
        '''
        self.gameloop = GameLoop(notifier)

        self.commands = commands

        self.shouldrun = True
        self.loop_task = None

    def get_command(self):
        GLOBAL_LOG.info('waiting for command')
        while self.shouldrun and not any(self.commands):
            time.sleep(1 / 100)

        if not self.shouldrun:
            return 'quit'

        GLOBAL_LOG.info('getting command')
        return self.commands.pop()

    def run(self):
        self.gameloop.loop(self.get_command)

    def __enter__(self):
        self.shouldrun = True
        self.commands.clear()
        self.loop_task = Thread(target=self.run)
        self.loop_task.start()

    def __exit__(self, *args):
        self.shouldrun = False
        self.loop_task.join()
