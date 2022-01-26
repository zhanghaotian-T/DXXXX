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
        if self.edit_dict['services:band'] == 41:
            ssb_offset = 6
            abs_ssb_freq = 504990
            abs_point_a = 503172
            pdcch_config_sib = 160
            msg_lenghth = 400
        elif self.edit_dict['services:band'] == 78:
            ssb_offset = 4
            abs_ssb_freq = 630720
            abs_point_a = 630164
            pdcch_config_sib = 64
            msg_lenghth = 400
        elif self.edit_dict['services:band'] == 79:
            ssb_offset = 6
            abs_ssb_freq = 721824
            abs_point_a = 720060
            pdcch_config_sib = 64
            msg_lenghth = 150
        else:
            ssb_offset = 6
            abs_ssb_freq = 504990
            abs_point_a = 503172
            pdcch_config_sib = 160
            msg_lenghth = 400
            logger.info('The service: {} is error'.format(self.edit_dict['band']))
        key_message_list = ['services:ssb-frequency',
                            'services:pdcch-config-sib1',
                            'services:ssb-subcarrier-offset',
                            'services:absolute-frequency-ssb',
                            'services:absolute-frequency-point-a',
                            'services:ref-freq-csi-rs',
                            'services:bo-report-msg-length',
                            'services:freq-band-indicator']
        for message in key_message_list:
            if message in self.edit_dict.keys():
                continue
            else:
                if message == 'services:ssb-frequency':
                    self.edit_dict['services:ssb-frequency'] = abs_ssb_freq
                elif message == 'services:absolute-frequency-ssb':
                    self.edit_dict['services:absolute-frequency-ssb'] = abs_ssb_freq
                elif message == 'services:ref-freq-csi-rs':
                    self.edit_dict['services:ref-freq-csi-rs'] = abs_ssb_freq
                elif message == 'services:pdcch-config-sib1':
                    self.edit_dict['services:pdcch-config-sib1'] = pdcch_config_sib
                elif message == 'services:ssb-subcarrier-offset':
                    self.edit_dict['services:ssb-subcarrier-offset'] = ssb_offset
                elif message == 'services:absolute-frequency-point-a':
                    self.edit_dict['services:absolute-frequency-point-a'] = abs_point_a
                elif message == 'services:bo-report-msg-length':
                    self.edit_dict['services:bo-report-msg-length'] = msg_lenghth
                elif message == 'services:freq-band-indicator':
                    self.edit_dict['services:freq-band-indicator'] = self.edit_dict['services:band']
                else:
                    logger.info('The key of config yaml is error, please check the config file')

    def edit_dict_complete(self):
        BBU_config = yaml.load(open('../BBUconfig.yaml', encoding='utf-8'), Loader=yaml.FullLoader)
        for key_message in BBU_config.keys():
            self.edit_dict[key_message] = BBU_config[key_message]
        self.complete_frequency_edit_dict()

    def dict_key_value_replace(self):
        for key_world in self.edit_dict.keys():
            self.conf_replace(key_world, str(self.edit_dict[key_world]))

    def xml_save(self):
        self.save_xml()


if __name__ == '__main__':
    a = CETCbbuEdite('../BBUconfdb/confdb.xml')
    a.run()
