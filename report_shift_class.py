# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_shift_class.ui'
#
# Created: Thu Feb  9 22:36:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(673, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(10, 50, 650, 421))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(650, 300))
        self.widget.setMaximumSize(QtCore.QSize(800, 600))
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setObjectName("widget")
        self.tableWidget = QtGui.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 411))
        self.tableWidget.setToolTip("")
        self.tableWidget.setStatusTip("")
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeaderItem(0).setText("ID")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeaderItem(1).setText("At")
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeaderItem(2).setText("Operator")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 241, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bClose = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bClose.setObjectName("bClose")
        self.horizontalLayout.addWidget(self.bClose)
        self.closeShift = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.closeShift.setObjectName("closeShift")
        self.horizontalLayout.addWidget(self.closeShift)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Shifts", None, QtGui.QApplication.UnicodeUTF8))
        self.bClose.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.closeShift.setText(QtGui.QApplication.translate("Dialog", "Close shift", None, QtGui.QApplication.UnicodeUTF8))

