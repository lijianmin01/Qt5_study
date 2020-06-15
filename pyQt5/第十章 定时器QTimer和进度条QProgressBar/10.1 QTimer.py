"""
当我们要让程序定期去执行某函数的时候，QTimer就派上用场了，
比如一个游戏程序，
它通常会定期去调用一个函数来进行更新操作。
而进度条可以用来显示某项任务的进度，从而让用户界面更加友好。
"""

# 按钮被点击后，QLabel显示的数字会不断增加：

import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        # 首先实例化一个QLabel，并将文本设为0
        self.label = QLabel('0',self)
        self.label.setFont(QFont('Arial Black',0))
        # setAlignment(Qt.AlignCenter)可以让QLabel控件在窗口中居中显示，
        # 而之前我们是通过addStretch(int)方法来让一个控件在布局中居中的
        self.label.setAlignment(Qt.AlignCenter)

        self.step = 0

        # 实例化一个QTimer，并将timeout信号连接到自定义的槽函数update_func()上：
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)

        self.ss_button = QPushButton('Start', self)             # 4
        self.ss_button.clicked.connect(self.start_stop_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.ss_button)

        self.setLayout(self.v_layout)

    # 最后我们实例化一个QPushButton按钮来控制定时器的启动的停止，
    # 连接的自定义的槽函数如下：
    def start_stop_func(self):
        if not self.timer.isActive():
            self.ss_button.setText('Stop')
            self.timer.start(100)
        else:
            self.ss_button.setText('Start')
            self.timer.stop()

    # 每次调用该槽函数就会将step值加1，并且用QLabel显示当前值；
    # 随着timer改变，从而改变字体大小
    def update_func(self):
        self.step += 1
        self.label.setText(str(self.step))
        self.label.setFont(QFont('Arial Black', self.step))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())





















