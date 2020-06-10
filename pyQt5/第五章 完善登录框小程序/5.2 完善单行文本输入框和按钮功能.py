import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit,\
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

# 在程序的最开始处定义一个全局变量USER_PWD
USER_PWD = {
        'la_vie': 'password'
    }
'''
该字典的键'la_vie'就是当作账号，
值‘password’就当作密码(之后复杂的程序会使用数据库，
这里就先简单定义一个全局变量来使用)。
'''

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
        self.lineedit_init()
        self.pushbutton_init()

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

    #对输入框功能进行完善
    def lineedit_init(self):
        self.user_line.setPlaceholderText("Please enter your username")
        self.pwd_line.setPlaceholderText('Please enter your password')

        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.user_line.text() and self.pwd_line.text():
            self.login_button.setEnabled(True)
        else:
            self.login_button.setEnabled(False)

    #如果账号框和密码框都有文本(通过text()方法获取输入框文本)，
    # 那就使登录按钮可用(setEnabled(True))，否则登录按钮不可用。
    def pushbutton_init(self):
        # 当文本是空的时候，登录按钮没办法使用
        self.login_button.setEnabled(False)
        # 所以我们将登录按钮的clicked信号和一个用于检查账号密码是否正确的自定义槽函数连接起来：
        self.login_button.clicked.connect(self.check_login_func)

    # 定义检查账号密码的槽函数：
    def check_login_func(self):
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            QMessageBox.information(self, 'Information', 'Log in Successfully!')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')

        self.user_line.clear()
        self.pwd_line.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())















