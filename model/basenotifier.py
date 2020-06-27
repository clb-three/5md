from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    @abstractmethod
    def info(self, msg):
        '''Emit an informational notification'''

    @abstractmethod
    def error(self, msg):
        '''Emit an error notification'''

    @abstractmethod
    def log(self, msg):
        '''Emit a log message'''
