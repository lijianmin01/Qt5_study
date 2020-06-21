import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.label = QLabel('Hello PyQt5', self)
        self.label.move(-100, 100)

        self.timeline = QTimeLine(5000, self)
        self.timeline.setFrameRange(0, 700)
        self.timeline.frameChanged.connect(self.set_frame_func)
        self.timeline.stateChanged.connect(lambda: print(self.timeline.state()))    # 1
        self.timeline.setLoopCount(0)

        self.start_btn = QPushButton('Start', self)
        self.stop_btn = QPushButton('Stop', self)
        self.pause_btn = QPushButton('Pause', self)
        self.resume_btn = QPushButton('Resume', self)

        self.start_btn.clicked.connect(self.timeline.start)                         # 2
        self.stop_btn.clicked.connect(self.timeline.stop)
        self.pause_btn.clicked.connect(lambda: self.timeline.setPaused(True))
        self.resume_btn.clicked.connect(self.timeline.resume)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.start_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.h_layout.addWidget(self.pause_btn)
        self.h_layout.addWidget(self.resume_btn)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def set_frame_func(self, frame):
        self.label.move(-100+frame, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())