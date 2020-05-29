"""
QPushButton还有两个信号是pressed和released，这两个信号解释如下：

pressed: 当鼠标在button上并点击左键的时候，触发信号 。
released: 当鼠标左键被释放的时候触发信号。
所以其实pressed和released两个连起来就是一个完整的clicked
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.button=QPushButton('按住',self)
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text()=='按住':
            self.button.setText("松开")
        else:
            self.button.setText("按住")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo =Demo()
    demo.show()
    sys.exit(app.exec_())