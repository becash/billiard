from PySide.QtCore import *
from PySide.QtGui import *

from classes_becash import *
from login_class import Ui_Dialog


class DialogLogin(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogLogin, self).__init__()
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.setupUi(self)
        self.conectSignals()


    def conectSignals(self):
        self.pushButton0.clicked.connect(self.buttonPress)
        self.pushButton1.clicked.connect(self.buttonPress)
        self.pushButton2.clicked.connect(self.buttonPress)
        self.pushButton3.clicked.connect(self.buttonPress)
        self.pushButton4.clicked.connect(self.buttonPress)
        self.pushButton5.clicked.connect(self.buttonPress)
        self.pushButton6.clicked.connect(self.buttonPress)
        self.pushButton7.clicked.connect(self.buttonPress)
        self.pushButton8.clicked.connect(self.buttonPress)
        self.pushButton9.clicked.connect(self.buttonPress)
        self.pushButtonC.clicked.connect(self.clearPass)
        self.bDelete.clicked.connect(self.checkPass)
        self.bCancel.clicked.connect(self.exitProgram)

    def clearPass(self):
        self.passLine.setText('')


    def exitProgram(self):
        self.userINfo = query("SELECT * FROM users WHERE pass='"+ self.passLine.text()  +"'and enable=1 LIMIT 1")
        if len(self.userINfo):
            self.exitCode = 'exit'
            self.accept()

        else:
            self.passLine.clear()
            msgBox = QMessageBox()
            msgBox.setWindowTitle(appName)
            msgBox.setText("Password ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def buttonPress(self):
        clickedButton = self.sender()
        digitValue = clickedButton.text()
        self.passLine.setText(self.passLine.text() + digitValue)

    def checkPass(self):
        self.userINfo = query("SELECT * FROM users WHERE pass='"+ self.passLine.text()  +"'and enable=1 LIMIT 1")
        if len(self.userINfo):
            self.exitCode = 'login'
            self.accept()
        else:
            msgBox = QMessageBox()
            self.passLine.setText('')
            msgBox.setWindowTitle(appName)
            msgBox.setText("Password ERROR")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()

    def closeEvent(self,event):
        event.ignore()
        self.exitProgram()

