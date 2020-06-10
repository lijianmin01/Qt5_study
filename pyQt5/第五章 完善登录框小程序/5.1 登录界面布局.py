import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit,\
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

# 完成登录界面

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(300,100)

        self.user_label = QLabel('Username: ',self)
        self.pwd_label = QLabel('Password: ',self)
        self.user_line= QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in',self)
        self.signin_button =QPushButton('Sign in',self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()

    def layout_init(self):
        self.grid_layout.addWidget(self.user_label,0,0,1,1)
        self.grid_layout.addWidget(self.user_line,0,1,1,1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)

        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)

        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
把布局管理专门放在了一个函数中layout_init()，然后只用在初始化函数中
加上layout_init()中就行。把对不同控件的操作分开来放在相应的函数中，这样写不仅可以让代码更加清晰明了，也方便日后维护。
"""













