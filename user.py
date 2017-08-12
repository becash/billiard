from PySide.QtCore import *
from PySide.QtGui import *
from user_class import Ui_Dialog

from classes_becash import *


class DialogUser(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogUser, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.order =' ORDER by `level`,`name` ASC'
        self.completamSelectul()
        self.tableWidget.cellDoubleClicked.connect(self.saveCellChange)

        #conectam  signalele
        # self.connect(self.select_, SIGNAL("currentIndexChanged(QString)"), self.selectChange)
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.bDelete, SIGNAL("clicked()"), self.deleteUser)
        self.connect(self.bInsert, SIGNAL("clicked()"), self.dialogOpen)


    def completamSelectul(self):
        sql = "SELECT * FROM users "+self.order
        records = query(sql)
        self.tableWidget.setRowCount(len(records))
        row =0
        if records:
            for record in records:
                self.tableWidget.blockSignals(True)
                self.tableSetText(self.tableWidget,row,0,record[1])
                #self.tableWidget.setItemDelegateForColumn(1, ComboDelegate(self,userLevels))
                self.tableSetText(self.tableWidget,row,1,userLevels[int(record[2])])
                self.tableSetText(self.tableWidget,row,2,record[3])
                #self.tableSetText(self.tableWidget,row,3,record[4])
                self.tableSetText(self.tableWidget,row,3,record[5])
                #self.tableWidget.setItemDelegateForColumn(4, ComboDelegate(self,selectBool))
                self.tableWidget.blockSignals(False)
                row =row +1
        #self.tableWidget.itemChanged.connect(self.saveCellChange)
        return


    def setData(self, index, value):
        #print ("um clasul principal", index.row(), index.column(), value)
        self.sqlSaveByID(index.row(),index.column(),value)

    def saveCellChange(self,arg):
        dialog = Dialog2()
        userData =query("SELECT * FROM users "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
        #logging.info(userData)
        dialog.uuid.setText(str(userData[0][0]))
        dialog.userNameLine.setText(str(userData[0][1]))
        dialog.prescurtarea_2.setText(str(userData[0][3]))
        dialog.lineEdit.setText(str(userData[0][4]))
        dialog.userLevel.setCurrentIndex(int(userData[0][2]))
        dialog.checkBox.setChecked(int(userData[0][5]))
        if dialog.exec_():
            self.completamSelectul()
        #self.sqlSaveByID(arg.row(),arg.column(),arg.text())


    def deleteUser(self):
        quit_msg = "Are you sure?"
        reply = QtGui.QMessageBox.question(self, 'Confirm', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            rowUuid =query("SELECT uuid FROM users "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
            query("DELETE FROM users WHERE uuid = '"+ rowUuid[0][0] +"'")
            self.completamSelectul()




    def sqlSaveByID(self,row,cell,value):
        cellName =query("SELECT column_name FROM information_schema.columns WHERE table_name='users'; ")[cell+1][0]
        rowUuid =query("SELECT uuid FROM users "+self.order+" LIMIT "+ str(row) +",1")
        query("UPDATE users SET "+ str(cellName) + " = '"+ str(value)+"' WHERE uuid='"+ rowUuid[0][0] +"'")

        self.tableWidget.blockSignals(True)
        self.tableSetText(self.tableWidget,row,cell,value)
        self.tableWidget.blockSignals(False)

    def tableSetText(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))

################## Creare user nou
    def dialogOpen(self):
        dialog = Dialog2()
        if dialog.exec_():
            self.completamSelectul()

#######################################  DIALOGUL __NEW USER
from user_new_class import Ui_Dialog
class Dialog2(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)
        self.userLevel.addItems(userLevels)
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        self.bDelete.clicked.connect(self.validateNewUserForm)


    def validateNewUserForm(self):
        #numele la utilizator shi parola
        # logging.info("Username is " + str(self.userNameLine.text()))
        # logging.info("Level is " + str(self.userLevel.currentIndex()))
        # logging.info("Notes is " + str(self.prescurtarea_2.text()))
        # logging.info("Pass is " + str(self.lineEdit.text()))
        # logging.info("Active is " + str(self.checkBox.isChecked()))
        if  len(query("SELECT * FROM users WHERE pass='"+ self.lineEdit.text()+"'and uuid !='"+self.uuid.text() +"'" )) :
            QtGui.QMessageBox.warning(self, appName, "Password Error,  Please use another password")
            return


        if len(str(self.userNameLine.text())) > 3 and  len(str(self.lineEdit.text())) >= 1:
            if len(str(self.uuid.text())) and  len((query("SELECT * FROM users WHERE uuid='"+ self.uuid.text()+"'"))) :
                query("UPDATE users SET name='"+ self.userNameLine.text()+ "', level='"+
                      str(self.userLevel.currentIndex())+ "', notes='"+self.prescurtarea_2.text() + "', pass='"+
                      self.lineEdit.text()+ "',enable='"+ str(int(self.checkBox.isChecked())) +"'  WHERE uuid='"+ str(self.uuid.text()) + "'")
                self.accept()
            else:
                if len(self.uuid.text()):
                    uuid = self.uuid.text()
                else:
                    uuid = getNewSID()
                query("INSERT INTO users VALUES ('"+uuid + "','"+ self.userNameLine.text()+ "','"+
                      str(self.userLevel.currentIndex())+ "','"+self.prescurtarea_2.text() + "','"+
                      self.lineEdit.text()+ "','"+ str(int(self.checkBox.isChecked())) +"')")
                self.accept()
        else:
            logging.info("verificati forma, POATE PAROLA DEJA EXISTA IN TABELA,  LA ALT USER")

