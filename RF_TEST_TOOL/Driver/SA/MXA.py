import pyvisa


class Mxa(object):
    def __init__(self):
        self.resource_manage = pyvisa.ResourceManager()
        self.instrument = None

    def connection(self, ip_port):
        self.instrument = self.resource_manage.open_resource(ip_port)

    def Opreating_band_unwanted_emission(self):
        pass
