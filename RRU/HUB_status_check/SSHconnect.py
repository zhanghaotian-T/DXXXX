import paramiko
import dgautolibs


class SshConnect(object):
    def __init__(self):
        self.connect_ssh =None
        self.connect()

    def connect(self):
        self.connect_ssh = paramiko.SSHClient()
        self.connect_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.connect_ssh.connect('192.168.255.22', username='dg', password='passw0rd')

    def write_common(self, common):
        self.connect_ssh.exec_command(str(common))


if __name__ == '__main__':
    print('PyCharm')

