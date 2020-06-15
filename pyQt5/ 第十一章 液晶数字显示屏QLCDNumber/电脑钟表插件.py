import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, \
    QVBoxLayout,QTextEdit,QLabel,QHBoxLayout
import time

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(400, 300)
        self.noted = QLabel(self)
        self.pics = QLabel(self)

        self.lcd_y_m_d = QLCDNumber(self)
        self.lcd_week = QLabel(self)
        self.lcd_time = QLCDNumber(self)

        self.header = QHBoxLayout()
        self.now_time = QHBoxLayout()
        self.all_h_layout = QVBoxLayout()

        self.layout_init()
        self.time_init()

    def layout_init(self):
        self.header.addWidget(self.pics)
        self.header.addWidget(self.noted)

        self.now_time.addWidget(self.lcd_y_m_d)
        self.now_time.addWidget(self.lcd_week)
        self.now_time.addWidget(self.lcd_time)

        self.all_h_layout.addLayout(self.header)
        self.all_h_layout.addLayout(self.now_time)

        self.setLayout(self.all_h_layout)

    def time_init(self):
        self.lcd_y_m_d.display(str(time.strftime("%Y-%m-%d",time.localtime())))
        self.lcd_time.display(str(time.strftime("%H:%M:%S",time.localtime())))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
不行，没实现
"""