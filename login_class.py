# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_class.ui'
#
# Created: Thu Feb  9 22:36:03 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 452)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(332, 411))
        Dialog.setMaximumSize(QtCore.QSize(332, 452))
        Dialog.setStyleSheet("QDialog{\n"
"background-image: url(images/logo.png);\n"
"background-repeat:none;\n"
"background-position:top;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius: 10%;\n"
"border-color: rgb(0, 0, 0);\n"
"border:1px solid\n"
"}\n"
"\n"
"QLineEdit{\n"
"\n"
"border-radius: 10%;\n"
"border-color: rgb(0, 0, 0);\n"
"border:1px solid\n"
"}\n"
"")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 90, 311, 361))
        self.widget.setMinimumSize(QtCore.QSize(311, 361))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.widget.setFont(font)
        self.widget.setToolTip("")
        self.widget.setStatusTip("")
        self.widget.setStyleSheet("font: 25pt \"MS Shell Dlg 2\";")
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 271, 96))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.passLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.passLine.setToolTip("")
        self.passLine.setStatusTip("")
        self.passLine.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.passLine.setText("")
        self.passLine.setEchoMode(QtGui.QLineEdit.Password)
        self.passLine.setReadOnly(True)
        self.passLine.setObjectName("passLine")
        self.gridLayout.addWidget(self.passLine, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bDelete = QtGui.QPushButton(self.gridLayoutWidget)
        self.bDelete.setToolTip("")
        self.bDelete.setStatusTip("")
        self.bDelete.setObjectName("bDelete")
        self.horizontalLayout.addWidget(self.bDelete)
        self.bCancel = QtGui.QPushButton(self.gridLayoutWidget)
        self.bCancel.setToolTip("")
        self.bCancel.setStatusTip("")
        self.bCancel.setObjectName("bCancel")
        self.horizontalLayout.addWidget(self.bCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 110, 271, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton7 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout_2.addWidget(self.pushButton7, 0, 0, 1, 1)
        self.pushButton4 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout_2.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton1 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout_2.addWidget(self.pushButton1, 2, 0, 1, 1)
        self.pushButton8 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout_2.addWidget(self.pushButton8, 0, 1, 1, 1)
        self.pushButton9 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout_2.addWidget(self.pushButton9, 0, 2, 1, 1)
        self.pushButton5 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout_2.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton2 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout_2.addWidget(self.pushButton2, 2, 1, 1, 1)
        self.pushButton6 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout_2.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton3 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout_2.addWidget(self.pushButton3, 2, 2, 1, 1)
        self.pushButton0 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout_2.addWidget(self.pushButton0, 3, 0, 1, 1)
        self.pushButtonC = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonC.setObjectName("pushButtonC")
        self.gridLayout_2.addWidget(self.pushButtonC, 3, 1, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.bDelete.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.bCancel.setText(QtGui.QApplication.translate("Dialog", "EXIT", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton7.setText(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton4.setText(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton1.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton8.setText(QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton9.setText(QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton5.setText(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton2.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton6.setText(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton3.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton0.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonC.setText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))

