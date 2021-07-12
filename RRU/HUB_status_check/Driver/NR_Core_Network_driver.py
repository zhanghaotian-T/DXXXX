import threading
from SSHconnect import SshConnect


class CoreNetworkControl(threading.Thread):
    def __init__(self, name='NR_Core_Network_Control'):
        super().__init__()
        self.name = name

    def run(self):
        pass


if __name__ == '__main__':
    print('PyCharm')
