# QSS 作用范围.
app.setStyleSheet("QStackedWidget{background-color:yellow;}")

一.QMainWindow：
QMainWindow类提供一个带有菜单条，工具条和一个状态条的主应用程序窗口。主窗口通常提供一个大的中央窗口部件，以及周围菜单，工具条，和一个状态栏。QMainWindow窗口经常被继承，使得封装中央部件，菜单，工具条，状态栏等都变得很容易，当用户点击它的时候，相应的槽就会被调用。

二.QWidget
QWidet类是所有用户界面对象的基类，窗口部件是用户界面的一个基本单元，它从窗口系统接收鼠标，键盘和其他消息，并在屏幕上绘制自己。一个窗口部件可以被他的父窗口或者是其他窗口挡住一部分。

三.QDialog
QDialog类是对话框窗口的基类，对话框窗口主要用于短期任务和用户进行短期通讯的顶级窗口，QDialog可以是模态对话框或者是非模态对话框。QDialog支持扩展并带有返回值，他们可以带有默认值

1.Qt Creator提供的默认基类有QMainWindow、QWidget、QDialog这3种。
QMainWindow是带有菜单栏和工具栏的主窗口，
QDialog是各种对话框的基类，而这两者都是继承自QWidget。
QWidget的（新建Qt GUI应用时选择QWidget为基类）。不仅如此，其实所有的窗口部件都继承 自QWidget。

QWidget的构造函数有两个参数：“QWidget * parent =0”和“Qt::WindowFlags f = 0”。面一个参数是指父窗口部件，默认值为0，表明没有父窗口；后面一个参数是Qt::WindowFlags的枚举类型，分为窗口类型（窗口的样式）和窗口标志（更改 窗口的标题栏和边框），可以进行位或操作。

ui是一个指向界面类的指针，使用“ui->”就是用来访问这个界面类里面的控件。
Qt提供的一些常用的对话框类型：
QColorDialog（颜色对话框）、
QFileDialog（文件对话框）、
QFontDialog（字体对话框）、
QInputDialog（输入对话框）、
QMessageBox（消息对话框）、
QProgressDialog（进度对话框）、
QErrorMessage（错误信息对话框）
QPageSetupDialog（页面设置对话框）、
QPrintDialog（打印对话框）、
QPrintPreviewDialog（打印预览对话框）。
其他窗口部件
（1）QFrame类（带边框的部件的基类），其子类有
QLabel（标签部件，显示文本或者图片）、QLCDNumber（液晶数字显示效果）、 QStackedWidget（提供了一个部件栈，可以切换多个界面）、
QToolBox（列层叠窗口，在一个界面上达到类似抽屉的效果，可以切换页面）。
（2）按钮部件，QAbstractButton类是按钮部件的抽象基类，其子类有
QCheckBox（复选框，可以同时选择多项）、
QPushButton（标准按钮）、
QRadioButton（单选框按钮）、
QToolButton（工具按钮）。
（3）QLineEdit（行编辑器），可以实现设置显示模式、输入掩码、输入验证、自动补全的功能。
（4）QAbstractSpinBox（数值设定框）是一个抽象基类，其子类有
QDataTimeEdit（设定日期时间）、
QSpinBox（设定整数）、
QDoubleSpinBox（设定浮点数）。
（5）QAbstractSlider（滑块部件），其子类有
QScrollBar（多用在QScrollArea类中实现滚动区域）、
QSlider（多用在音量控制或多媒体播放进度等方面）、
QDial（刻度表盘）。
---------------------
作者：konsy_dong
来源：CSDN
原文：https://blog.csdn.net/sinat_36053757/article/details/70142070
版权声明：本文为博主原创文章，转载请附上博文链接！



statusBar
self.statusBar().showMessage('Ready')

setToolTip

addToolBar


QAction

exitAct = QAction(QIcon('exit.png'), '&Exit', self)
exitAct.setShortcut('Ctrl+Q')
exitAct.setStatusTip('Exit application')
exitAct.triggered.connect(qApp.quit)


self.menuBar & addMenu
menubar = self.menuBar()
fileMenu = menubar.addMenu('&File')
fileMenu.addAction(exitAct)

QMenu

menubar = self.menuBar()
fileMenu = menubar.addMenu('File')

impMenu = QMenu('Import', self)
impAct = QAction('Import mail', self)
impMenu.addAction(impAct)

newAct = QAction('New', self)

fileMenu.addAction(newAct)
fileMenu.addMenu(impMenu)

QMessageBox.question
reply = QMessageBox.question(self, 'Message',
    "Are you sure to quit?", QMessageBox.Yes |
    QMessageBox.No, QMessageBox.No)
我们创建了一个消息框，上面有俩按钮：Yes和No.第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
if reply == QtGui.QMessageBox.Yes:
    event.accept()
else:
    event.ignore()
这里判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否者就忽略关闭事件。


右键菜单
def contextMenuEvent(self, event):

       cmenu = QMenu(self)

       newAct = cmenu.addAction("New")
       opnAct = cmenu.addAction("Open")
       quitAct = cmenu.addAction("Quit")
       action = cmenu.exec_(self.mapToGlobal(event.pos()))

       if action == quitAct:
           qApp.quit()

# mini application
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

author: Jan Bodnar
website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

```

面对对象
```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
