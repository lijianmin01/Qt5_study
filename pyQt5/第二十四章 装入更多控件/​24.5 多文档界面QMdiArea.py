import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QTextEdit


class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.mdi_area = QMdiArea(self)  # 1
        self.setCentralWidget(self.mdi_area)

        self.toolbar = self.addToolBar('Tool Bar')

        self.new_action = QAction(QIcon('images/new.ico'), 'New', self)  # 2
        self.close_action = QAction(QIcon('images/close.ico'), 'Close', self)
        self.close_all_action = QAction(QIcon('images/close_all.ico'), 'Close All', self)
        self.mode1_action = QAction(QIcon('cascade.ico'), 'Cascade', self)
        self.mode2_action = QAction(QIcon('tile.ico'), 'Tile', self)

        self.new_action.triggered.connect(self.new_func)  # 3
        self.close_action.triggered.connect(self.mdi_area.closeActiveSubWindow)
        self.close_all_action.triggered.connect(self.mdi_area.closeAllSubWindows)
        self.mode1_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        self.mode2_action.triggered.connect(self.mdi_area.tileSubWindows)

        self.toolbar.addAction(self.new_action)  # 4
        self.toolbar.addAction(self.close_action)
        self.toolbar.addAction(self.close_all_action)
        self.toolbar.addAction(self.mode1_action)
        self.toolbar.addAction(self.mode2_action)

    def new_func(self):
        text = QTextEdit()
        sub = QMdiSubWindow()
        sub.setWidget(text)
        self.mdi_area.addSubWindow(sub)
        sub.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
