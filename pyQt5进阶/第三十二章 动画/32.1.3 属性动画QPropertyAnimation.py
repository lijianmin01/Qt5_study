# 那如果要改变位置呢？其实只用把size属性换成pos属性，然后用QPoint替换QSize就可以了。

import sys
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(600,600)

        self.btn = QPushButton('Move',self)
        self.btn.resize(100,100)

        self.animation = QPropertyAnimation(self.btn,b'pos')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QPoint(0,0))
        self.animation.setEndValue(QPoint(500,500))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())