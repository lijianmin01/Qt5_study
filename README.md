# Qt5_study

# 学习：https://zhuanlan.zhihu.com/p/86958063
# http://zetcode.com/gui/pyqt5/  前期代码看这位大佬写的博客
# https://zhuanlan.zhihu.com/pyqt5
# 2020.5.29
* 本来一开始打算用C++来学习Qt5,Qt转了半天多，最后我用的是VS2019,然后就是成功不了，御酒打算用Qt自带的IDE,很不幸，还是成功不了
* 拿python吧，嘻嘻

## 2020.5.31
* https://zhuanlan.zhihu.com/p/86959079
* 总：https://zhuanlan.zhihu.com/p/75673557

## 2020.6.7
* pyqtdeploy

### 3.6 小结
* 1. QLineEdit控件为单行文本输入框；-
* 2. 了解四种布局方式：垂直布局QVBoxLayout、水平布局QHBoxLayout、表单布局QFormLayout和网格布局QGridLayout；
* 3. addWidget()方法用来添加控件，addLayout()方法用来添加布局；
* 4. 请记住QGridLayout的addWidget()语法形式：
* * addWidget(widget, row, column, rowSpan, columnSpan)

## 2020.06.08
### 4.3 小结
* 1. 消息框的种类有：
* * information 信息框；question 问答框； warning 警告框； critical 错误框； about 关于框( 其实还有一个aboutQt框，是专门用来展示Qt软件信息的，这里不再讲述)。
* 2. 语法形式(buttons可以不用指定)：
* * QMessageBox.information(QWidget, 'Title', 'Content', buttons)
* 3. 在与消息框交互的时候，可以用一个变量来保存消息框返回的按钮信息，接下来再用判断语句来作出不同的反应。​

## 2020.06.12
### 6.2 小结
* 1. 顾名思义，QTextEdit为用来编辑文本，而QTextBrowser用来显示文本；
* 2. setText()用来设置文本，toPlainText()用来获取文本，这两个控件都有这些方法；
* 3. 浏览框会执行Html代码。
* 图标网：http://easyicon.net/

### 7.5 小结
* 1. QPushButton和QToolButton非常相似，不过QToolButton更多是与QToolBar搭配使用，用来显示工具图片；
* 2. 可以通过setIcon()方法来给按钮设置图标；可以用setPixmap()方法给QLabel控件设置图片；
* 3. toogled信号在按钮状态发生改变时发出；stateChanged也是，不过该信号用于QCheckBox；
* 4. QRadioButton单选按钮只能进行多选一操作，即每次只会有一个单选按钮被选中；
* 5. 如果要让QCheckBox拥有三种状态的话，则需要通过setTristate(True)方法来设置；
* 6. 若要连接带有参数的自定义槽函数，可以通过lambda表达式来完成。

## 2020.06.14
### 8.3 小结
* 1. 下拉框介绍了QComboBox和QFontComboBox，后者是从前者继承并专门用来给用户选择字体的控件。
* 2. 添加选项内容方法为addItem()和addItems()，后者添加可循环对象；
* 3. 当下拉框当前选项发生改变的时候，会触发currentIndexChanged和currentTextChanged信号；
* 4. setFont()方法可以用来设置一些控件的字体；
* 5. 数字调节框介绍了QSpinBox和QDoubleSpinBox，前者调节整型数字，后者调节浮点型数字；
* 6. 当调节框数字发生改变时，会触发valueChanged信号；
* 7. setRange()方法用来设置范围，setSingleStep()方法用来设置步长，setValue()方法用来设置初始值。​

### 9.3 小结
* QSlider和QDial用法都差不多
* Qt.QHorizontal和Qt.Vertical分别用来实现水平的滑动条和垂直的滑动条
* setWindowTitle()可以设置窗口标题，setFixedSize()可以固定窗口或控件大小。

## 2020.6.15
### 10.3 小结
* 1. QTimer定时器会根据设定的时间不断发出timeout信号并调用连接的槽函数，通过start(int)方法来设置时间并启动定时器，stop()方法用于停止定时器；
* 2. 通过isActive()方法来判断定时器是否被激活，setSingleShot()方法可以在触发timeout信号后只调用一次槽函数；
* 3. 通过setOrientation(Qt.Vertical)方法可以将进度条设为垂直显示；
* 4. setMinimum()和setMaximum()方法用来设置进度条范围(可以用setRange()替代)，setValue()方法用于设置进度条的当前值，reset()方法用于重置进度条


### ​11.2 小结
* 1. QLCDNumber显示方式其实就跟电子表的显示方式一样。
* 2. setDigitCount(int)用于设置可显示位数；
* setSegmentStyle()用于设置样式；setMode()用于设置数字显示方式；display()用于显示。

## ​12.3 小结
* 1. QCalendarWidget为日历控件，用户可以设置日期范围，可以设置日历初始化时显示的日期(如果没有设置的话，默认为当天日期)；
* 2. QDateTimeEdit、QDateEdit以及QTimeEdit这三个控件用法差不多，读者掌握QDateTimeEdit的话其他两种其实也就明白怎么使用了；
* 3. 通过setCalendarPopup(True)方法可以让QDateTimeEdit和QDateEdit显示日历