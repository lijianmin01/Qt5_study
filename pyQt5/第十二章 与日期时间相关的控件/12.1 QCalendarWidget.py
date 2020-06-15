# # 下面来简单显示一个日历控件，点击不同的星期，会显示不同的心情

import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout

# 1. 设置一个字典，并将各个星期及对应的颜文字分别作为键值输入；
EMOTION = {  # 1
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́) ✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        # 通过setMinimumDate()和
        # setMaximumDate()可以设置日历的最小和最大日期
        # (可用setDateRange()替代)，传入的参数为QDate。
        self.calendar.setMinimumDate(QDate(1946, 2, 14))  # 2
        self.calendar.setMaximumDate(QDate(6666, 6, 6))  # 3
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
        # self.calendar.setFirstDayOfWeek(Qt.Monday)                            # 4
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))
        # 5
        # setGridVisible(bool)方法可以设置是否在日历上显示网格；
        self.calendar.setGridVisible(True)  # 6
        # 当点击到日历上的某个日期时，clicked信号就会被触发
        self.calendar.clicked.connect(self.show_emotion_func)  # 6

        self.calendar.setFirstDayOfWeek(Qt.Sunday)

        print(self.calendar.minimumDate())  # 7
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel(self)  # 8
        self.label.setAlignment(Qt.AlignCenter)

        # setSelectedDate()方法可以设置日历初始化时所显示的日期
        # ，如果不设置，则默认是当天日期；
        weekday = self.calendar.selectedDate().toString('ddd')  # 9
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):  # 10
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())











#
# import sys
# from PyQt5.QtCore import QDate, Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout
#
# EMOTION = {                                                                     # 1
#     'Mon': '(╯°Д°)╯︵ ┻━┻',
#     'Tue': '(╯￣Д￣)╯╘═╛',
#     'Wed': '╭(￣▽￣)╯╧═╧',
#     'Thu': '_(:з」∠)_',
#     'Fri': '(๑•̀ㅂ•́) ✧',
#     'Sat': '( ˘ 3˘)♥',
#     'Sun': '(;′༎ຶД༎ຶ`)'
# }
#
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo,self).__init__()
#         self.calendar = QCalendarWidget(self)
#         self.calendar.setMinimumDate(QDate(1946,2,14))
#         self.calendar.setMaximumDate(QDate(6666,6,6))
#         # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
#         # self.calendar.setFirstDayOfWeek(Qt.Monday)                            # 4
#         # self.calendar.setSelectedDate(QDate(1946, 2, 14))                     # 5
#         self.calendar.setGridVisible(True)  # 6
#         self.calendar.clicked.connect(self.show_emotion_func)  # 6
#
#         print(self.calendar.minimumDate())                                      # 7
#         print(self.calendar.maximumDate())
#         print(self.calendar.selectedDate())
#
#         self.label = QLabel(self)
#         self.label.setAlignment(Qt.AlignCenter)
#
#         weekday = self.calendar.selectedDate().toString("ddd")
#         self.label.setText(EMOTION[weekday])
#
#         self.v_layout = QVBoxLayout()
#         self.v_layout.addWidget(self.calendar)
#         self.v_layout.addWidget(self.label)
#
#         self.setLayout(self.v_layout)
#         self.setWindowTitle('QCalendarWidget')
#
#     def show_emotion_func(self):  # 10
#         weekday = self.calendar.selectedDate().toString('ddd')
#         self.label.setText(EMOTION[weekday])
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())
#
#
