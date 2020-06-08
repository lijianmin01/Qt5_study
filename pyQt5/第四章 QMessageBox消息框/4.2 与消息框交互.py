# 不同按钮，程序作出的反应不同

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.button = QPushButton('Click',self)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?',
                             QMessageBox.Yes | QMessageBox.No)

        if choice == QMessageBox.Yes:  # 2
            self.button.setText('Changed!')
        elif choice == QMessageBox.No:  # 4
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

"""
1. 当点击消息框上的某个按钮之后，会返回这个按钮，而这里将返回的按钮结果保存在choice中；

2. 若是按下了Yes，则改变按钮的文字；

3. 若是按下了No，则什么都不做。


"""

