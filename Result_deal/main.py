import re


class ResultDeal(object):
    def __init__(self):
        self.report = dict()
        self.aclr_l1 = list()
        self.aclr_ui = list()
        self.tx_mean_power = list()
        self.evm = list()
        self.ccdf = list()
        self.test_model = dict()
        self.channel = dict()
        self.aclr_l1_index_pre = 0
        self.aclr_ui_index_pre = 0

    def run(self):
        pass

    # def file_open(self):
    #     with open('Result_log/ResultsLog.txt') as f:
    #         self.report["ResultsLog"] = {}
    #         for index, line in enumerate(f):
    #             print(index)
    #             if 'Test Model' in line:
    #                 test_model = re.findall(r'LTE_ETM[0-9]_\w+', line)[0]
    #                 self.report['ResultsLog'][test_model] = self.test_model
    #                 self.aclr_l1 = list()
    #                 self.aclr_ui = list()
    #                 self.tx_mean_power = list()
    #                 self.evm = list()
    #                 self.ccdf = list()
    #             if "Channel#" in line:
    #                 channel = re.findall(r'[0-9]+', line)[0]
    #                 self.report['ResultsLog'][test_model][channel] = self.channel
    #                 self.aclr_l1 = list()
    #                 self.aclr_ui = list()
    #                 self.tx_mean_power = list()
    #                 self.evm = list()
    #                 self.ccdf = list()
    #             if "ACLR_EUTRA_L1" in line:
    #                 aclr_l1 = re.findall(r'[0-9]+.[0-9]+', line)[0]
    #                 self.aclr_l1.append(aclr_l1)
    #                 if (index - self.aclr_l1_index_pre) == 8:
    #                     aclr_l1_average = (float(self.aclr_l1[-1]) + float(self.aclr_l1[-2])) / 2
    #                     del self.aclr_l1[-2:]
    #                     self.aclr_l1.append(aclr_l1_average)
    #                 self.report['ResultsLog'][test_model][channel]['ACLR_EUTRA_L1'] = self.aclr_l1
    #                 self.aclr_l1_index_pre = index
    #             if 'ACLR_EUTRA_U1' in line:
    #                 aclr_u1 = re.findall(r'[0-9]+.[0-9]+', line)[0]
    #                 self.aclr_ui.append(aclr_u1)
    #                 if (index - self.aclr_ui_index_pre) == 8:
    #                     aclr_l1_average = (float(self.aclr_ui[-1]) + float(self.aclr_ui[-2])) / 2
    #                     del self.aclr_ui[-2:]
    #                     self.aclr_ui.append(aclr_l1_average)
    #                 self.report['ResultsLog'][test_model][channel]['ACLR_EUTRA_U1'] = self.aclr_ui
    #                 self.aclr_ui_index_pre = index
    #             if 'Tx Mean Power Average' in line:
    #                 if test_model == 'ETM1_1':
    #                     tx_reference_power = re.findall(r'[0-9]+.[0-9]+', line)
    #                     self.tx_mean_power.append(tx_reference_power)
    #                     self.report['ResultsLog'][test_model][channel]['TX Mean Power Average'] = self.tx_mean_power
    #             if 'EVM Average' in line:
    #                 evm = re.findall(r'[0-9]+.[0-9]+', line)
    #                 self.evm.append(evm)
    #                 self.report['ResultsLog'][test_model][channel]['EVM Average'] = self.tx_mean_power
    #             if 'CCDF Power Level at 0.1%' in line:
    #                 ccdf = re.findall(r'[0-9]+.[0-9]+', line)
    #                 self.ccdf.append(ccdf)
    #                 self.report['ResultsLog'][test_model][channel]['CCDF Power Level at 0.1%'] = self.ccdf
    #     return self.report

    def file_open(self):
        with open('Result_log/ResultsLog.txt') as f:
                self.report["ResultsLog"] = {}
                for index, line in enumerate(f):

                    pass

    def key_word_fil(self):
        pass

    def line_key_word(self, line):
        try:
            channel = re.findall(r'Channel#	\s*[0-9]*', line)
            alcr_l1 = re.findall(r'ACLR_EUTRA_L1:\s*[0-9]*.[0-9]*', line)
            aclr_ui = re.findall(r'ACLR_EUTRA_U1:\s*[0-9]*.[0-9]*', line)
            tx_mean_power = re.findall(r'Tx Mean Power Average\S*\s*[0-9]*.[0-9]*', line)
            evm = re.findall(r'')
            evm_average = 0
            ccdf = 0

        except Exception as e:
            return None


if __name__ == '__main__':
    a = ResultDeal()
    b = a.file_open()
    pass

