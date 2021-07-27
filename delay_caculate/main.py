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
        self.ui.pushButton.clicked.connect(self.primary_caculate_time)
        self.ui.lineEdit_2.returnPressed.connect(self.caculate_time)

    def promt_message(self):
        self.ui.lineEdit.setText('0x507')
        self.ui.lineEdit_2.setText(chr(0x0075) + 's')
        # self.ui.lineEdit.setReadOnly(True)
        # self.ui.lineEdit.setStyleSheet("color: gray")

    def primary_caculate_time(self):
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

    def caculate_time(self):
        primary_date_hex = self.ui.lineEdit.text()[2:]
        if self.ui.checkBox.checkState():
            delta_time_int = self.ui.lineEdit_2.text()[:-2]
            date_time_hex = float(delta_time_int) * 122.88
            adv_result = hex(int(primary_date_hex, 16) - int(date_time_hex, 16))
            self.ui.lineEdit_4.setText(adv_result)
        if self.ui.checkBox_2.checkState():
            delta_time_int = self.ui.lineEdit_2.text()[:-2]
            date_time_hex = float(delta_time_int) * 122.88
            delay_result = hex(primary_date_hex + date_time_hex)
            self.ui.lineEdit_4.setText(delay_result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = DelayCaculate()
    windows.show()
    sys.exit(app.exec_())
