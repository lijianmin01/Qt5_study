"""
想象下，假如你的程序中用到了100个按钮，那你会选择将这100个按钮全部同时显示在界面上吗？当然不能这么做，不然界面得多拥挤。
我们可以将这100个按钮放在一个滚动区域QScrollArea中，用户刚开始只能看见几个按钮，但滚动条可以让他们操作其余的按钮。
 通过QScrollArea我们可以让界面显得更加整洁友好。

QScrollArea本身自带滚动条，但是有很多时候，开发人员可能想要往滚动条上加入更多功能来控制界面，
或者说有时候只是需要用到滚动条而已。QScrollBar类可以让我们设计自己想要的滚动条。

"""
# 通过下面这个例子来一起讲解下QScrollArea和QScrollBar的基本用法

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QScrollArea, QScrollBar, \
                            QHBoxLayout, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('image.jpg'))
        # setScaledContents(True)方法可以让图片随着QLabel控件大小变化而变化，即自适应；
        self.label.setScaledContents(True)

        # 实例化一个QScrollArea控件，调用setWidget()方法将QLabel滚动区域中的控件。
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollbar = QScrollBar(Qt.Horizontal, self)  # 3
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

        self.bigger_btn = QPushButton('Zoom in', self)  # 4
        self.smaller_btn = QPushButton('Zoom out', self)

        self.bigger_btn.clicked.connect(self.bigger_func)  # 5
        self.smaller_btn.clicked.connect(self.smaller_func)
        self.scrollbar.valueChanged.connect(self.sync_func)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.bigger_btn)
        self.h_layout.addWidget(self.smaller_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        self.v_layout.addWidget(self.scrollbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def bigger_func(self):
        self.label.resize(self.label.width() * 1.2, self.label.height() * 1.2)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

    def smaller_func(self):
        self.label.resize(self.label.width() * 0.8, self.label.height() * 0.8)
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())

    def sync_func(self):
        self.scroll_area.horizontalScrollBar().setValue(self.scrollbar.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())








