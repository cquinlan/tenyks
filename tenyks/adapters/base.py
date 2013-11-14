import queue

import threading


class BaseAdapter(threading.Thread):

    def __init__(self):
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        super(BaseAdapter, self).__init__()

    def connect(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()
