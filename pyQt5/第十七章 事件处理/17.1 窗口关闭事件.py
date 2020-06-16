# 在博客编辑器中进行写作时，若没有点击保存直接关闭窗口时(触发窗口关闭事件)，会出现弹框询问是否确定离开：

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, \
    QPushButton, QMessageBox, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        # is_saved变量用于记录用户是否已经进行保存；
        self.is_saved = True

        # QTextEdit控件用于文本编辑，将其textChanged信号和自定义的槽函数连接起来：
        self.textedit = QTextEdit(self)
        self.textedit.textChanged.connect(self.on_textchanged_func)

        self.button = QPushButton("save",self)
        self.button.clicked.connect(self.on_clicked_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

        with open('saved.txt', 'r') as f:
            text = str(f.read())
            self.textedit.setText(text)
        f.close()

    """
    在槽函数中我们判断在每次文本内容发生变化时，
    textedit中是否还有文本，若有的话则将is_saved变量设为False，
    即未保存；若无文本，则将其设为True(如果没有文本的话，
    那可以直接关闭窗口，程序不会询问是否需要保存，因为没必要)。
    """
    def on_textchanged_func(self):
        # 多行简单文本框用 toPlainText()
        if self.textedit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def on_clicked_func(self):
        self.save_func(self.textedit.toPlainText())
        self.is_saved = True

    def save_func(self,text):
        with open('saved.txt','w') as f:
            f.write(text)
    # 我们重新定义了QWidget的窗口关闭函数closeEvent()
    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self,' ','Do you want to save the text ?',
                                          QMessageBox.Yes | QMessageBox.No |QMessageBox.Cancel)
        if choice == QMessageBox.Yes:
            self.save_func(self.textedit.toPlainText())
        elif choice == QMessageBox.No:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())






