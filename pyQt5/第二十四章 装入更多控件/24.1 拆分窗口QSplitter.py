"""
下面我们将第二十章中的QListView、
QTreeView和QTableView放到拆分窗口中，
三个视图全都只用QDirModel来显示文件目录。
请看下方代码：
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSplitter, QListView, QTreeView, QTableView, QDirModel


class Demo(QSplitter):                                          # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.dir_model = QDirModel(self)                        # 2

        self.list_view = QListView(self)                        # 3
        self.tree_view = QTreeView(self)
        self.table_view = QTableView(self)
        self.list_view.setModel(self.dir_model)
        self.tree_view.setModel(self.dir_model)
        self.table_view.setModel(self.dir_model)

        self.tree_view.doubleClicked.connect(self.show_func)    # 4

        # self.setOrientation(Qt.Vertical)                      # 5
        self.addWidget(self.list_view)
        self.addWidget(self.tree_view)
        self.insertWidget(0, self.table_view)
        self.setSizes([300, 200, 200])
        print(self.count())

    def show_func(self, index):
        self.list_view.setRootIndex(index)
        self.table_view.setRootIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())