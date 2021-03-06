#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Haotian
@file: chart.py
@time: 2021/10/11
"""
from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QDateTimeAxis, QLineSeries, QBarCategoryAxis
from PySide6.QtCore import Qt, QTimer, Slot, QDateTime, QPointF, QPoint, QDate
from PySide6.QtGui import QPen

from PySide6.QtCharts import QChart, QChartView
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow
import random
import sys


class Chart(QChart):
    def __init__(self, parent=None):
        super(Chart, self).__init__(QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
        self._timer = QTimer()
        self._series = QLineSeries(self)
        self._titles = list()
        self._axisX = QDateTimeAxis()
        self._axisX.setFormat('dd-MM-yyyy h:mm:ss')
        self._axisY = QValueAxis()
        self._step = 0
        self._x = 5
        self._y = 6

        self._timer.timeout.connect(self.handleTimeout)
        self._timer.setInterval(1000)

        green = QPen(Qt.red)
        green.setWidth(3)
        self._series.setPen(green)
        # self._series.append(self._x.toMSecsSinceEpoch(), self._y)
        self.addSeries(self._series)
        self.addAxis(self._axisX, Qt.AlignBottom)
        self.addAxis(self._axisY, Qt.AlignLeft)

        self.start_time = QDateTime.currentDateTime()
        self.end_time = self.start_time.addSecs(10)
        self._series.attachAxis(self._axisX)
        self._series.attachAxis(self._axisY)
        self._axisX.setTickCount(1)
        # self._axisX.setLabelsAngle(60)
        self._axisX.setRange(self.start_time, self.end_time)
        self._axisY.setRange(-5, 10)

        self._timer.start()

    @Slot()
    def handleTimeout(self):
        x = self.plotArea().width() / self._axisX.tickCount()
        # y = (self._axisX.max().toMSecsSinceEpoch() - self._axisX.min().toMSecsSinceEpoch()) / self._axisX.tickCount()
        y = 6
        self._x = y + 1
        # print(self._x.currentDateTime().toMSecsSinceEpoch())

        self._series.append(self._x, self._y)
        # self._series.append(1, 10)
        # self._series.append(QPoint(2, 5))
        # self._series.append(QPoint(3, 5))
        self.scroll(x, 0)
        if self._x == 100:
            self._timer.stop()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    window = QMainWindow()
    chart = Chart()
    chart.setTitle("Dynamic spline chart")
    chart.legend().hide()
    chart.setAnimationOptions(QChart.AllAnimations)
    chart_view = QChartView(chart)
    chart_view.setRenderHint(QPainter.Antialiasing)
    window.setCentralWidget(chart_view)
    window.resize(800, 800)
    window.show()

    sys.exit(a.exec())
