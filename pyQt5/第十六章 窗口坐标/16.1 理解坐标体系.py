"""
左上角都为原点(0, 0)，向右为x轴正向，向下为y轴正向。

    x()——得到窗口左上角在显示屏屏幕上的x坐标；
    y()——得到窗口左上角在显示屏屏幕上的y坐标；
    pos()——得到窗口左上角在显示屏屏幕上的x和y坐标，类型为QPoint()；
    geometry().x()——的到客户区左上角在显示屏屏幕上的x坐标；
    geometry().y()——的到客户区左上角在显示屏屏幕上的y坐标；
    geometry()——的到客户区左上角在显示屏屏幕上的x和y坐标，以及客户区的宽度和长度，类型为QRect()；width()——得到客户区的宽度；
    height()——得到客户区的长度；geometry().width()——得到客户区的宽度；geometry().height()——得到客户区的长度；
    frameGeometry().width()——得到窗口的宽度；
    frameGeometry().height()——得到窗口的长度；

        frameGeometry().x()——即x()，得到窗口左上角在显示屏屏幕上的x坐标；
        frameGeometry().y()——即y()，得到窗口左上角在显示屏屏幕上的y坐标；
        frameGeometry()——即pos()，得到窗口左上角在显示屏屏幕上的x和y坐标，以及窗口的宽度和长度，类型为QRect()；
"""

# QWidget窗口，并调用各个方法打印下它的坐标

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(200, 200)                    # 1
    widget.move(100, 100)                      # 2
    # widget.setGeometry(100, 100, 200, 200)   # 3
    widget.show()

    print('-----------------x(), y(), pos()-----------------')
    print(widget.x())
    print(widget.y())
    print(widget.pos())

    print('-----------------width(), height()-----------------')
    print(widget.width())
    print(widget.height())

    print('-----------------geometry().x(), geometry.y(), geometry()-----------------')
    print(widget.geometry().x())
    print(widget.geometry().y())
    print(widget.geometry())

    print('-----------------geometry.width(), geometry().height()-----------------')
    print(widget.geometry().width())
    print(widget.geometry().height())

    print('-----------------frameGeometry().x(), frameGeometry().y(), frameGeometry(), '
          'frameGeometry().width(), frameGeometry().height()-----------------')
    print(widget.frameGeometry().x())
    print(widget.frameGeometry().y())
    print(widget.frameGeometry())
    print(widget.frameGeometry().width())
    print(widget.frameGeometry().height())

    sys.exit(app.exec_())