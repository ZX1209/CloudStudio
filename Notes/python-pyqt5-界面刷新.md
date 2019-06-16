QT对界面的调整有很多种形式，如果发现界面样式不正常，通过缩放窗口，或者某项鼠标操作才正常，可能是你的窗口没有正常刷新。可以试试以下方法

1. update()函数，实质上是调用了repaint函数，但是不是同步的，就是repaint函数可能不会立即执行。调用多次update()可能只执行了一次repaint（）函数。
void QWidget::update()

2.就是直接调用repaint()函数，如果这个控件不是disable状态或者不是隐藏状态，它将直接调用paintEvent()函数。如果你需要立刻刷新，官方也建议之间是用repaint()函数。
void QWidget::repaint()


3.如果以上都不行，你也可以试试以下这个方法。showNormal（），它也许会有用。
void QWidget::showNormal()

4.使用resize（）函数。可以这样调用this->resize(this->size());
void resize(const QSize &)

5.终极大招为 adjust()函数，一般情况下直接使用这个函数，就能进行界面的实时调整
void QWidget::adjustSize()


一般以上几种方法总有一种适合你。祝你好远！
--------------------- 
作者：漫步繁华街 
来源：CSDN 
原文：https://blog.csdn.net/xiezhongyuan07/article/details/79924902 
版权声明：本文为博主原创文章，转载请附上博文链接！