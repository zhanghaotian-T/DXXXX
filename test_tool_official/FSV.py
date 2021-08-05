import time

import pyvisa


class Fsv(object):
    def __init__(self):
        self.resource_manage = pyvisa.ResourceManager()
        self.instrument = None

    def _connection(self, ip_port):
        if not self.instrument:
            self.instrument = self.resource_manage.open_resource(ip_port)

    def connection(self, ip_port):
        self._connection(ip_port)
        return self.instrument

    def write(self, command):
        self.instrument.write(command)
        time.sleep(0.5)

    def set_frequency(self, frequency):
        self.write('')
        pass


if __name__ == '__main__':
    a = Fsv()
    instrument = a.connection('192.168.255.11')


