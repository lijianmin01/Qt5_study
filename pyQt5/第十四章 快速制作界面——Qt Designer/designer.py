# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(274, 446)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.browser_label = QtWidgets.QLabel(Form)
        self.browser_label.setObjectName("browser_label")
        self.gridLayout.addWidget(self.browser_label, 0, 0, 1, 1)
        self.text_browser = QtWidgets.QTextBrowser(Form)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 1, 0, 1, 1)
        self.edit_label = QtWidgets.QLabel(Form)
        self.edit_label.setTextFormat(QtCore.Qt.RichText)
        self.edit_label.setObjectName("edit_label")
        self.gridLayout.addWidget(self.edit_label, 2, 0, 1, 1)
        self.text_edit = QtWidgets.QTextEdit(Form)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browser_label.setText(_translate("Form", "QTextBrowser"))
        self.edit_label.setText(_translate("Form", "QTextEdit"))
