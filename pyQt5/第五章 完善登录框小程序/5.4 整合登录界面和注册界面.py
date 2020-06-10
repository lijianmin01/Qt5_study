'''
但是此时运行程序点击登录界面上的sign in按钮的话，
注册界面是显示不出来的，所以我们要将登录界面sign in按钮的clicked()信号
和一个自定义的用来显示注册界面的槽函数连接起来：
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit,\
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 100)

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()
        self.signin_page = SigninPage()     # 实例化SigninPage()

"""
https://zhuanlan.zhihu.com/p/75527971
"""

