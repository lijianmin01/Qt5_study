import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QLineEdit,\
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QMessageBox

class SigninPage(QDialog):
    def __init__(self):
        super(SigninPage,self).__init__()
        self.user_label = QLabel("Username: ",self)
        self.user_line = QLineEdit(self)
        self.pwd_label = QLabel("Password: ",self)
        self.pwd_line = QLineEdit(self)
        self.pwd2_label = QLabel("Password: ",self)
        self.pwd2_line = QLineEdit(self)

        self.sigin = QPushButton("注册",self)

        self.grid_layout = QGridLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()


    def layout_init(self):
        self.grid_layout.addWidget(self.user_label,0,0,1,1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd2_label, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd2_line, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.sigin,3,0,1,2)

        #self.all_v_layout.addLayout(self.grid_layout)
        self.setLayout(self.grid_layout)

    # 将Sign in按钮设为不可用(setEnabled(False))
    def lineedit_init(self):
        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)
        self.pwd2_line.textChanged.connect(self.check_input_func)

    def check_input_func(self):
        if self.sigin.text() and self.user_line.text() and self.pwd2_line.text():
            self.sigin.setEnabled(True)
        else:
            self.sigin.setEnabled(False)

    def pushbutton_init(self):
        self.sigin.setEnabled(False)
        self.sigin.clicked.connect(self.check_signin_func)


