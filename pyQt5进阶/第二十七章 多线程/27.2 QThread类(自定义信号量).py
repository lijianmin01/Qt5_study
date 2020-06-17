# 用信号来时刻传递count变量的值给UI线程中的label。
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        self.button = QPushButton('Count',self)
        self.button.clicked.connect(self.count_func)
        self.label = QLabel('0',self)
        self.label.setAlignment(Qt.AlignCenter)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def count_func(self):
        self.my_thread.start()

    def set_label_func(self,num):
        self.label.setText(num)

class MyThread(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread,self).__init__()
        self.count = 0

    def run(self):
        while True:
            print(self.count)
            self.count+=1
            self.my_signal.emit(str(self.count))
            self.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())




