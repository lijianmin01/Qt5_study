# 自定义信号

#注意这里将QPushButton换成了QLabel来讲解：​​​

"""

1. 需要先导入pyqtSignal；

2. 实例化一个自定义的信号；

3. 将自定义的信号连接到自定义的槽函数上；

4. mousePressEvent()方法是许多控件自带的，这里来自于QWidget。该方法用来监测鼠标是否有按下。现在鼠标若被按下，则会发出自定义的信号。
"""

import sys
from PyQt5.QtCore import pyqtSignal                             # 1
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Demo(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super(Demo,self).__init__()
        self.label = QLabel('Hello World~',self)
        self.my_signal.connect(self.change_text)

    def change_text(self):
        if self.label.text() =='Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

'''小结
1. 可以将信号和槽视作裁片鸣枪与选手开跑，信号发出，则相应连接的槽函数启动；

2. 单个信号可以连接单个槽；单个信号可以连接多个槽；多个信号可以连接单个槽；信号可以与信号连接；也可以自定义信号；

3. mousePressEvent()方法是许多控件自带的方法，用来监测鼠标是否被按下。​
'''