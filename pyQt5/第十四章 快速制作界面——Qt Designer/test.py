# 在test.py中进行逻辑代码构写

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from designer import Ui_Form

class Demo(QWidget,Ui_Form):
    def __init__(self):
        super(Demo,self).__init__()
        self.setupUi(self)
        self.text_edit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())