"""
拖放分为拖动和放下两个动作，它们涉及到以下事件:
        DragEnterEvent: 所拖动目标进入接收该事件的窗口或控件时触发；
        DragMoveEvent: 所拖动目标进入窗口或控件后，继续被拖动时触发；
        DragLeaveEvent: 所拖动目标离开窗口或控件时触发；
        DropEvent: 所拖动目标被放下时触发。
"""

# 一个可以实现拖放txt文件并读取的小程序：

import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser

class Demo(QTextBrowser):
    def __init__(self):
        super(Demo,self).__init__()
        # setAcceptDrops(True)方法可以让该控件接收放下(Drop)事件
        self.setAcceptDrops(True)

    """
     当拖动目标进入QTextBrowser的那一刹那，触发dragEnterEvent事件，
     在该响应函数中，我们先判断所拖动目标的MIME类型是否为text/plain，
     若是的话则调用acceptProposedAction()方法来表明可以
     在QTextBrowser上进行拖放动作；
    """
    # 当目标进入窗体后，如果不放下而是继续移动的话，则会触发dragMoveEvent事件
    def dragEnterEvent(self, QDragEnterEvent):
        print('Drag Enter')
        if QDragEnterEvent.mimeDate().hasText():
            QDragEnterEvent.acceptProposedAction()

    def dragMoveEvent(self, QDragMoveEvent):
        print('Drag Move')

    #  将进入控件后的目标再次拖动到控件之外时，就会触发dragLeaveEvent()事件
    def dragLeaveEvent(self,QDragLeaveEvent):
        print('Drag Drop')
        # MacOS?
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/')

        # Linux
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/').strip()

        #Windows
        txt_path = QDropEvent.mimeData().text().replace('file:///', '')

        with open(txt_path, 'r') as f:
            self.setText(f.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())