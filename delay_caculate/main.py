import re
import sys

from ui.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QTextBrowser
from loguru import logger
import logging


class QPlainTextEditeLoggrt(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QTextBrowser(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.append(msg)
        # self.widget.appendHtml(msg)


class DelayCaculate(QMainWindow, QPlainTextEditeLoggrt):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.run()

    def run(self):
        self.promt_message()
        self.logger_handle_transfer()
        self.ui.pushButton.clicked.connect(self.detect_input)
        self.ui.lineEdit_2.returnPressed.connect(self.caculate_time)

    def logger_handle_transfer(self):
        _logger_text_broswer = QPlainTextEditeLoggrt(self)
        logger.add(_logger_text_broswer)
        self.ui.verticalLayout_4.addWidget(_logger_text_broswer.widget)

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
                logger.info(f'Current Delay Register input {self.ui.lineEdit.text()}')
            elif len(self.ui.lineEdit_3.text()) > 2:
                self.time_to_hex()
        except Exception as e:
            print(e)

    def primary_caculate_time(self):
        try:
            primary_time_source = self.ui.lineEdit.text()
            primary_time_hex = primary_time_source[2:]
            primary_time_int = int(primary_time_hex, 16)
            if primary_time_int >= 6140:
                self.ui.comboBox.setCurrentText('Forward')
                primary_time = round(((65536 - primary_time_int) / 122.88), 2)
                self.ui.lineEdit_3.setText(str(primary_time) + chr(0x0075) + 's')

            else:
                self.ui.comboBox.setCurrentText('Delay')
                primary_time = round((primary_time_int / 122.88), 2)
                self.ui.lineEdit_3.setText(str(primary_time) + chr(0x0075) + 's')
        except Exception as e:
            logger.info(e)

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
        primary_date_int = self.ui.lineEdit_3.text()[:-2]
        primary_date_state = self.ui.comboBox.currentText()
        if self.ui.checkBox.checkState():
            delta_time_str = self.ui.lineEdit_2.text()[:-2]
            if primary_date_state == 'Delay':
                if delta_time_str > primary_date_int:
                    caculate_time = float(delta_time_str) - float(primary_date_int)
                    clock_times = 65536 - round(float(caculate_time) * 122.88)
                    self.ui.lineEdit_4.setText(hex(int(clock_times)))
                if delta_time_str <= primary_date_int:
                    caculate_time = float(primary_date_int) - float(delta_time_str)
                    clock_times = round(float(caculate_time) * 122.88)
                    self.ui.lineEdit_4.setText(hex(int(clock_times)))
            elif primary_date_state == 'Forward':
                caculate_time = float(primary_date_int) + float(delta_time_str)
                clock_times = 65536 - round(float(caculate_time) * 122.88)
                self.ui.lineEdit_4.setText(hex(int(clock_times)))
        if self.ui.checkBox_2.checkState():
            delta_time_str = self.ui.lineEdit_2.text()[:-2]
            if primary_date_state == 'Forward':
                if delta_time_str > primary_date_int:
                    caculate_time = float(delta_time_str) - float(primary_date_int)
                    clock_times = round(float(caculate_time) * 122.88)
                    self.ui.lineEdit_5.setText(hex(int(clock_times)))
                else:
                    caculate_time = float(primary_date_int) - float(delta_time_str)
                    clock_times = 65536 - round(float(caculate_time) * 122.88)
                    self.ui.lineEdit_5.setText(hex(int(clock_times)))
            elif primary_date_state == 'Delay':
                caculate_time = float(primary_date_int) + float(delta_time_str)
                clock_times = round(float(caculate_time) * 122.88)
                self.ui.lineEdit_5.setText(hex(int(clock_times)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = DelayCaculate()
    windows.show()
    sys.exit(app.exec())
