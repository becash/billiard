from PySide.QtCore import *
from PySide.QtGui import *
from cards_class import Ui_Dialog

from classes_becash import *


class DialogCards(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogCards, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.order =' ORDER by `id`'
        self.completamSelectul()
        self.tableWidget.cellDoubleClicked.connect(self.saveCellChange)

        #conectam  signalele
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.bDelete, SIGNAL("clicked()"), self.deleteCard)
        self.connect(self.bInsert, SIGNAL("clicked()"), self.dialogOpen)


    def completamSelectul(self):
        sql = "SELECT * FROM cards "+self.order
        records = query(sql)
        self.tableWidget.setRowCount(len(records))
        row =0
        if records:
            for record in records:
                self.tableWidget.blockSignals(True)
                self.tableSetText(self.tableWidget,row,0,record[0])
                #self.tableWidget.setItemDelegateForColumn(1, ComboDelegate(self,cardLevels))
                self.tableSetText(self.tableWidget,row,3,selectBool[int(record[3])])
                self.tableSetText(self.tableWidget,row,1,record[1])
                self.tableSetText(self.tableWidget,row,2,record[2])
                self.tableWidget.blockSignals(False)
                row =row +1
        return


    def setData(self, index, value):
        #print ("um clasul principal", index.row(), index.column(), value)
        self.sqlSaveByID(index.row(),index.column(),value)

    def saveCellChange(self,arg):
        dialog = Dialog2()
        cardData =query("SELECT * FROM cards "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
        
        dialog.uuid =cardData[0][4]
        dialog.cardNumber.setText(str(cardData[0][0]))
        dialog.onwerNameLine.setText(str(cardData[0][1]))
        dialog.discount.setText(str(cardData[0][2]))
        dialog.active.setChecked(int(cardData[0][3]))
        if dialog.exec_():
            self.completamSelectul()
        #self.sqlSaveByID(arg.row(),arg.column(),arg.text())


    def deleteCard(self):
        quit_msg = "Are you sure?"
        reply = QtGui.QMessageBox.question(self, 'Confirm', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            rowUuid =query("SELECT uuid FROM cards "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
            query("DELETE FROM cards WHERE uuid = '"+ rowUuid[0][0] +"'")
            self.completamSelectul()




    def sqlSaveByID(self,row,cell,value):
        cellName =query("SELECT column_name FROM information_schema.columns WHERE table_name='cards'; ")[cell+1][0]
        rowUuid =query("SELECT uuid FROM cards "+self.order+" LIMIT "+ str(row) +",1")
        query("UPDATE cards SET "+ str(cellName) + " = '"+ str(value)+"' WHERE uuid='"+ rowUuid[0][0] +"'")

        self.tableWidget.blockSignals(True)
        self.tableSetText(self.tableWidget,row,cell,value)
        self.tableWidget.blockSignals(False)

    def tableSetText(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))

################## Creare card nou
    def dialogOpen(self):
        dialog = Dialog2()
        dialog.uuid = ""
        if dialog.exec_():
            self.completamSelectul()

#######################################  DIALOGUL __NEW card
from cards_new_class import Ui_Dialog
class Dialog2(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        self.bOk.clicked.connect(self.validateNewcardForm)


    def validateNewcardForm(self):
        if  len(query("SELECT * FROM cards WHERE id='"+ self.cardNumber.text()+"'  AND  uuid !='"+ str(self.uuid)+"'" )) :
            QtGui.QMessageBox.warning(self, appName, "Card ID exist. Use another")
            return


        if len(str(self.cardNumber.text())) > 1 and  len(str(self.onwerNameLine.text())) >= 1:
            if len(str(self.uuid)) and  len((query("SELECT * FROM cards WHERE uuid='"+ self.uuid+"'"))) :
                query("UPDATE cards SET owner='"+ self.onwerNameLine.text()+ "', id='"+self.cardNumber.text() + "', enable='"+ str(int(self.active.isChecked())) +"'  WHERE uuid='"+ str(self.uuid) + "'")
                self.accept()
            else:
                if len(self.uuid):
                    uuid = self.uuid
                else:
                    uuid = getNewSID()
                query("INSERT INTO cards VALUES ('"+self.cardNumber.text() + "','"+ self.onwerNameLine.text()+ "','"+ str(self.discount.text())+ "','"+ str(int(self.active.isChecked())) +"','"  +  uuid+   "')")
                self.accept()
        else:
            logging.info("verificati forma, POATE CARDUL DEJA EXISTA IN TABELA")

