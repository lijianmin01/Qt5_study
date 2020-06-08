import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()

        self.btn_information = QPushButton('information',self)
        #self.btn_information.clicked.connect(self.show_information)

        self.btn_question = QPushButton('Question', self)
        #self.btn_question.clicked.connect(self.show_question)

        self.btn_warning = QPushButton('warning', self)
        #self.btn_warning.clicked.connect(self.show_warning)

        # 错误框
        self.btn_critical = QPushButton('critical ', self)
        #self.btn_critical.clicked.connect(self.show_critical)

        # 关于框
        self.btn_about = QPushButton('about', self)
        self.btn_about.clicked.connect(self.show_about1())

        def show_information(self):
            QMessageBox.information(self, 'Title', 'Content',
                                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        # def show_question(self):
        #     QMessageBox.question(self, 'question', 'Content',
        #                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        # def show_warning(self):
        #     QMessageBox.question(self, 'warning', 'Content',
        #                          QMessageBox.Ok)
        # def show_critical(self):
        #     QMessageBox.question(self, 'critical', 'Content',
        #                          QMessageBox.Ok)
        def show_about1(self):
            QMessageBox.question(self, 'about', 'Content',
                                 QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())




