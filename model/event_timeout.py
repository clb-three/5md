
import time
from threading import Thread


class EventTimeout(Thread):
    '''
    Events should be triggered after some time, so
    this encodes the timer and the business logic to ensure safe execution.
    '''

    DEFAULT_TIMEOUT_SEC = 3  # Event timeout in seconds

    def __init__(self, event, ctx):
        def timer():
            time.sleep(EventTimeout.DEFAULT_TIMEOUT_SEC)
            if ctx.target is not event:
                event.do_script(ctx)

        super().__init__(target=timer)
