# 改变大小、颜色或位置是动画中的常见操作，
# 而QPropertyAnimation类可以修改控件的属性值，从而帮助我们实现这些动画效果

import sys
from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(600,600)

        self.btn = QPushButton('Bigger',self)
        self.btn.resize(100,100)

        self.animation = QPropertyAnimation(self.btn,b'size')
        # 调用setDuration()方法设置动画持续时间，这里的6000代表持续6秒
        self.animation.setDuration(6000)
        # 开始大小
        self.animation.setStartValue(QSize(100,100))
        # 最终大小
        self.animation.setEndValue(QSize(600,600))
        """
        这里传入的参数必须为QVariant类型(可以把QVariant理解为Qt中常见的数据类型)，
        该类型包括int，float，double，QColor，QLine，QLineF，QPoint，QPointF，
        QRect，QRectF，QSize和QSizeF等。
        """

        # 调用start()方法开始动画
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())






