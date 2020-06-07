"""
上面的代码是将两个QLabel用垂直布局方式摆放，将两个QLineEdit也用垂直布局方式摆放，
最后用一个水平布局管理来摆放着两个垂直布局管理器。那换种思路，
可以把QLabel和QLineEdit用水平布局方式摆放：
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QLabel, QLineEdit, QPushButton,QHBoxLayout, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        self.user_label = QLabel("Username: ",self)
        self.pwd_label = QLabel("Password: ",self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)

        self.login_button = QPushButton("Login in",self)
        self.sigin_button = QPushButton("Sign in",self)

        self.user_layout = QHBoxLayout()
        self.pwd_layout = QHBoxLayout()
        self.btn_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.user_layout.addWidget(self.user_label)
        self.user_layout.addWidget(self.user_line)
        self.pwd_layout.addWidget(self.pwd_label)
        self.pwd_layout.addWidget(self.pwd_line)
        self.btn_layout.addWidget(self.login_button)
        self.btn_layout.addWidget(self.sigin_button)

        self.all_v_layout.addLayout(self.user_layout)
        self.all_v_layout.addLayout(self.pwd_layout)
        self.all_v_layout.addLayout(self.btn_layout)

        self.setLayout(self.all_v_layout)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())