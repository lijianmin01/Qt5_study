'''
QToolButton是与工具操作相关的按钮，通常和QToolBar搭配使用。
QToolButton一般不用来显示文本，而显示图标QIcon
(关于QToolBar我们会在后续介绍QMainWindow的时候再详细讲解)。

不过在方法使用上，QToolButton跟QPushButton还是很像的：
'''

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QToolButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.test_button = QToolButton(self)  # 1
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('../QIconImg/button.png'))
        self.test_button.toggled.connect(self.button_state_func)
        self.test_button.isCheckable()
        self.test_button.setText("666")

    def button_state_func(self):
        print(self.test_button.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 请注意不能在QToolButton实例化的时候直接传入文本字符串，
因为该控件没有相应的初始化函数。也就是说这样做是错误的：
self.test_button = QToolButton('Test', self) 
如果要设置文本的话得通过setText()方法。
但是setText()方法和setIcon()方法都使用的话，只会显示图标。
"""



















