# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_new_class.ui'
#
# Created: Thu Feb  9 22:36:04 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 362)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(332, 100))
        Dialog.setMaximumSize(QtCore.QSize(332, 500))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 158, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bDelete = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bDelete.setToolTip("")
        self.bDelete.setStatusTip("")
        self.bDelete.setObjectName("bDelete")
        self.horizontalLayout.addWidget(self.bDelete)
        self.bCancel = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bCancel.setToolTip("")
        self.bCancel.setStatusTip("")
        self.bCancel.setObjectName("bCancel")
        self.horizontalLayout.addWidget(self.bCancel)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 311, 311))
        self.groupBox.setToolTip("")
        self.groupBox.setStatusTip("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 311, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_4.setToolTip("")
        self.l_4.setStatusTip("")
        self.l_4.setAlignment(QtCore.Qt.AlignCenter)
        self.l_4.setObjectName("l_4")
        self.gridLayout.addWidget(self.l_4, 0, 0, 1, 1)
        self.userNameLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.userNameLine.setObjectName("userNameLine")
        self.gridLayout.addWidget(self.userNameLine, 1, 1, 1, 1)
        self.controlerOFF = QtGui.QLineEdit(self.gridLayoutWidget)
        self.controlerOFF.setObjectName("controlerOFF")
        self.gridLayout.addWidget(self.controlerOFF, 6, 1, 1, 1)
        self.l_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_3.setToolTip("")
        self.l_3.setStatusTip("")
        self.l_3.setAlignment(QtCore.Qt.AlignCenter)
        self.l_3.setObjectName("l_3")
        self.gridLayout.addWidget(self.l_3, 1, 0, 1, 1)
        self.uuid = QtGui.QLineEdit(self.gridLayoutWidget)
        self.uuid.setReadOnly(True)
        self.uuid.setObjectName("uuid")
        self.gridLayout.addWidget(self.uuid, 0, 1, 1, 1)
        self.controlerON = QtGui.QLineEdit(self.gridLayoutWidget)
        self.controlerON.setObjectName("controlerON")
        self.gridLayout.addWidget(self.controlerON, 5, 1, 1, 1)
        self.l_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_5.setAlignment(QtCore.Qt.AlignCenter)
        self.l_5.setObjectName("l_5")
        self.gridLayout.addWidget(self.l_5, 6, 0, 1, 1)
        self.prescurtarea_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.prescurtarea_2.setObjectName("prescurtarea_2")
        self.gridLayout.addWidget(self.prescurtarea_2, 3, 1, 1, 1)
        self.l = QtGui.QLabel(self.gridLayoutWidget)
        self.l.setToolTip("")
        self.l.setStatusTip("")
        self.l.setAlignment(QtCore.Qt.AlignCenter)
        self.l.setMargin(10)
        self.l.setObjectName("l")
        self.gridLayout.addWidget(self.l, 3, 0, 1, 1)
        self.l_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_7.setToolTip("")
        self.l_7.setStatusTip("")
        self.l_7.setAlignment(QtCore.Qt.AlignCenter)
        self.l_7.setMargin(10)
        self.l_7.setObjectName("l_7")
        self.gridLayout.addWidget(self.l_7, 2, 0, 1, 1)
        self.l_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_2.setToolTip("")
        self.l_2.setStatusTip("")
        self.l_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_2.setObjectName("l_2")
        self.gridLayout.addWidget(self.l_2, 4, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 9, 1, 1, 1)
        self.l_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_6.setAlignment(QtCore.Qt.AlignCenter)
        self.l_6.setObjectName("l_6")
        self.gridLayout.addWidget(self.l_6, 5, 0, 1, 1)
        self.userLevel = QtGui.QComboBox(self.gridLayoutWidget)
        self.userLevel.setObjectName("userLevel")
        self.gridLayout.addWidget(self.userLevel, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_9.setObjectName("l_9")
        self.horizontalLayout_2.addWidget(self.l_9)
        self.price1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.price1.setObjectName("price1")
        self.horizontalLayout_2.addWidget(self.price1)
        self.l_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_8.setObjectName("l_8")
        self.horizontalLayout_2.addWidget(self.l_8)
        self.price2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.price2.setObjectName("price2")
        self.horizontalLayout_2.addWidget(self.price2)
        self.l_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_10.setObjectName("l_10")
        self.horizontalLayout_2.addWidget(self.l_10)
        self.price3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.price3.setObjectName("price3")
        self.horizontalLayout_2.addWidget(self.price3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)
        self.controlerName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.controlerName.setObjectName("controlerName")
        self.gridLayout.addWidget(self.controlerName, 7, 1, 1, 1)
        self.controlerUrl = QtGui.QLineEdit(self.gridLayoutWidget)
        self.controlerUrl.setObjectName("controlerUrl")
        self.gridLayout.addWidget(self.controlerUrl, 8, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Table editor", None, QtGui.QApplication.UnicodeUTF8))
        self.bDelete.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.bCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Table data", None, QtGui.QApplication.UnicodeUTF8))
        self.l_4.setText(QtGui.QApplication.translate("Dialog", "UUID", None, QtGui.QApplication.UnicodeUTF8))
        self.l_3.setText(QtGui.QApplication.translate("Dialog", "Table name", None, QtGui.QApplication.UnicodeUTF8))
        self.l_5.setText(QtGui.QApplication.translate("Dialog", "COM OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.l.setText(QtGui.QApplication.translate("Dialog", "Order", None, QtGui.QApplication.UnicodeUTF8))
        self.l_7.setText(QtGui.QApplication.translate("Dialog", "Salon", None, QtGui.QApplication.UnicodeUTF8))
        self.l_2.setText(QtGui.QApplication.translate("Dialog", "Prices", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.l_6.setText(QtGui.QApplication.translate("Dialog", "COM ON", None, QtGui.QApplication.UnicodeUTF8))
        self.l_9.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.l_8.setText(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.l_10.setText(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Controler name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Controler url", None, QtGui.QApplication.UnicodeUTF8))

