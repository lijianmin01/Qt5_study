import sys
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(600,600)

        self.btn = QPushButton('Move',self)
        self.btn.setGeometry(0,0,100,100)

        self.animation = QPropertyAnimation(self.btn,b'geometry')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QRect(0,0,100,100))
        self.animation.setEndValue(QRect(300,300,300,300))
        # setEasingCurve()设置缓和曲线(即动画变化形式)
        self.animation.setEasingCurve(QEasingCurve.InBounce)
        # 调用setLoopCount()并传入-1来无限循环动画(传入正整数代表运行相应的次数，传入0不运行)
        self.animation.setLoopCount(-1)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())