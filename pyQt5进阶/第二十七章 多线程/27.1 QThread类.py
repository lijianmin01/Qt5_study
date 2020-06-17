# 要实现多线程，我们要先继承QThread类并重新实现其中的run()函数，
# 也就是说把耗时的操作放入run()函数中。

import sys
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        self.button = QPushButton('Count',self)
        self.button.clicked.connect(self.count_func)
        self.label = QLabel('0',self)
        self.label.setAlignment(Qt.AlignCenter)

        self.my_thread = MyThread()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def count_func(self):
        self.my_thread.start()


class MyThread(QThread):
    def __init__(self):
        super(MyThread,self).__init__()
        self.count = 0

    def run(self):
        while True:
            print(self.count)
            self.count+=1
            self.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())