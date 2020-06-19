"""
CSS可以让网页更美观，而QSS可以让我们的程序界面更加漂亮。(单押 ヘ(￣ω￣ヘ) ♪)

28.1 基本规则

每条QSS样式都由两部分组成：

1. 选择器，该部分指定要美化的控件

2. 声明，该部分指定要在控件上使用的属性和值

例如下面这条样式：

QPushButton是设置的选择器，而大括号里的color: red分别为属性和值。
这条样式会将所有的QPushButoon实例和它子类的文本颜色都设置为红色。
我们直接来示范一下看下效果
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.button1 = QPushButton('super class',self)
        self.button2 = SubButton()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.setLayout(self.h_layout)

class SubButton(QPushButton):
    def __init__(self):
        super(SubButton,self).__init__()
        self.setText('subclass')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    # qss = 'QPushButton {color: red}'
    qss = 'QPushButton {color: red; background-color: blue}'
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())

"""
当然也可以同时指定多个选择器：
    QPushButton, QLabel, QLineEdit {color: red}
以上写法等同于：
    QPushButton {color: red}
    QLabel {color: red}
    QLineEdit {color: red}

"""


