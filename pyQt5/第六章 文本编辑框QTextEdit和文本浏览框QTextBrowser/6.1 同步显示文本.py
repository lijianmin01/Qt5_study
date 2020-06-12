"""
前者用来编辑文本，后者无法编辑
左边为QTextEdit控件，右边为QTextBrowser控件。在左边输入文字时，右边会同步显示。
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel('QTextEdit', self)
        self.browser_label = QLabel('QTextBrowser', self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)  # 1

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())  # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


"""
程序非常简单。通过实例化两个QLabel、一个QTextEdit以及一个QTextBrowser
再通过垂直布局和水平布局就可以完成整个界面。关键点是在信号和槽的连接上。

1. 将self.text_edit的textChanged信号连接到自定义的槽函数上。也就是说当self.text_edit中的文本发生改变的时候，
就会发出textChanged信号，然后调用show_text_func()槽函数。

2. 在槽函数中我们通过setText()方法将self.text_browser的文本设为self.text_edit的文本，
而self.text_edit的文本通过toPlainText()获取，而不是text().
"""









# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
#     QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout
#
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo,self).__init__()
#         self.edit_label = QLabel('QTextEdit',self)
#         self.browser_label = QLabel('QTextBrowser',self)
#         self.text_edit = QTextEdit(self)
#         self.text_browser = QTextBrowser(self)
#
#         self.edit_v_layout = QVBoxLayout()
#         self.browser_v_layout = QVBoxLayout()
#         self.all_h_layout = QHBoxLayout()
#
#     def layout_init(self):
#         self.edit_v_layout.addWidget(self.edit_label)
#         self.edit_v_layout.addWidget(self.text_edit)
#
#         self.browser_v_layout.addWidget(self.browser_label)
#         self.browser_v_layout.addWidget(self.text_browser)
#
#         self.all_h_layout.addLayout(self.edit_v_layout)
#         self.all_h_layout.addLayout(self.browser_v_layout)
#
#         self.setLayout(self.all_h_layout)
#
#     def text_edit_init(self):
#         self.text_edit.textChanged.connect(self.show_text_func)
#
#     def show_text_func(self):
#         self.text_browser.setText(self.text_edit.toPlainText())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())















