import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()

    def db_connect(self):
        # 通过调用QSqlDatabase类的addDatabase()方法来创建一个数据库连接
        self.db = QSqlDatabase.addDatabase('QSQLITE')    # 1
        # 调用setDatabaseName()设置要使用的数据库名称，
        # 只需要写入一个路径，文件名以.db结尾即可
        # (若该数据库已经存在，则使用该数据库；若不存在则会新建一个)
        self.db.setDatabaseName('./test.db')             # 2
        # 调用open()方法打开数据库，若打开成功则返回True，失败则返回False
        if not self.db.open():                           # 3
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    # 在窗口关闭事件中通过self.db.close()方法来关闭数据库。
    def closeEvent(self, QCloseEvent):                   # 4
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())