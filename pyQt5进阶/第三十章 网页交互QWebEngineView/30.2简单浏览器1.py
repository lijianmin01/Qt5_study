import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

import re

# class My_QWebEngineView(QWebEngineView):
#
#     def mousePressEvent_cnt(self):
#         print("123")
#         self.browser.load(QUrl(self.browser.url()))

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(1000,600)

        self.back_btn = QPushButton(self)
        self.forward_btn = QPushButton(self)
        self.refresh_btn = QPushButton(self)
        self.zoom_in_btn = QPushButton(self)
        self.zoom_out_btn = QPushButton(self)
        self.url_le = QLineEdit(self)

        self.browser = QWebEngineView(self)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.btn_init()
        self.le_init()
        self.browser_init()
        #self.other_init()

    def layout_init(self):
        self.h_layout.setSpacing(0)
        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)
        # ，使用setSpacing()传入参数0代表让各个控件之间不存在间隔(主要想让按钮靠拢)，
        self.h_layout.addStretch(2)
        self.h_layout.addWidget(self.url_le)
        self.h_layout.addStretch(2)
        self.h_layout.addWidget(self.zoom_in_btn)
        self.h_layout.addWidget(self.zoom_out_btn)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)

        self.setLayout(self.v_layout)


    def btn_init(self):
        self.back_btn.setIcon(QIcon('imgs/back.png'))
        self.forward_btn.setIcon(QIcon('imgs/forward.png'))
        self.refresh_btn.setIcon(QIcon('imgs/reload.png'))
        self.zoom_in_btn.setIcon(QIcon('imgs/zoom_in.png'))
        self.zoom_out_btn.setIcon(QIcon('imgs/zoom_out.png'))

        # 实现按钮的功能：
        self.back_btn.setShortcut('Ctrl+,')
        self.back_btn.clicked.connect(self.browser.back)
        self.back_btn.setShortcut('Ctrl+.')
        self.forward_btn.clicked.connect(self.browser.forward)
        self.refresh_btn.clicked.connect(self.browser.reload)

        self.zoom_in_btn.setShortcut('Ctrl+=')
        self.zoom_in_btn.clicked.connect(self.zoom_in_func)
        self.zoom_out_btn.setShortcut('Ctrl+-')
        self.zoom_out_btn.clicked.connect(self.zoom_out_func)


    def le_init(self):                            # 5
        self.url_le.setFixedWidth(600)
        self.url_le.setPlaceholderText('Search or enter website name')

    # 在输入框中输入网址并敲击回车后，
    # QWebEngineView加载并显示相应的网址内容：
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            flag = re.match(r'^https?:/{2}\w.+$', str(self.url_le.text()))
            # self.url_le.hasFocus():判断是为了只有在输入框被编辑的状态下敲击回车才会让网页实现跳转
            # 用load()方法并传入一个QUrl类型参数即可(不能单单传入字符串，需要用QUrl()把字符串转为QUrl对象)
            if flag and self.url_le.hasFocus():
                self.browser.load(QUrl(self.url_le.text()))
            else:
                if self.url_le.text()[-4:]=='.com':
                    self.browser.load(QUrl('https://' + self.url_le.text()))
                else:
                    self.browser.load(QUrl('https://www.baidu.com/s?wd='+self.url_le.text()))

    def mousePressEvent(self, QMouseEvent):
        print(self.browser.url())
        self.browser.load(QUrl(self.browser.url()))

    def urlChanged(self):
        self.browser.load(QUrl(self.browser.url()))

    #首次运行程序时，QWebEngineView显示百度网页
    def browser_init(self):
        self.browser.load(QUrl('https://baidu.com'))
        self.browser.urlChanged.connect(lambda: self.url_le.setText(self.browser.url().toDisplayString()))


    # 放大缩小页面
    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())