#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: CETC_BBU_Conf_edit.py
@time: 2021/12/23
"""

from Driver.xml_edit import BbuconfdbReconfig
from loguru import logger


class CETCbbuEdite(BbuconfdbReconfig):

    def __init__(self, file_path, amf_ip='169.169.20.175', plmn='26203', service_band=79):
        BbuconfdbReconfig.__init__(self, file_path)
        self.amf_ip = amf_ip
        self.plmn = plmn
        self.services_band = service_band
        self.edit_dict = None

    def run(self):
        self.conf_get()

    def complete_frequency_edit_dict(self, ssb_offset=None, abs_ssb_freq=None, abs_point_a=None, pdcch_config_sib=None):
        freq_edite_dict = {}
        if self.services_band == 41:
            ssb_offset = 6
            abs_ssb_freq = 504990
            abs_point_a = 503172
        elif self.services_band == 78:
            ssb_offset = 4
            abs_ssb_freq = 630720
            abs_point_a = 630164
            pdcch_config_sib = 64
        elif self.services_band == 79:
            ssb_offset = 6
            abs_ssb_freq = 721824
            abs_point_a = 720060
            pdcch_config_sib = 64
        else:
            logger.info('The service: {} is error'.format(self.services_band))

    def dict_key_value_replace(self, replace_dict, key_world, replace_value):
        pass

if __name__ == '__main__':
    print('Python')
