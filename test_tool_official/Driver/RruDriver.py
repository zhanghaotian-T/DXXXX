#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :RruDriver.py
# @Time      :2021/9/14 22:12
# @Author    :Haotian

from bci import Bci
from loguru import logger


class RruDriver(Bci):

    def adv9528_status(self, commonlist):
        try:
            for common in commonlist:
                adv9528_return = self.query_common(common)[-2:]
                if adv9528_return != '7a':
                    logger.warning('The Adv9528 Statues Error')
                else:
                    return True
        except Exception as error:
            logger.info(error)

    def idt_staues(self, common_list):
        idt_status = True
        try:
            for common in common_list:
                sub_idt_return = self.query_common(common)[-1:]
                if sub_idt_return == 3:
                    idt_status_sub = True
                else:
                    idt_status_sub = False
                idt_status = idt_status or idt_status_sub
            return idt_status
        except Exception as error:
            logger.info('The idt check code is Fail')

    def carries_config(self, commom_list):
        try:
            for commom in commom_list:
                self.send_common(commom, wait_time=6)
        except Exception as erro:
            logger.info('The carrier set code Fail')


if __name__ == "__main__":
    run_code = 0
