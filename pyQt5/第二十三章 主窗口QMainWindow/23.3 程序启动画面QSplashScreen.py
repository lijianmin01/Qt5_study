"""
许多应用程序的主窗口在打开前都会先展示一个启动画面(例如PS)，这是因为打开需要一定时间，所以用启动画面来显示模块加载进度，这也是一种增加程序使用友好度的方法。通常我们会将程序启动画面的代码放在程序入口中，位于sys.exit(app.exec_())之前
"""
# 首先先更新下导入的模块，我们新增了time、QPixmap、Qt以及QSplashScreen：


import sys
import time
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,\
                            QFontDialog, QColorDialog, QSplashScreen

"""
    判断文本是否保存了
    是否是第一次保存
    文件路径保存
"""


class Demo(QMainWindow):
    is_saved = True
    is_saved_first = True
    path = ""

    def __init__(self):
        super(Demo, self).__init__()
        # 添加菜单栏、工具栏和状态栏：
        self.file_menu = self.menuBar().addMenu('File')
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu("Help")

        self.file_toolbar = self.addToolBar('File')
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()

        # 将一个动作看作一种命令，每当用户点击某个动作时，就会触发某种命令，程序从而执行相应的命令。那现在我们就要实例化几个动作
        self.new_action = QAction('New', self)
        self.open_action = QAction('OPen', self)
        self.save_action = QAction('Save', self)
        self.save_as_action = QAction('Save As', self)
        self.close_action = QAction('Close', self)
        self.cut_action = QAction('Cut', self)
        self.copy_action = QAction('Copy', self)
        self.paste_action = QAction('Paste', self)
        # 字体修改
        self.font_action = QAction('Font', self)
        # 颜色修改
        self.color_action = QAction('Color', self)
        self.about_action = QAction('Qt', self)
        self.about_author = QAction('备注', self)

        # 实例化一个QTextEdit控件
        self.text_edit = QTextEdit(self)

        # 剪切复制粘贴功能 ==> QMimeData类
        self.mime_data = QMimeData()
        self.clipboard = QApplication.clipboard()

        """
        调用QMainWindow的setCentralWidget()方法可以设置主窗口的中央控件，
        这里我们将文本编辑框text_edit设置为中央控件。调用resize()方法将窗口设置到合适的大小
        """
        self.setCentralWidget(self.text_edit)
        self.resize(450, 600)

        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()
        self.text_edit_int()

    # 将相应的动作添加到了菜单栏
    def menu_init(self):
        # addSeparator()方法顾名思义就是加一个分割条
        # 调用addAction()方法就可以将动作添加进去
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)

        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.font_action)
        self.edit_menu.addAction(self.color_action)

        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.about_author)

    def toolbar_init(self):
        self.file_toolbar.addAction(self.new_action)
        self.file_toolbar.addAction(self.open_action)
        self.file_toolbar.addAction(self.save_action)
        self.file_toolbar.addAction(self.save_as_action)

        self.edit_toolbar.addAction(self.cut_action)
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.paste_action)
        self.edit_toolbar.addAction(self.font_action)
        self.edit_toolbar.addAction(self.color_action)

    # 状态栏
    def status_bar_init(self):
        self.status_bar.showMessage('Ready to compose')

    # action_init()中设置动作
    # setToolTip()方法可以用来设置小气泡提示，当鼠标停留在该动作上时，就会显示相应的提示(当然我们也可以对其他对象使用该方法，比如QPushButton)。
    # setStatusTip()就是设置状态栏信息
    # 将new_action的triggered信号与自定义的槽函数连接起来
    def action_init(self):
        self.new_action.setIcon(QIcon('images/new.ico'))
        self.new_action.setShortcut('Ctrl+N')
        self.new_action.setToolTip('Create a new file')
        self.new_action.setStatusTip('Create a new file')
        self.new_action.triggered.connect(self.new_func)

        self.open_action.setIcon(QIcon('images/open.ico'))  # 2
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')
        self.open_action.triggered.connect(self.open_file_func)

        self.save_action.setIcon(QIcon('images/save.ico'))  # 3
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')
        self.save_action.triggered.connect(lambda: self.save_func(self.text_edit.toHtml()))

        self.save_as_action.setIcon(QIcon('images/save_as.ico'))  # 4
        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.setToolTip('Save the file to a specified location')
        self.save_as_action.setStatusTip('Save the file to a specified location')
        self.save_as_action.triggered.connect(lambda: self.save_as_func(self.text_edit.toHtml()))

        self.close_action.setIcon(QIcon('images/close.ico'))  # 5
        self.close_action.setShortcut('Ctrl+E')
        self.close_action.setToolTip('Close the window')
        self.close_action.setStatusTip('Close the window')
        self.close_action.triggered.connect(self.close_func)

        self.cut_action.setIcon(QIcon('images/cut.ico'))  # 6
        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setToolTip('Cut the text to clipboard')
        self.cut_action.setStatusTip('Cut the text')
        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.setIcon(QIcon('images/copy.ico'))  # 7
        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setIcon(QIcon('images/paste.ico'))  # 8
        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setToolTip('Paste the text')
        self.paste_action.setStatusTip('Paste the text')
        self.paste_action.triggered.connect(self.paste_func)

        self.font_action.setIcon(QIcon('images/font.ico'))  # 9
        self.font_action.setShortcut('Ctrl+T')
        self.font_action.setToolTip('Change the font')
        self.font_action.setStatusTip('Change the font')
        self.font_action.triggered.connect(self.font_func)

        self.color_action.setIcon(QIcon('images/color.ico'))  # 10
        self.color_action.setShortcut('Ctrl+R')
        self.color_action.setToolTip('Change the color')
        self.color_action.setStatusTip('Change the color')
        self.color_action.triggered.connect(self.color_func)

        self.about_action.setIcon(QIcon('images/about.ico'))  # 11
        self.about_action.setShortcut('Ctrl+Q')
        self.about_action.setToolTip('What is Qt?')
        self.about_action.setStatusTip('What is Qt?')
        self.about_action.triggered.connect(self.about_func)

        self.about_author.setIcon(QIcon('images/author.ico'))
        self.about_action.setShortcut('Ctrl+A')
        self.about_author.setToolTip('备注信息')
        self.about_author.setStatusTip('备注信息')
        self.about_author.triggered.connect(self.about_author_func)

    # 创建新的文件
    """
    判断当前文本是否有保存，如果没有的话，
    那就出现弹框询问是否要保存，
    按Yes的话就调用save_func()函数进行保存
    保存好了当然要将当前的文本编辑框清空

    若按No不进行保存的话，就直接清空

    若按下Cancel取消的话，则不进行任何动
    """

    def new_func(self):
        # QPlainTextEdit 多行简单文本框用toPlainText()
        if not self.is_saved and self.text_edit.toPlainText():
            choice = QMessageBox.Question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                self.text_edit.clear()
                self.is_saved_first = True
            elif choice == QMessageBox.No:
                self.text_edit.clear()
            else:
                pass
        else:
            self.text_edit.clear()
            self.is_saved = False
            self.is_saved_first = True

    def open_file_func(self):
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log *.md)')
                if file:
                    with open(file, 'r') as f:
                        self.text_edit.clear()
                        self.text_edit.setText(f.read())
                        self.is_saved = True
            elif choice == QMessageBox.No:
                file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log *.md)')
                if file:
                    with open(file, 'r') as f:
                        self.text_edit.clear()
                        self.text_edit.setText(f.read())
                        self.is_saved = True
            else:
                pass
        else:
            file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log *.md)')
            if file:
                with open(file, 'r') as f:
                    self.text_edit.clear()
                    self.text_edit.setText(f.read())
                    self.is_saved = True

    def save_func(self, text):
        if self.is_saved_first:
            self.save_as_func(text)
        else:
            with open(self.path, 'w') as f:
                f.write(text)
            self.is_saved = True

    def save_as_func(self, text):
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.html *.txt *.log *.md)')
        if self.path:
            with open(self.path, 'w') as f:
                f.write(text)
            self.is_saved = True
            self.is_saved_first = False

    # QCloseEvent.accept()换成了self.close()。QCloseEvent.ignoret()其实功能上就相当于pass
    def close_func(self):
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                self.close()
            elif choice == QMessageBox.No:
                self.close()
            else:
                pass

    # 关闭该软件
    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()

    # 颜色
    """
    记事本涉及到颜色，所以不能调用QTextEdit的toPlainText()方法，
    因为该方法获取的是纯文本，
    所以颜色会丢失掉。应该要调用toHtml()方法保留颜色；
    """

    # self.text_edit.textCursor()方法可以获取到文本编辑框当前的指针(类型为QTextCursor)
    # 调用selection()方法可以获取到指针当前所选择的内容
    # 我们需要再调用toHtml()方法来获取到文本内容
    # 当用户进行剪切后，被剪切的文本肯定要消失，
    # 所以就调用QTextCursor的removeSelectedText()方法
    def cut_func(self):
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)
        self.text_edit.textCursor().removeSelectedText()

    #  copy_action的槽函数如下，方法同理，只不过此时不需要将文本删除：
    def copy_func(self):
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)

    # 在paste_action的槽函数中，我们只需要调用insetHtml()方法将剪贴板中的文本插入即可
    def paste_func(self):
        self.text_edit.insertHtml(self.clipboard.mimeData().html())

    # font_action和color_action的槽函数
    def font_func(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def color_func(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    # about_action所连接的槽函数最为简单，就是打开一个关于Qt的消息框即可
    def about_func(self):
        QMessageBox.aboutQt(self, 'About Qt')

    def about_author_func(self):
        QMessageBox.information(self, '备注：', '作者：红橙', QMessageBox.Cancel)  # 2

    def text_edit_int(self):
        self.text_edit.textChanged.connect(self.text_changed_func)

    def text_changed_func(self):
        if self.text_edit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True


# 开始动画
def start_animation():
    splash = QSplashScreen()
    splash.setPixmap(QPixmap('images/zyx1.jpg'))
    splash.show()
    font = QFont("微软雅黑",16)
    splash.setFont(font)
    splash.showMessage('<font color="blue" size="16">Welcome to Use This PyQt5-Made Notebook~ <br> 向为喜爱的创造一切，不想不爱的人解释一句~</font>',
                       Qt.AlignBottom | Qt.AlignCenter, Qt.white)
    #splash.setFont(QFont("microsoft yahei", 20, QFont::Bold))
    time.sleep(2)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    start_animation()

    demo = Demo()
    demo.show()
    sys.exit(app.exec_())




