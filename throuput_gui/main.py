import paramiko


class SshConnect(object):

    def __init__(self):
        self.user = 'dg'
        self.host = '192.168.255.1'
        self.ssh = None

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname='192.168.255.1', port=23, username='root')
        





if __name__ == "__main__":
    SSH_Connection = SshConnect()
    SSH_Connection.connect()


