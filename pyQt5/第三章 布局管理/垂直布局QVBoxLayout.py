'''
垂直布局QVBoxLayout
该布局方式就是将各个控件按从上到下垂直的方式摆放
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout

class Demo(QWidget):

    def __init__(self):
        super(Demo,self).__init__()
        self.user_label = QLabel('Usename: ',self)
        self.pwd_label = QLabel('password: ',self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.user_label)
        self.v_layout.addWidget(self.pwd_label)

        self.setLayout(self.v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 实例化一个垂直布局管理器QVBoxLayout；

2-3. 通过调用addWidget()方法来将控件一个个添加到垂直布局中，最先添加的出现在最上方；

4. 将self.v_layout设为整个窗口的最终布局方式。
"""