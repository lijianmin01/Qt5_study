"""
2.1 通过按钮来改变文本(一个信号连接一个槽)
很多程序上是有“开始”按钮的，按下去后按钮上的文本就变成了“停止”。
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.button =QPushButton('Start',self)
        self.button.clicked.connect(self.change_text)

    def change_text(self):
        if self.button.text()=='Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

    # def change_text(self):
    #     print("change text")
    #     self.button.setText('Stop')
    #     self.button.clicked.disconnect(self.change_text)

    # def change_text_cnt(self):
    #     print("change text")
    #     if self.button.text()=='Stop':
    #         self.button.setText('Start')
    #         self.button.clicked.connect(self.change_text_cnt)
    #     elif self.button.text()=='Start':
    #         self.button.setText('Stop')
    #         self.button.clicked.connect(self.change_text_cnt)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())