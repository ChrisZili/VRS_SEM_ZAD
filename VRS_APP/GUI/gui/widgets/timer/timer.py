import time

from PySide6.QtWidgets import QWidget
from PyQt6 import QtCore
from PySide6.QtWidgets import QLabel


class Timer(QLabel):
    def __init__(self,action= None):
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        super().__init__(self.time.toString('hh:mm:ss'))
        self.action = action

        self.setStyleSheet(
            "color: #8a95aa; font-size: 30px; font-weight: bold;")

        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(1000)

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.setText(self.time.toString('hh:mm:ss'))
        # if int(self.time.toString('hh:mm:ss').split(":")[1]) == 10 and int(self.time.toString('hh:mm:ss').split(":")[2]) == 0:
        #     self.action()


    def reset(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.setText(self.time.toString('hh:mm:ss'))

    def stop(self):
        self.timer.stop()
