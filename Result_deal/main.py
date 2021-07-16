import re
import pandas as pd
import os


class ResultDeal(object):
    def __init__(self):
        self.report = list()
        self.ant = 'ANT_1'
        self.test_model = None
        self.channel = None
        self.aclr_l1_pre = 0
        self.aclr_u1_pre = 0
        self.sn = None

    def run(self):
        file_path_list = self.file_ergodic()
        for file_path in file_path_list:
            self.file_open(file_path)
        print(file_path_list)
        self.save_report_log(self.report)

    def file_open(self, file_path):
        print(file_path)
        self.sn = re.findall(r'\\.*.txt', file_path)[0][1: -4]
        with open(file_path, encoding='UTF-8', errors='replace') as f:
            for index, line in enumerate(f):
                print(line)
                if 'Test Model' in line:
                    self.test_model = re.findall(r'LTE_ETM[0-9]_\w+', line)[0]
                if "Channel#" in line:
                    self.channel = re.findall(r'[0-9]+', line)[0]
                if ("ACLR_EUTRA_L1" in line) and (index - self.aclr_l1_pre != 8):
                    aclr_l1 = re.findall(r'[0-9]+.[0-9]+', line)[0]
                    self.report.append(
                        self.sn + ';' + self.ant + ';' + self.test_model + ';' + self.channel + ';' + 'ACLR_L1;' + aclr_l1)
                    self.aclr_l1_pre = index
                if ('ACLR_EUTRA_U1' in line) and (index - self.aclr_u1_pre != 8):
                    aclr_u1 = re.findall(r'[0-9]+.[0-9]+', line)[0]
                    self.report.append(
                        self.sn + ';' + self.ant + ';' + self.test_model + ';' + self.channel + ';' + 'ACLR_U1;' + aclr_u1)
                    self.aclr_u1_pre = index
                if ('Tx Mean Power Average' in line) and (self.test_model == 'LTE_ETM1_1'):
                    tx_mean_power = re.findall(r'[0-9]+.[0-9]+', line)[0]
                    self.report.append(
                        self.sn + ';' + self.ant + ';' + self.test_model + ';' + self.channel + ';' + 'TX_MEAN_POWER;' + tx_mean_power)
                if 'EVM Average' in line:
                    evm = re.findall(r'[0-9]+.[0-9]+', line)[0]
                    self.report.append(
                        self.sn + ';' + self.ant + ';' + self.test_model + ';' + self.channel + ';' + 'EVM;' + evm)
                if 'CCDF Power Level at 0.1%' in line:
                    ccdf = re.findall(r'[0-9]+.[0-9]+', line)[1]
                    self.report.append(
                        self.sn + ';' + self.ant + ';' + self.test_model + ';' + self.channel + ';' + 'CCDF 0.1%;' + ccdf)
                if 'END OF LTE Tx MODULATION RESULTS' in line:
                    self.ant = 'ANT_2'
        self.ant = "ANT_1"
        f.close()
        return self.report

    def save_report_log(self, result_list: list):
        print(result_list)
        result_list_dataframe = [x.split(';') for x in result_list]
        final_result = pd.DataFrame(result_list_dataframe,
                                    columns=['SN', 'ANT', 'Test_Model', 'Frequency', 'Test_Case', 'Result'])
        if not os.path.exists(r'Report'):
            os.makedirs(r'Report')
            final_result.to_csv(r'Report/Result_Report.csv', encoding='utf-8')
            print(final_result)
        else:
            final_result.to_csv(r'\Report\Result_Report.csv')
            print(final_result)
            
    def file_ergodic(self):
        file_path_main = 'Result_log'
        path_list = list()
        for i in os.listdir(file_path_main):
            file_path = os.path.join('Result_log', i)
            path_list.append(file_path)
        return path_list


if __name__ == '__main__':
    a = ResultDeal()
    a.run()
    input()