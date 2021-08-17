import dgautolibs.utils
from bci import Bci


class TestOfficial(Bci):
    def run(self):
        pass


if __name__ == '__main__':
    tn = TestOfficial(host='192.168.255.11', user='dg', password='passw0rd')
    tn.connect()



