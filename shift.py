from PySide.QtCore import *
from PySide.QtGui import *
from report_shift_class import Ui_Dialog

from classes_becash import *
from change import DialogChange


class DialogShiftTable(QDialog,Ui_Dialog):
    def __init__(self,mainWindow):
        super(DialogShiftTable, self).__init__()
        self.maindindow = mainWindow
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.completamSelectul()
        self.bClose.clicked.connect(self.accept)
        self.closeShift.clicked.connect(self.closeShiftQ)
        self.tableWidget.cellDoubleClicked.connect(self.openShiftReport)


    def completamSelectul(self):
        logging.info("-------completamSelectul--------")
        sql = "SELECT *,(SELECT name FROM users WHERE uuid=shift.user) FROM shift ORDER by id  DESC "
        records = query(sql)
        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)

        row =0
        if records:
            for record in records:
                logging.info(record)
                self.tableSetTextRight(self.tableWidget,row,0,record[0])
                # self.tableSetTextRight(self.tableWidget,row,1,record[2])
                self.tableSetTextLeft(self.tableWidget,row,2,record[5])
                self.tableSetTextRight(self.tableWidget,row,1,time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(record[2])))
                # self.tableSetTextRight(self.tableWidget,row,4,record[3])
                # self.tableSetText(self.tableWidget,row,4,record[9])
                row =row +1
        return


    def setData(self, index, value):
        #print ("um clasul principal", index.row(), index.column(), value)
        self.sqlSaveByID(index.row(),index.column(),value)



    def closeShiftQ(self):
        self.maindindow.closeShiftQ()



    def openShiftReport(self,arg):
        logging.info('-----openShiftReport-----')
        schimbulCurentDinTabel =  query("SELECT id AS idd,uuid,user,att,(SELECT att FROM shift WHERE id=idd+1) AS finish  FROM shift  ORDER by id  DESC LIMIT " + str(self.tableWidget.currentRow()) + ",1")
        dialog = DialogChange(self.maindindow.userInfo,schimbulCurentDinTabel[0])
        dialog.exec_()

    def sqlSaveByID(self,row,cell,value):
        cellName =query("SELECT column_name FROM information_schema.columns WHERE table_name='tables'; ")[cell+1][0]
        rowUuid =query("SELECT uuid FROM users "+self.order+" LIMIT "+ str(row) +",1")
        query("UPDATE tables SET "+ str(cellName) + " = '"+ str(value)+"' WHERE uuid='"+ rowUuid[0][0] +"'")

        self.tableWidget.blockSignals(True)
        self.tableSetText(self.tableWidget,row,cell,value)
        self.tableWidget.blockSignals(False)

    def tableSetTextLeft(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignLeft)
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))


    def tableSetTextRight(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignRight)
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))
