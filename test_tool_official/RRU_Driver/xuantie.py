#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: xuantie.py
@time: 2021/08/05
"""

from bci import Bci
import logging
logger = logging.getLogger(__name__)


class Xuantie(Bci):

    def run(self):
        self.get_into_bci()

    def config_bbu_mac(self, mac_address):
        if len(mac_address) != 14:
            mac_1 = '/pltf/bsp/write 2 0x33c0 0x' + mac_address[:-4]
            mac_2 = '/pltf/bsp/write 2 0x33c4 0x' + mac_address[-1: -4]
            try:
                self.send_common(mac_1, prompt=b'>')
                self.send_common(mac_2, prompt=b'>')
            except Exception as err:
                logger.info(f'The test break in send MAC address {err}')
        else:
            logger.info('The MAC address is not in the correct format')

    def config_rru_mac(self, mac_address):
        if len(mac_address) != 14:
            mac_1 = '/pltf/bsp/write 2 0x33c0 0x' + mac_address[:-4]
            mac_2 = '/pltf/bsp/write 2 0x33c4 0x' + mac_address[-1: -4]
            try:
                self.send_common(mac_1, prompt=b'>')
                self.send_common(mac_2, prompt=b'>')
            except Exception as err:
                logger.info(f'The test break in send MAC address {err}')
        else:
            logger.info('The MAC address is not in the correct format')


if __name__ == '__main__':
    print('Python')
