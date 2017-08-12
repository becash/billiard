from PySide.QtGui import *
import printer, math
from functions import  *
from pay_class import Ui_Dialog
from numpad import DialogNumPad
from cash_register import *




class DialogPay(QDialog, Ui_Dialog):

    def __init__(self,id,mainWindow):
        super(DialogPay, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.maindindow = mainWindow

        self.setWindowIcon(QIcon('images/circle_red.png'))
        self.setWindowTitle("Dialog.")
        self.setupUi(self)
        self.id =id
        self.setVariables()
        self.conectSignals()
        self.inputSumm.selectAll()
        self.focusedLineEditName = ""
        self.firstClean =1
        self.cardDetails = []
        self.cardId= "0"
        self.cardCode.textChanged.connect(self.onCardCodeChange)
        self.cardPercent.textChanged.connect(self.onCardPercentChange)



        ##validate  la inputsumm
        rectExp = QtCore.QRegExp()
        rectExp.setPattern('^[1-9]\d*(?:\.\d{0,2})?$')
        validator = QRegExpValidator(rectExp,self.inputSumm)
        self.inputSumm.setValidator(validator)
        self.inputSumm.setFocus()




    def buttonClick(self,arg):
        self.remain= self.remain + arg
        self.addToTime = self.addToTime + arg
        self.timeRemain.setText(time.strftime("%H:%M", time.gmtime(self.remain)))

    def setVariables(self):
        paymentsType = query("SELECT `name` FROM payments_types ORDER by id")
        for type  in paymentsType:
            self.paymentType.addItem(type[0])
        self.orderDetails =query("SELECT * FROM orders  WHERE row_id="+str(self.id))[0]
        self.uuid = self.orderDetails[0]

        if float(self.orderDetails[16]) == float(0):
            sums = math.ceil( float (self.orderDetails[12]))
        else:
            sums = math.ceil(  float( self.orderDetails[16]))

        avansuri = query("SELECT sum FROM payments  WHERE parent_order='"+self.uuid +"'")
        self.avans=float(0)
        for i in avansuri:
            self.avans+=float(i[0])

        self.datorie=  math.ceil( sums - self.avans)
        self.labelAvans.setText(str(self.avans))# avans   pentru  joaca
        self.sumForGame.setText(str(self.orderDetails[12]))# suma   pentru  joaca
        self.paymentOrder.setText(str(self.id))
        self.cardPercent.setText(str(self.orderDetails[14]))

        if  self.orderDetails[13] != "" and  int(self.orderDetails[13]) != 0  :
            self.cardDetails = query("SELECT * FROM cards  WHERE  enable=1 AND   id=" + str(self.orderDetails[13]))
            if(len(self.cardDetails)):

                # self.cardPercent.setDisabled(True)
                self.cardCode.setText(str(self.cardDetails[0][0]))
                # self.cardCode.setDisabled(True)
                self.onwerValue.setText(self.cardDetails[0][1])
                self.cardId = self.cardDetails[0][0]
                self.cardDetails = []





        self.recalculamValorileCompurilor()

    def conectSignals(self):
        self.pushButtonOK.clicked.connect(self.saveChanges)
        self.focusCardPercent.clicked.connect(self.padCardPercent)
        self.focusCardCode.clicked.connect(self.padCardCode)
        self.focusSumTotal.clicked.connect(self.padSumTotal)



    def padCardPercent(self):
        dialog = DialogNumPad()
        if dialog.exec_():
            self.cardPercent.setText(dialog.inputValue)

    def padCardCode(self):
        dialog = DialogNumPad()
        if dialog.exec_():
            self.cardCode.setText(dialog.inputValue)

    def padSumTotal(self):
        dialog = DialogNumPad()
        if dialog.exec_():
            self.inputSumm.setText(dialog.inputValue)


    def buttonPress(self):
        if self.firstClean:
            self.clearPass()
            self.firstClean=0
        clickedButton = self.sender()
        digitValue = clickedButton.text()

        if self.focusSumTotal.isChecked():
            if  self.inputSumm.text() == '' and digitValue == 0.0:
                return
            self.inputSumm.setText(self.inputSumm.text() + digitValue)
            return

        if self.focusCardCode.isChecked():
            self.cardCode.setText(self.cardCode.text() + digitValue)
            return

        if self.focusCardPercent.isChecked():
            self.cardPercent.setText(self.cardPercent.text() + digitValue)
            return


    def onCardCodeChange(self):
        self.cardPercent.blockSignals(True)
        self.cardDetails = []
        self.cardPercent.setText("0")
        if self.cardCode.text()!="":
            self.onwerValue.setText("")
            self.cardDetails = query("SELECT * FROM cards  WHERE enable=1 AND   id=" + str(self.cardCode.text()))
            if(len(self.cardDetails)):
                self.cardPercent.setText(str(self.cardDetails[0][2]))
                self.onwerValue.setText(self.cardDetails[0][1])
                self.cardId = self.cardDetails[0][0]
                self.cardDetails = []

        self.recalculamValorileCompurilor()
        self.cardPercent.blockSignals(False)

    def onCardPercentChange(self):
        self.cardCode.blockSignals(True)
        if int(self.cardPercent.text())> 100:
            eroarePopup("Discount  cannot be bigger 100%")
            self.cardPercent.setText("")

        if self.cardPercent.text() != ""  and len(self.cardDetails)==0:
            self.onwerValue.setText("")
            self.cardCode.setText("")
            self.cardId = "0"
        self.recalculamValorileCompurilor()
        self.cardCode.blockSignals(False)


    def recalculamValorileCompurilor(self):
        if self.cardPercent.text()!= "":
            self.labelTotal.setText(str(      math.ceil(  float( self.orderDetails[12]) * float(   1 - (int(self.cardPercent.text())*0.01)))       ))  #  suma  care trebuie achitatta
            self.inputSumm.setText(str(      math.ceil(  float( self.orderDetails[12]) * float(   1 - (int(self.cardPercent.text())*0.01))  - self.avans    )       ))  #  suma  care trebuie achitatta
            self.dicountSumm.setText(        str(  math.floor(  float( self.orderDetails[12]) * float(   (int(self.cardPercent.text())*0.01))    )    ))
        else:
            self.labelTotal.setText(str(self.datorie)) #  suma  care trebuie achitatta
            self.inputSumm.setText(str(self.datorie))  #  suma  care trebuie achitatta
            self.dicountSumm.setText( "0")


    def saveChanges(self):
            try:
                if self.cardPercent.text()=="":
                    cardPercent = "0"
                else:
                    cardPercent = self.cardPercent.text()
                paymentID =  query("INSERT INTO payments VALUES (NULL ,'"+ self.uuid +"',\
                                    IF(((SELECT id FROM payments_types ORDER BY id LIMIT "+ str(self.paymentType.currentIndex()) +",1)=101),0, (SELECT id FROM payments_types ORDER BY id LIMIT "+ str(self.paymentType.currentIndex()) +",1)   )  ,\
                                              "+str(self.inputSumm.text())+",0)")
            except Exception as e:

                logging.critical("EROARE LA PLATA")
                logging.critical(str(e))
                eroarePopup("Error on register payment")
                raise
            else:

                # print(self.datorie)
                # print(self.dicountSumm.text())
                # print(self.inputSumm.text())

                # punem 3(partial acitat), sau 9(achitat complet)??????????????????????????????????
                if float(  float(self.datorie)  - float(self.dicountSumm.text())  ) <= float(self.inputSumm.text()) +1  :
                    payed = "9"
                else:
                    payed = "3"

                ##verificam  daca e cu reducere
                if self.cardPercent.text()=="":
                    disc_card = "0"
                    disc_percent = "0"
                    summ_disc = "0"
                    summ_netto = self.orderDetails[12]
                else:
                    disc_card = self.cardCode.text()
                    disc_percent = self.cardPercent.text()
                    summ_disc = self.dicountSumm.text()
                    summ_netto = str(  float(self.orderDetails[12]) - float(self.dicountSumm.text()))


                qSting ="UPDATE orders SET payed='"+ payed+"' , disc_card='"+ str(disc_card) +"' , disc_percent='"+str (disc_percent)+"' , summ_disc='"+str(summ_disc )+"' , summ_netto='"+ str(  summ_netto  ) +"'   WHERE uuid='" + str(self.uuid)+"'"
                query(qSting)

                self.orderDetails = query("SELECT * FROM orders  WHERE row_id=" + str(self.id))[0]

                #tiparim chekul  fiscal,      CREEM  FISHIER

                checkFiscal = int(query("SELECT cash_reg FROM payments_types ORDER BY id LIMIT "+ str(self.paymentType.currentIndex()) +",1")[0][0])
                if checkFiscal:
                     if printGameCheck(self.inputSumm.text()) :

                         query("UPDATE payments SET  cash_reg=1   WHERE id=" + str(paymentID))

                #tipatim  chekul nefiscal
                try:
                    printerClass = printer.PrinterClass()
                    printerClass.printCheck(self)
                except:
                    self.close()
                    raise



