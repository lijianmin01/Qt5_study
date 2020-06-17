"""
当在执行某些复杂且耗时的操作时，我们不能将该操作放在界面控制线程中(即UI线程，
就是app.exec_()所在的线程)，否则我们会发现界面停止响应(或卡顿)
"""
import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.count = 0

        self.button = QPushButton('Count',self)
        self.button.clicked.connect(self.count_func)
        self.label = QLabel('0',self)
        self.label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def count_func(self):
        while True:
            self.count +=1
            print(self.count)
            self.label.setText(str(self.count))
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
理想的情况应该是这样，当我们点击按钮时，程序就会无限计数，\
然后将文本设置为相应的数字。
但是这里的计数操作绝对耗时，而且它处在UI线程中(此时都是主线程)，
所以程序界面会停止响应，文本不会显示计数，而查看控制台会发现是有在计数的。

我们应该采用多线程，将复杂耗时的操作放在与界面控制不同的线程中，让两者独立开来。
"""




