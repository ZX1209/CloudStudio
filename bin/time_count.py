# -*- coding: utf-8 -*-
# > https://blog.csdn.net/Kprogram/article/details/83623079
import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen

from PyQt5.QtCore import QCoreApplication, QTime, QTimer
from PyQt5.QtWidgets import QLCDNumber, QWidget, QPushButton, QVBoxLayout, QApplication


class CountClock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 窗口信息
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle("Count Clock")
        self.show()

        # 显示时间的元件
        self.lcd = QLCDNumber(self)
        # 设置为显示五个字符
        self.lcd.setDigitCount(8)

        # 放成一列
        vbox = QVBoxLayout()

        vbox.addWidget(self.lcd)

        self.setLayout(vbox)

        # 利用计时器每一秒打印时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        # 小时，分钟，秒钟
        self.h = 0
        self.m = 0
        self.s = 0

    def showTime(self):
        # 每秒自增

        self.s = self.s + 1
        if self.s == 60:
            self.s = 0
            self.m = self.m + 1
        if self.m == 60:
            self.m = 0
            self.h = self.h + 1
        # 创建时间字符串

        time = QTime(self.h, self.m, self.s)
        text = time.toString("hh:mm:ss")
        # # 打印时间（每隔一秒中间的' : '号会闪一下
        # if time.second() % 2 == 0:
        #     text = text[:2] + " " + text[3:]
        # print(text)
        self.lcd.display(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ex = CountClock()

    sys.exit(app.exec_())