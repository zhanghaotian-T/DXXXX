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

    def __init__(self, file_path):
        BbuconfdbReconfig.__init__(self, file_path)
        self.file_path = file_path
        self.edit_dict = dict()

    def run(self):
        self.conf_get()
        self.edit_dict_complete()
        self.dict_key_value_replace()
        self.xml_save()

    def complete_frequency_edit_dict(self):

        if self.edit_dict['band'] == 41:
            ssb_offset = 6
            abs_ssb_freq = 504990
            abs_point_a = 503172
            pdcch_config_sib = 160
        elif self.edit_dict['band'] == 78:
            ssb_offset = 4
            abs_ssb_freq = 630720
            abs_point_a = 630164
            pdcch_config_sib = 64
        elif self.edit_dict['band'] == 79:
            ssb_offset = 6
            abs_ssb_freq = 721824
            abs_point_a = 720060
            pdcch_config_sib = 64
        else:
            ssb_offset = 6
            abs_ssb_freq = 504990
            abs_point_a = 503172
            pdcch_config_sib = 64
            logger.info('The service: {} is error'.format(self.edit_dict['band']))
        key_message_list = ['ssb-frequency', 'ref-frequency-csi-rs', 'pdcch-config-sib1', 'ssb-subcarrier-offset', 'absolute-frequency-point-a']
        for message in key_message_list:
            if message in self.edit_dict.keys():
                continue
            else:
                if message == 'ssb-frequency':
                    self.edit_dict['ssb-frequency'] = abs_ssb_freq
                elif message == 'ref-frequency-csi-rs':
                    self.edit_dict['ref-frequency-csi-rs'] = abs_ssb_freq
                elif message == 'pdcch-config-sib1':
                    self.edit_dict['pdcch-config-sib1'] = pdcch_config_sib
                elif message == 'ssb-subcarrier-offset':
                    self.edit_dict['ssb-subcarrier-offset'] = ssb_offset
                elif message == 'absolute-frequency-point-a':
                    self.edit_dict['absolute-frequency-point-a'] = abs_point_a
                elif message == 'absolute-frequency-ssb':
                    self.edit_dict['absolute-frequency-ssb'] = abs_ssb_freq
                else:
                    logger.info('The key of config yaml is error, please check the config file')

    def edit_dict_complete(self):
        BBU_config = yaml.load(open('BBUconfig.yaml', encoding='utf-8'), Loader=yaml.FullLoader)
        for key_message in BBU_config.keys():
            self.edit_dict[key_message] = BBU_config[key_message]
        self.complete_frequency_edit_dict()

    def dict_key_value_replace(self):
        for key_world in self.edit_dict.keys():
            self.conf_replace(key_world, str(self.edit_dict[key_world]))

    def xml_save(self):
        with open(self.file_path, 'wb') as file:
            self.soup.encode(formatter=None)
            file.write(self.soup.prettify('utf-8'))


if __name__ == '__main__':
    a = CETCbbuEdite('./BBUconfdb/confdb.xml')
    a.run()
