import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QLabel, QVBoxLayout,QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        self.start_btn = QPushButton('Start',self)
        self.stop_and_continue_btn = QPushButton('Stop',self)
        self.clear_btn = QPushButton('Clear',self)

        self.label = QLabel('0',self)

        self.all_v_layout = QVBoxLayout()
        self.btn_layout = QHBoxLayout()

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)

        self.layout_init()
        self.btn_init()

    def layout_init(self):
        self.label.setAlignment(Qt.AlignCenter)
        self.all_v_layout.addWidget(self.label)

        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.stop_and_continue_btn)
        self.btn_layout.addWidget(self.clear_btn)

        self.all_v_layout.addLayout(self.btn_layout)

        self.setLayout(self.all_v_layout)

    def btn_init(self):
        self.start_btn.clicked.connect(self.start_btn_func)
        self.stop_and_continue_btn.clicked.connect(self.stop_and_continue_btn_func)
        self.clear_btn.clicked.connect(self.clear_btn_func)

    def start_btn_func(self):
        self.my_thread.is_run = True
        self.my_thread.start()

    def stop_and_continue_btn_func(self):
        if self.stop_and_continue_btn.text()=='Stop' and self.my_thread.is_run and self.my_thread.count!=0:
            self.my_thread.is_run = False
            self.stop_and_continue_btn.setText('Continue')
        elif not self.my_thread.is_run and self.stop_and_continue_btn.text()=='Continue':
            self.my_thread.is_run = True
            self.stop_and_continue_btn.setText('Stop')
            self.my_thread.start()
        else:
            pass

    def clear_btn_func(self):
        self.my_thread.is_run = False
        self.stop_and_continue_btn.setText('Stop')
        self.label.setText('0')
        self.my_thread.count = 0

    def set_label_func(self,num):
        self.label.setText(num)

class MyThread(QThread):
    my_signal = pyqtSignal(str)
    is_run =True

    def __init__(self):
        super(MyThread,self).__init__()
        self.count = 0

    def run(self):
        while self.is_run:
            self.count+=1
            self.my_signal.emit(str(self.count))
            self.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())