import threading
from SSHconnect import SshConnect


class HubControl(threading.Thread):
    def __init__(self, name='Hub_Control'):
        super().__init__()
        self.name = name
        self.connect = SshConnect()

    def run(self):
        pass

    def status_query(self):
        pass


if __name__ == '__main__':
    print('PyCharm')
