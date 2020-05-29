#信号都为clicked，然后再多定义几个槽函数：

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(300,300)
        self.setWindowTitle('demo')
        self.button = QPushButton('Start',self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)
        self.button.clicked.connect(self.change_window_title)

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)
        return None
    def change_window_size(self):
        print("change_window_size")
        self.resize(500,500)
        self.button.clicked.disconnect(self.change_window_size)
        return None

    def change_window_title(self):
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())