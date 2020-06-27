import logging
import sys

# This is a singleton, it's initialized only once and then the reference is shared.
GLOBAL_LOG = None
if not GLOBAL_LOG:
    GLOBAL_LOG = logging.getLogger('five-minute-dungeon')
    GLOBAL_LOG.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    GLOBAL_LOG.addHandler(ch)
