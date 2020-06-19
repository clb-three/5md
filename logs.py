import logging
import sys

# This is a singleton, it's initialized only once and then the reference is shared.
globallog = None
if not globallog:
    globallog = logging.getLogger('five-minute-dungeon')
    globallog.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    globallog.addHandler(ch)
