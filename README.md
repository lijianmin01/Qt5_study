# Qt5_study

# 学习：https://zhuanlan.zhihu.com/p/86958063
# http://zetcode.com/gui/pyqt5/  前期代码看这位大佬写的博客
# https://zhuanlan.zhihu.com/pyqt5
# 2020.5.29
* 本来一开始打算用C++来学习Qt5,Qt转了半天多，最后我用的是VS2019,然后就是成功不了，御酒打算用Qt自带的IDE,很不幸，还是成功不了
* 拿python吧，嘻嘻

## 2020.5.31
* https://zhuanlan.zhihu.com/p/86959079

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