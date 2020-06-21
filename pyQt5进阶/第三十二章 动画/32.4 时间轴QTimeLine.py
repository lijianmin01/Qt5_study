import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.label = QLabel('Hello PyQt5', self)
        self.label.move(-100, 100)

        # 实例化一个QTimeLine类，持续时间为5秒
        self.timeline = QTimeLine(5000, self)                       # 1
        self.timeline.setFrameRange(0, 700)                         # 2
        self.timeline.frameChanged.connect(self.set_frame_func)     # 3
        # 注意这里传入0代表无限循环运行，而不是不运行。传入正整数会运行相应次数，传入负数不运行。
        self.timeline.setLoopCount(0)                               # 4
        self.timeline.start()

    def set_frame_func(self, frame):
        # 我们调用move()方法，根据帧数来移动QLabel控件的位置；
        self.label.move(-100+frame, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())