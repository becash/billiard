from PySide.QtGui import *
from classes_becash import *
from report_change_class import Ui_Dialog


class DialogChange(QDialog,Ui_Dialog):
    def __init__(self,userInfo,autoreportID=""):


        print(autoreportID)

        super(DialogChange, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        ####DATEPIKER

        self.userInfo=userInfo
        self.autoreportID = autoreportID
        self.reportFrom = PyDateTimeEdit()
        self.gridLayoutDate.addWidget(self.reportFrom,0,1)
        self.reportTo = PyDateTimeEdit()
        self.gridLayoutDate.addWidget(self.reportTo,1,1)
        # self.initiemSelectulLaSchimburi()
        self.setamPerioada()
        self.previewButton.clicked.connect(self.renderHtmlCode)
        self.printButton.clicked.connect(self.preview)
        self.clearButton.clicked.connect(lambda : self.reportPreview.setHtml(''))
        self.renderHtmlCode()


    def setamPerioada(self):
        logging.info("-------setamPerioada-----------")
        current_time = time.localtime()
        if self.autoreportID:
            fromPeriod = QtCore.QDateTime.fromTime_t(self.autoreportID[3])
            if self.autoreportID[4]:
                toPeriod = QtCore.QDateTime.fromTime_t(self.autoreportID[4])
            else:
                toPeriod = QtCore.QDateTime(int(time.strftime('%Y', current_time)), int(time.strftime('%m', current_time)),int(time.strftime('%d', current_time)), 23, 59, 59)
        else:
            ####
            start = query("SELECT att FROM shift ORDER BY id DESC LIMIT 1")[0][0]
            if start :
                fromPeriod  = QtCore.QDateTime.fromTime_t(start)
            else:
                fromPeriod = QtCore.QDateTime(int(time.strftime('%Y', current_time)), int(time.strftime('%m', current_time)), int(time.strftime('%d', current_time)), 0, 0, 0)
            toPeriod  = QtCore.QDateTime.fromTime_t(time.time())


        self.reportFrom.setDateTime(fromPeriod)
        self.reportTo.setDateTime(toPeriod)

        # print(self.autoreportID)
        # print(fromPeriod)
        # print(toPeriod)

    def rendTableHead(self,curTable,curMinuts,curentSumNetto,curentSumBrutto,curentSumDiscount):
        self.htmlRow+="<tr>\
            <th colspan=3 >Sub total: "+ str(curTable) +"</th>\
            <th>"+str(curMinuts/60)+"</th>\
            <th>"+str(round(curentSumBrutto,2))+"</th>\
            <!--th>"+str(round(curentSumDiscount,2))+"</th-->\
            <th>"+str(round(curentSumNetto,2))+"</th>\
              </tr>"

    def renderHtmlCode(self,extended=False):
        rows = query("SELECT o.uuid,o.table_id,o.operator,o.at,o.stoptime,o.payed,o.state,o.row_id,o.sync,o.price1,o.price2,o.price3,o.summ_brutto,o.disc_card,o.disc_percent,o.summ_disc,o.summ_netto,table_id as table_ids,t.name,c.owner,t.salon  FROM orders o \
                     LEFT JOIN tables t ON t.id=o.table_id\
                     LEFT JOIN cards c ON c.id=o.disc_card\
                     WHERE `at`>"+ str(self.reportFrom.dateTime().toTime_t()) +" and stoptime<"+str(self.reportTo.dateTime().toTime_t()) +" and payed=9 and state=0 ORDER BY name" )
        if len(rows)==0:
            self.reportPreview.setHtml("<h1>No records</h1>")
            return "<h1>No records</h1>"

        self.htmlRow = ''
        curTable = rows[0][13]
        curMinuts =0
        curentSumNetto =0
        curentSumDiscount = 0
        curentSumBrutto = 0
        totalMinuts =0
        totalTotalNetto =0
        totalTotalDisc =0
        totalTotalBrutto =0

        for tab in rows:
            logging.info("Taburile:"+str(tab))
            if not curTable == tab[13]:
                # self.rendTableHead(curTable,curMinuts,curentSumNetto,curentSumBrutto,curentSumDiscount)
                curTable=tab[13]
                totalMinuts += curMinuts
                totalTotalNetto += curentSumNetto
                totalTotalDisc += curentSumDiscount
                totalTotalBrutto += curentSumBrutto
                curMinuts =0
                curentSumNetto =0
                curentSumDiscount =0
                curentSumBrutto =0

            #cardul
            if tab[19]:
                tabOnwer = str(tab[19])
            else:
                tabOnwer = ''

            self.htmlRow+="<tr  style='border-bottom: 1px solid black;font-size:19px'>\
                    <td ><b >"+ str(tab[18])+ "<br/>"  + str(tab[7])+"</b></td>\
                    <td ><b>"+ str(time.strftime("%H:%M", time.localtime(tab[3])))+ "<br/>"+ str(time.strftime("%H:%M", time.localtime(tab[4])))+"</b></td>\
                    <td ><b>"+ str(round(int(tab[4]-tab[3])/60))+"<br/>"+ str(tab[12])+"</b></td>\
                    <td ><b>"+ tabOnwer+"<br/>"+str(tab[14])+"</b></td>\
                    <!--td ><b>" + str(tab[15]) + "</b></td-->\
                    <td ><b>"+ str(tab[16])+"</b></td>\
                    </tr>"





            curMinuts += int(tab[4]-tab[3])
            curentSumNetto += float(tab[16])
            curentSumDiscount += float(tab[15])
            curentSumBrutto += float(tab[12])


        # self.rendTableHead(curTable,curMinuts,curentSumNetto,curentSumBrutto,curentSumDiscount)

        totals ="<tr>\
            <th colspan=2><!--h3>Total:</h3--></th>\
            <th><h2>"+str((totalMinuts + curMinuts)/60)+"</h2></th>\
            <th></th>\
            <!--th><h3>"+str(round(totalTotalDisc+ curentSumDiscount,2))+"</h3></th-->\
            <th><h3>"+str(round(totalTotalNetto + curentSumNetto,2))+"</h3></th>\
              </tr>"

        htmlHead="""
                    <script>
                    //alert(location.href)
                    </script>

                     <style type="text/css">
                     body{
                     font-family:  Arial,  sans-serif;
                     }
                     TABLE {
                        width: 100%; /* Ширина таблицы */
                       /* border: 1px solid black; /* Рамка вокруг таблицы */
                        background: #ffffff; /* Цвет фона таблицы */
                       }
                       TD, TH {
                        text-align: center; /* Выравнивание по центру */
                        padding: 3px; /* Поля вокруг содержимого ячеек */
                       }
                       TH {
                        background: rgb(255, 252, 200); /* Цвет фона */
                        color: #000000; /* Цвет текста */
                        border-bottom: 1px solid black; /* Линия снизу */
                       }
                       .lc {
                        font-weight: bold; /* Жирное начертание текста */
                        text-align: left; /* Выравнивание по левому краю */
                       }
                       h1{
                       line-height:20px
                       }
                       p, h1,table {
                       font-family: arial;
                       }
                      </style>
                    """
        htmlAntet="<h1>Shift report</h1>\
        <h2>From: "+self.reportFrom.text()+"</h2>\
        <h2>To: "+self.reportTo.text()+"</h2>\
        <h2>Printed :"+str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time())))+"</h2>\
        <h2>Operator: "+self.userInfo[1]+"</h2>"




        if extended:
            displayTable = ''
        else:
            displayTable = 'display:none'

        htmlBoby="""<table style='"""    +   displayTable  +  """' >
              <thead>
              <tr  style='border-bottom: 1px solid black;font-size:19px'>
               <th>Table<hr/>Order</th>
               <th>Clock</th>
               <th>Mins<hr/>Sum</th>
               <th>Card<hr/>%</th>
               <!--th>Discount <br/>sum</th-->
               <th>Total</th>
              </tr>
             </thead>
        """ +self.htmlRow+ totals +"</table> <hr/>"


        #footerul,  de desupt la raport
        #footerul,  de desupt la raport
        htmlFooter = """
        <h1>Payments</h1>
        <table style='border:none;font-weight: 900;'  >
        """

        #tabelul payments_types
        payments_types = query("SELECT SUM(p.sum) as summa, t.name \
                               FROM payments p  \
                               LEFT JOIN orders o ON o.uuid = p.parent_order \
                               LEFT JOIN payments_types t ON t.id = p.payment_typ\
                               WHERE o.at>"+ str(self.reportFrom.dateTime().toTime_t()) +" and o.at<"+str(self.reportTo.dateTime().toTime_t()) +"  GROUP BY t.id  ")
        if len(rows) == 0:
            return
        payments_types_total = 0
        for rowww in payments_types:
            payments_types_total += rowww[0]
            htmlFooter +="<tr>\
            <td><h2>"+rowww[1]+"</h2></td>\
            <td><h2>"+ str(rowww[0]) +"</h2></td>\
                </tr>"

        htmlFooter+="""
        <tr>
            <td  style='border-top: 1px solid black;'  ><h2>Total</h2></td>
            <td   style='border-top: 1px solid black;' ><h2>"""+str(payments_types_total) +"""</h2></td>
        </tr>
        </table>

        <h2>Tables</h2>
        <table  style='border:none' >

        """
        #tabelul tables
        tables_table = query("SELECT SUM(summ_netto) AS summ,(SELECT name FROM tables WHERE id=orders.table_id) AS tableName FROM orders WHERE  `at`>"+ str(self.reportFrom.dateTime().toTime_t()) +" and `at`<"+str(self.reportTo.dateTime().toTime_t()) +"  GROUP BY table_id ")
        if len(rows) == 0:
            return
        tables_total = 0
        for rowww in tables_table:
            tables_total+= rowww[0]
            htmlFooter +="<tr>\
            <td><h2>"+rowww[1]+"</h2></td>\
            <td><h2>"+str(rowww[0])+"</h2></td>\
                </tr>"

        htmlFooter+="""
        <tr>
            <td  style='border-top: 1px solid black;'><h2>Total</h2></td>
            <td  style='border-top: 1px solid black;'><h2>"""+str(tables_total)+"""</h2></td>
        </tr>
        </table>

        <hr/>
        <h2>Printed:""" + str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time()))) + """</h2>
        """

        finalHTML = htmlHead+htmlAntet+htmlBoby+htmlFooter

        self.reportPreview.setHtml(finalHTML)
        return finalHTML

    def preview(self):
        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.reportPreview.print_(p))

        preview.exec_()

