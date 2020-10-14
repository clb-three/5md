import logging

from uvicorn.config import LOGGING_CONFIG

# Set all of uvicorn's streamhandlers to warning minimum
for h in LOGGING_CONFIG['handlers'].values():
    h['level'] = 'WARNING'

logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s::%(name)s::%(levelname)s::%(message)s')


def getLogger(name):
    """Get a logger with a certain name."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(name)s::%(levelname)s::%(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
