from PySide.QtCore import *
from PySide.QtGui import *

from classes_becash import *
from numpad_class import Ui_Dialog


class DialogNumPad(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogNumPad, self).__init__()
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
        self.pushButtonPlot.clicked.connect(self.buttonPress)
        self.pushButtonC.clicked.connect(self.clearPass)
        self.bOk.clicked.connect(self.returnValue)

    def clearPass(self):
        self.passLine.setText('')

    def returnValue(self):
        self.inputValue = self.passLine.text()
        self.accept()


    def buttonPress(self):
        clickedButton = self.sender()
        digitValue = clickedButton.text()
        self.passLine.setText(self.passLine.text() + digitValue)


