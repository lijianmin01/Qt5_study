"""
由于按钮并没有颜色属性color，所以我们不能单纯的将b'color'传入，
必须要创建一个(注意属性必须要有一个设置函数[setter]，即属性可写，
才可以在动画中起效果。上面讲到的size，
pos和geometry属性都可以通过setGeometry()函数来设置，
pos还有move()函数，而size还有resize()函数)。

@property这个装饰器都有所了解，
它可以将一个方法转换为具有相同名称的只读属性，
其实也就是加了一个我们需要的属性
"""

import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

'''
class test(object):
    def __init__(self):
        super(Demo,self).__init__()
        self._color = ''

    """
    @property装饰器创建了一个color属性，
    再通过@color.setter装饰器给该属性一个设置函数，
    这样我们实例化Demo类后就可以非常方便地使用color属性了
    """

    @property
    def get_color(self):
        return self._color

    @color.setter
    def set_color(self,value):
        self._color = value

    """
     除了装饰器我们还可以使用property()函数来添加属性，
    该函数的作用是返回属性值
    """

    """
    property()函数中的
    fget参数为用于读取属性值的函数，
    而fset是用于设置属性值的函数。返回属性值保存在color中，
    也就是我们自定义的属性
    """
    color = property(fget=get_color, fset=set_color)
'''



class MyButton(QPushButton):
    def __init__(self,text=None,parent=None):
        super(MyButton,self).__init__(text,parent)
        self._color = QColor()


    def get_color(self):
        return self._color

    def set_color(self,col):
        self._color = col
        self.setStyleSheet('background-color: rgb({},{},{})'.format(col.red(), col.green(), col.blue()))

    # color = pyqtProperty(QColor, fget=get_color, fset=set_color)
    color = pyqtProperty(QColor, fget=get_color, fset=set_color)

class Demo(QWidget):
    def __init__(self):
        super(Demo,self).__init__()
        self.resize(600,600)

        self.btn = MyButton('Color',self)
        self.btn.setGeometry(0,0,100,100)

        self.animation = QPropertyAnimation(self.btn, b'color')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QColor(0, 0, 0))
        self.animation.setEndValue(QColor(255, 255, 255))
        self.animation.setLoopCount(-1)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


