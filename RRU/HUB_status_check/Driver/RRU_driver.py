import threading
from SSHconnect import SshConnect


class RruControl(threading.Thread):
    def __init__(self, name='RRU_Control'):
        super().__init__()
        self.name = name

    def run(self):
        pass


if __name__ == '__main__':
    print('PyCharm')
