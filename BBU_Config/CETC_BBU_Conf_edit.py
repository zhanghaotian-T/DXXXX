#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: CETC_BBU_Conf_edit.py
@time: 2021/12/23
"""

from Driver.xml_edit import BbuconfdbReconfig
from loguru import logger
import yaml


class CETCbbuEdite(BbuconfdbReconfig):

    def __init__(self, file_path, amf_ip='169.169.20.175', plmn='26203', service_band=79):
        BbuconfdbReconfig.__init__(self, file_path)
        self.amf_ip = amf_ip
        self.plmn = plmn
        self.services_band = service_band
        self.edit_dict = None

    def run(self):
        self.conf_get()

    def complete_frequency_edit_dict(self):
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

    def edit_dict_complete(self):
        BBU_config = yaml.load(open('BBUconfig.yaml', encoding='utf-8'), Loader=yaml.FullLoader)
        self.edit_dict = {'amf-ipv4-address': BBU_config['amf-ipv4-address'], 'band': BBU_config['band'],
                          'reference_frequency': BBU_config['reference_frequency'], 'plmn-id': BBU_config['plmn-id']}

        for single_message in []:
            if single_message in BBU_config.keys():
                self.edit_dict[single_message] = BBU_config[single_message]
        pass


    def dict_key_value_replace(self, replace_dict, replace_file):

        pass


if __name__ == '__main__':
    print('Python')
