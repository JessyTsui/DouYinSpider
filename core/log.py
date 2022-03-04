from .config import EnsureExist
import sys, time, os


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def now_time(self):
        now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        return now

    def path(self):
        now = Logger().now_time()
        path = "./log/{}/".format(now)
        EnsureExist(path)
        return path

    def flush(self):
        pass
