import re
import sys

from ui.MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication


class DelayCaculate(QMainWindow):
    def __init__(self):
        super(DelayCaculate, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run()

    def run(self):
        self.promt_message()
        self.ui.pushButton.clicked.connect(self.detect_input)
        self.ui.lineEdit_2.returnPressed.connect(self.caculate_time)

    def promt_message(self):
        self.ui.lineEdit.setText('0x')
        self.ui.lineEdit_2.setText(chr(0x0075) + 's')
        self.ui.lineEdit_3.setText(chr(0x0075) + 's')
        self.ui.comboBox.addItems(['Forward', 'Delay'])
        self.resize(400, 250)
        # self.ui.lineEdit.setReadOnly(True)
        # self.ui.lineEdit.setStyleSheet("color: gray")

    def detect_input(self):
        try:
            if len(self.ui.lineEdit.text()) > 2:
                self.primary_caculate_time()
            elif len(self.ui.lineEdit_3.text()) > 2:
                self.time_to_hex()
        except Exception as e:
            print(e)

    def primary_caculate_time(self):
        try:
            primary_time_source = self.ui.lineEdit.text()
            primary_time_hex = primary_time_source[2:]
            primary_time_int = int(primary_time_hex, 16)
            self.ui.comboBox.addItems(['Forward', 'Delay'])
            if primary_time_int >= 6140:
                self.ui.comboBox.setCurrentText('Forward')
                primary_time = round(((65536 - primary_time_int) / 122.88), 2)
                self.ui.lineEdit_3.setText(str(primary_time) + chr(0x0075) + 's')
            else:
                self.ui.comboBox.setCurrentText('Delay')
                primary_time = round((primary_time_int / 122.88), 2)
                self.ui.lineEdit_3.setText(str(primary_time) + chr(0x0075) + 's')
        except Exception as e:
            print(e)

    def time_to_hex(self):
        fix_time = self.ui.comboBox.currentText()
        caculate_time = self.ui.lineEdit_3.text()[:-2]
        if fix_time == 'Forward':
            clock_times = 65536 - round(float(caculate_time) * 122.88)
            self.ui.lineEdit.setText(hex(int(clock_times)))
        elif fix_time == 'Delay':
            clock_times = round(float(caculate_time) * 122.88)
            self.ui.lineEdit.setText(hex(int(clock_times)))
        else:
            raise 'the input is not wanted'

    def caculate_time(self):
        self.primary_caculate_time()
        primary_date_hex = self.ui.lineEdit.text()
        if self.ui.checkBox.checkState():
            delta_time_str = self.ui.lineEdit_2.text()[:-2]
            date_time_int = float(delta_time_str) * 122.88
            adv_result = hex(int(int(primary_date_hex, 16) + date_time_int))
            self.ui.lineEdit_4.setText(adv_result)
        if self.ui.checkBox_2.checkState():
            delta_time_str = self.ui.lineEdit_2.text()[:-2]
            date_time_int = float(delta_time_str) * 122.88
            delay_result = hex(int(int(primary_date_hex, 16) - date_time_int))
            self.ui.lineEdit_4.setText(delay_result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = DelayCaculate()
    windows.show()
    sys.exit(app.exec_())
