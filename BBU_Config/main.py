import sys
import logging

from functools import partial
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2 import QtCore


class Obj(QtCore.QObject, logging.Handler):
    sig = QtCore.Signal(dict)

    def __init__(self):
        QtCore.QObject.__init__(self)
        logging.Handler.__init__(self)

    def emit(self, logRecord):
        # This is intended to be logging.Handler 
        # implementation of emit, not the QObject one
        self.sig.emit({"a":123, "b":321})


if __name__ == "__main__":
    app = QApplication(sys.argv)

    handler = Obj()

    logger = logging.getLogger(name='test')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    w = QWidget()
    b = QPushButton(w)
    b.clicked.connect(partial(logger.debug, "ASD"))
    w.show()

    app.exec_()