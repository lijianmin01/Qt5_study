import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./test.db')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        query = QSqlQuery()  # 1

        query.exec_("CREATE TABLE students "                                  # 2
                    "(id INT(11) PRIMARY KEY, class VARCHAR(4) NOT NULL, "
                    "name VARCHAR(25) NOT NULL, score FLOAT)")

        query.exec_("INSERT INTO students (id, class, name, score) "          # 3
                    "VALUES (2018010401, '0104', 'Louis', 59.5)")
        query.exec_("INSERT INTO students (id, class, name, score) "
                    "VALUES (2018011603, '0116', 'Chris', 99.5)")

        query.exec_("SELECT name, class, score FROM students")                # 4
        while query.next():
            stu_name = query.value(0)
            stu_class = query.value(1)
            stu_score = query.value(2)
            print(stu_name, stu_class, stu_score)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
