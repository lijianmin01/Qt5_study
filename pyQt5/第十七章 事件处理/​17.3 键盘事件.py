# 每当用户按下或释放键盘上的任意键时都会触发键盘事件：

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)  # 1
        self.pic_label.setPixmap(QPixmap('../QIconImg/17part/keyboard.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

        self.key_label = QLabel('No Key Pressed', self)  # 2
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):  # 3
        if QKeyEvent.key() == Qt.Key_Up:
            self.pic_label.setPixmap(QPixmap('../QIconImg/17part/up.png'))
            self.key_label.setText('Key Up Pressed')
        elif QKeyEvent.key() == Qt.Key_Down:
            self.pic_label.setPixmap(QPixmap('../QIconImg/17part/down.png'))
            self.key_label.setText('Key Down Pressed')
        elif QKeyEvent.key() == Qt.Key_Left:
            self.pic_label.setPixmap(QPixmap('../QIconImg/17part/left.png'))
            self.key_label.setText('Key Left Pressed')
        elif QKeyEvent.key() == Qt.Key_Right:
            self.pic_label.setPixmap(QPixmap('../QIconImg/17part/right.png'))
            self.key_label.setText('Key Right Pressed')

    def keyReleaseEvent(self, QKeyEvent):  # 4
        self.pic_label.setPixmap(QPixmap('../QIconImg/17part/keyboard.png'))
        self.key_label.setText('Key Released')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())