import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QMainWindow, \
    QTabWidget

import re

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 创建tabwidget

        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)

        self.tabWidget.currentChanged.connect(self.change_tab)

        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        #self.setCentralWidget(self.tabWidget)

        self.all_layout = QVBoxLayout()
        self.all_layout.addWidget(self.tabWidget)
        self.setLayout(self.all_layout)

        # 第一个标签页
        self.webview = WebEngineView(self)  # self必须要有，是将主窗口作为参数，传给浏览器

        self.webview.load(QUrl("http://www.baidu.com"))

        self.now_view = self.webview
        self.create_tab(self.webview)



    def change_tab(self):
        # webview
        self.now_view = self.tabWidget.currentWidget().webview
        self.now_line = self.tabWidget.currentWidget().url_le

    # 创建tab
    def create_tab(self, webview):
        webview.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        webview.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        webview.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.tab = QWidget()

        self.tab.back_btn = QPushButton(self.tab)
        self.tab.forward_btn = QPushButton(self.tab)
        self.tab.refresh_btn = QPushButton(self.tab)
        self.tab.zoom_in_btn = QPushButton(self.tab)
        self.tab.zoom_out_btn = QPushButton(self.tab)
        self.tab.url_le = QLineEdit(self.tab)
        self.tab.webview = webview

        self.now_view=self.tab.webview
        self.now_line=self.tab.url_le

        self.tabWidget.addTab(self.tab, "新标签页")
        self.tabWidget.setCurrentWidget(self.tab)


        self.Layout = QVBoxLayout(self.tab)
        self.btn = QHBoxLayout(self.tab)

        self.btn.setSpacing(0)
        self.btn.addWidget(self.tab.back_btn)
        self.btn.addWidget(self.tab.forward_btn)
        self.btn.addWidget(self.tab.refresh_btn)
        # ，使用setSpacing()传入参数0代表让各个控件之间不存在间隔(主要想让按钮靠拢)，
        self.btn.addStretch(2)
        self.btn.addWidget(self.tab.url_le)
        self.btn.addStretch(2)
        self.btn.addWidget(self.tab.zoom_in_btn)
        self.btn.addWidget(self.tab.zoom_out_btn)

        # 按钮初始化
        self.tab.back_btn.setIcon(QIcon('imgs/back.png'))
        self.tab.forward_btn.setIcon(QIcon('imgs/forward.png'))
        self.tab.refresh_btn.setIcon(QIcon('imgs/reload.png'))
        self.tab.zoom_in_btn.setIcon(QIcon('imgs/zoom_in.png'))
        self.tab.zoom_out_btn.setIcon(QIcon('imgs/zoom_out.png'))

        self.tab.back_btn.setShortcut('Ctrl+,')
        self.tab.back_btn.clicked.connect(webview.back)
        self.tab.back_btn.setShortcut('Ctrl+.')
        self.tab.forward_btn.clicked.connect(webview.forward)
        self.tab.refresh_btn.clicked.connect(webview.reload)

        self.tab.zoom_in_btn.setShortcut('Ctrl+=')
        self.tab.zoom_in_btn.clicked.connect(lambda : (webview.setZoomFactor(webview.zoomFactor() + 0.1)))
        self.tab.zoom_out_btn.setShortcut('Ctrl+-')
        self.tab.zoom_out_btn.clicked.connect(lambda : (webview.setZoomFactor(webview.zoomFactor() - 0.1)))

        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addLayout(self.btn)
        self.Layout.addWidget(webview)


        # 算了先设置搜索功能把
    def keyPressEvent(self,QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            flag = re.match(r'^https?:/{2}\w.+$', str(self.now_line.text()))
            # self.url_le.hasFocus():判断是为了只有在输入框被编辑的状态下敲击回车才会让网页实现跳转
            # 用load()方法并传入一个QUrl类型参数即可(不能单单传入字符串，需要用QUrl()把字符串转为QUrl对象)
            if flag and self.now_line.hasFocus():
                self.now_view.load(QUrl(self.now_line.text()))
            else:
                if self.now_line.text()[-4:] == '.com':
                    self.now_view.load(QUrl('https://' + self.now_line.text()))
                else:
                    self.now_view.load(QUrl('https://www.baidu.com/s?wd=' + self.now_line.text()))

    # 关闭tab
    def close_Tab(self, index):
        if self.tabWidget.count() > 1:
            self.tabWidget.removeTab(index)
        else:
            self.close()  # 当只有1个tab时，关闭主窗口


class WebEngineView(QWebEngineView):

    def __init__(self,mainwindow,parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow
        self.other_init()


    # 重写createwindow()，实现制作出新的页面
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)
        self.mainwindow.create_tab(new_webview)
        new_webview.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        return new_webview

    def other_init(self):
        # #支持视频播放
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        # 支持页面关闭请求
        self.page().windowCloseRequested.connect(self.on_windowCloseRequested)

        # 支持页面下载请求
        # self.page().profile().downloadRequested.connect(self.on_downloadRequested)

    #  支持页面关闭请求
    def on_windowCloseRequested(self):
        the_index = self.mainwindow.tabWidget.currentIndex()
        self.mainwindow.tabWidget.removeTab(the_index)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = Demo()
    the_mainwindow.show()
    sys.exit(app.exec_())