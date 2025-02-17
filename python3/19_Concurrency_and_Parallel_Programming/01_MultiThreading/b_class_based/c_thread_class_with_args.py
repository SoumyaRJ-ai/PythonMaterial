"""
Purpose:
    This is not very trivial to access the values of
    args and kwargs from a subclass as their values are
    being saved in private variables.
"""

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="(%(threadName)-10s) %(message)s",
)


class ThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None):
        threading.Thread.__init__(
            self,
            group=group,
            target=target,
            name=name,
            args=(),
            kwargs=None,
            daemon=None,
        )
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("This thread is running with %s and %s", self.args, self.kwargs)


for x in range(5):
    myThread = ThreadWithArgs(args=(x,), kwargs={"Country": "USA", "Zip": "12345"})
    myThread.start()
    time.sleep(1)
