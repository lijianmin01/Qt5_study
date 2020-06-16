"""
通常我们在Windows或Linux上使用复制都是按ctrl+c然后按ctrl+v进行粘贴(Mac上为command+c和command+v)，
这其中就涉及到了剪贴板，
当进行复制时，其实是将要复制的内容放到了一个无形的剪贴板上，
要粘贴时，再将剪贴板上的内容放到界面上。
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QPushButton, QGridLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.clipboard = QApplication.clipboard()  # 1
        self.clipboard.dataChanged.connect(lambda: print('Data Changed'))

        self.copy_btn = QPushButton('Copy', self)  # 2
        self.copy_btn.clicked.connect(self.copy_func)

        self.paste_btn = QPushButton('Paste', self)  # 3
        self.paste_btn.clicked.connect(self.paste_func)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.text_edit, 0, 0, 1, 1)
        self.g_layout.addWidget(self.text_browser, 0, 1, 1, 1)
        self.g_layout.addWidget(self.copy_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.paste_btn, 1, 1, 1, 1)
        self.setLayout(self.g_layout)

    def copy_func(self):
        # 们将text_edit中的文本获取过来并通过setText()方法将其设置为剪贴板的文本；
        self.clipboard.setText(self.text_edit.toPlainText())

    def paste_func(self):
        self.text_browser.setText(self.clipboard.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())