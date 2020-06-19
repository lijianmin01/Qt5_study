import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        #self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)

        #####创建tabwidget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)

        ####第一个tab
        self.webview = WebEngineView(self)   #self必须要有，是将主窗口作为参数，传给浏览器
        self.webview.load(QUrl("http://www.baidu.com"))
        self.create_tab(self.webview)


    #创建tab
    def create_tab(self,webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "新标签页")
        self.tabWidget.setCurrentWidget(self.tab)
        #####
        self.Layout = QVBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)



    #关闭tab
    def close_Tab(self,index):
        if self.tabWidget.count()>1:
            self.tabWidget.removeTab(index)
        else:
            self.close()   # 当只有1个tab时，关闭主窗口





################################################
#######创建浏览器
################################################
class WebEngineView(QWebEngineView):

    def __init__(self,mainwindow,parent=None):
        super(WebEngineView, self).__init__(parent)
        self.mainwindow = mainwindow


    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview = WebEngineView(self.mainwindow)

        self.mainwindow.create_tab(new_webview)

        return new_webview


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = MainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
