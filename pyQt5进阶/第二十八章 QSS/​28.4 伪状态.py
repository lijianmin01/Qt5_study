import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button1 = QPushButton('button1', self)
        self.button2 = QPushButton('button2', self)
        self.button2.setProperty('name', 'btn2')

        my_list = ['A', 'B', 'C', 'D']
        self.combo = QComboBox(self)
        self.combo.addItems(my_list)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.combo)
        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = """
          QPushButton:hover {background-color: red}                     
          QPushButton[name='btn2']:pressed {background-color: blue}
          QComboBox::drop-down:hover {background-color: green}
          QComboBox::drop-down:!hover {background-color: yellow}
          """
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())

"""
我们知道如果在if判断语句中加个感叹号!就表示相反(否)，那我们也可以在伪状态前加上这个感叹号!来表示相反状态。比如：

QPushButton:!hover {background-color: red}
"""