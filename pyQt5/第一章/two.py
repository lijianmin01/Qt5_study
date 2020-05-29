import sys
from PyQt5.QtWidgets import QApplication,QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel()
    #label.setText("Hello World")

    """可以直接在字符串上加上html代码，修饰文本样式"""
    label.setText('<h1>Hello</h1><br><font color="red" size="30">World</font>')
    label.show()
    sys.exit(app.exec_())