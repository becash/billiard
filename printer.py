import sys,time,base64
from PySide import QtGui,QtWebKit
from functions import *
from classes_becash import salons

########PRINT ORDER CLAS
#####extragerea   fin  forma  a argumentelor  PODUL DINTRE >>> JAVASCRIPT  SHI >>>PYTHON
class PrinterClass():
    def __init__(self):
        # super(PrinterClass, self).__init__(None)
        self.printer = QtGui.QPrinter()
        self.printer.setPrinterName(query("SELECT value FROM settings WHERE id=51")[0][0])  # DENUMIREA PRINTERULUI    "MGPOS TM-80(USB)"
        self.printer.setPageMargins(0, 0, 12, 0, QtGui.QPrinter.Millimeter)
        self.webView = QtWebKit.QWebView()
        self.webView.loadFinished.connect(self.handlePrint)


    def handlePrint(self):
        # print("Check printed")
        logging.info("Check printed")
        i = 0
        while i < int(query("SELECT value FROM settings WHERE id=52")[0][0]):
            i = i + 1
            self.webView.print_(self.printer)

#####tiparim  CHECK



    def printCheck(self,mainWindow):
        img_file = "images/invoice.jpg"
        b64 = base64.encodebytes(open(img_file, "rb").read())
        # timesss = str(time.time())
        # self.html = '<html><body><h1>'+timesss +'</h1><img style="display:block; width:100%;height:100px;" src="data:image/bmp;base64,'+b64.decode("utf8") +'"><h1>'+timesss +'</h1></body></html>'
        minuteTarif1 =0
        minuteTarif2 =0
        minuteTarif3 =0

        finish = mainWindow.orderDetails[4]
        if finish == None:
            finish = int(time.time())
        summa = 0
        while finish > mainWindow.orderDetails[3]:

            periadaMinutei = getPeriodByTime(finish)
            if periadaMinutei ==0:
                minuteTarif1 += 1

            if periadaMinutei ==1:
                minuteTarif2 += 1

            if periadaMinutei ==2:
                minuteTarif3 +=1
            finish -= 60


        self.html = """
<style>
    body{
        font-family: arial;
    }
    table{
        border-spacing:0;
    }
    .swRepColHdrRow>th,.swRepColHdrRow>td,{
        width: 20%;
        text-align:left !important;
    }
    .swRepResultLine>td{
        text-align:right !important;
    }


    thead{
        /*background-color: aquamarine;*/
    }
    tfoot{
        /*background-color: aquamarine;*/
    }
    .swRepTitle {
        font-size: 18pt;
        text-align: center;
        margin: 0px !important;
        padding-bottom: 10px;
        padding-top: 20px;
        border-bottom: 1px solid #d0ccc9;
        padding-left: 20px;
    }
    td{
       /* border: 1px solid;*/
    }


    #details th{
       /* border: 1px solid;*/
    }

    img{
        width: 100%;
    }


    .descript{
        margin: auto;
         text-align: center;
         font-weight:100;
    }

</style><img style="display:block; width:100%;height:100px;" src="data:image/jpeg;base64,"""  +b64.decode("utf8") +"""">

<h1 style="margin: auto; text-align: center">Nota de plata</h1>
<h4 class="descript">Nr.""" +  str( mainWindow.orderDetails[7])  + """  Data """ + time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(mainWindow.orderDetails[3])) + """</h4>
<hr/>
<h4 class="descript">""" +  str(query("SELECT value FROM settings WHERE id=30")[0][0])   +  """</h4>
<h4 class="descript">""" +  str(query("SELECT value FROM settings WHERE id=31")[0][0])   +  """</h4>
<h4 class="descript">""" +  str(query("SELECT value FROM settings WHERE id=32")[0][0] )  +  """</h4>


<h3  style="margin: auto; text-align: center">Masa """ +  str(    query("SELECT name FROM tables WHERE id="+str(mainWindow.orderDetails[1]))[0][0]     )    +  """   sala:"""+    salons[query("SELECT salon FROM tables WHERE id="+str(mainWindow.orderDetails[1]))[0][0]]        +""" </h3>
<h4 class="descript">start : """+ time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(mainWindow.orderDetails[3]))  + """</h4>
<h4  class="descript">finish: """+ time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(mainWindow.orderDetails[4]))  + """</h4>

        <TABLE  id="details" style="width: 100%;">
        <thead>
        <tr style="font-size: 80%">
            <TH></TH>
            <TH>Pret lei</TH>
            <TH>Timp min</TH>
            <TH>Suma</TH>
        </tr>
        </thead>

            <tbody>"""

        if minuteTarif1:
            self.html +="""<TR>
            <TD>Tarif nr.1</TD>
            <TD style="text-align:right !important;" >""" + str(mainWindow.orderDetails[9])  +"""</TD>
            <TD style="text-align:right !important;">""" + str(minuteTarif1)  +"""</TD>
            <TD style="text-align:right !important;">""" + str(mainWindow.orderDetails[9]* minuteTarif1 )  +"""</TD>
        </TR>"""

        if minuteTarif2:
            self.html +="""<TR>
            <TD>Tarif nr.2</TD>
            <TD style="text-align:right !important;" >""" + str(mainWindow.orderDetails[10])  +"""</TD>
            <TD style="text-align:right !important;">""" + str(minuteTarif2)  +"""</TD>
            <TD style="text-align:right !important;">""" + str(mainWindow.orderDetails[10]* minuteTarif2 )  +"""</TD>
        </TR>"""

        if minuteTarif3:
            self.html +="""<TR>
            <TD>Tarif nr.3</TD>
            <TD style="text-align:right !important;" >""" + str(mainWindow.orderDetails[11])  +"""</TD>
            <TD style="text-align:right !important;">""" + str(minuteTarif3)  +"""</TD>
            <TD style="text-align:right !important;">""" + str(mainWindow.orderDetails[11]* minuteTarif3 )  +"""</TD>
        </TR>"""

        self.html +="""</tbody>


        <TFOOT>

                <TR style="text-align:right !important;">
                    <td colspan="2"></td>
                    <td>""" + str(minuteTarif1 +minuteTarif2 +minuteTarif3)  +"""</td>
                    <td>""" +    str( mainWindow.orderDetails[9]* minuteTarif1 + mainWindow.orderDetails[10]* minuteTarif2 + mainWindow.orderDetails[11]* minuteTarif3 )      +  """</td>
                </TR>

                <TR style="text-align:right !important;">
                    <td>Reducere%</td>
                    <td>""" + str(mainWindow.orderDetails[14] )  +"""</td>
                    <td>suma</td>
                    <td>""" + str(mainWindow.orderDetails[15] )  +"""</td>
                </TR>

                <TR style="text-align:right !important;">
                    <td colspan="2"></td>
                    <td >Total </td>
                    <td >""" + str(mainWindow.orderDetails[16] )  +"""</td>
                </TR>

                <TR style="text-align:right !important;">
                    <td colspan="2"></td>
                    <td colspan="2">"""  +  query("SELECT name FROM payments_types ORDER BY id LIMIT "+ str(mainWindow.paymentType.currentIndex()) +",1")[0][0]  +   """</td>
                </TR>

                <TR>
                    <td colspan="2" style="text-align:center !important;"><h3>PLATIT</h3></td>
                    <td colspan="2"  style="border: 1px solid;text-align:center !important;" ><h3>""" + str(mainWindow.inputSumm.text() )  +"""</h3></td>
                </TR>

        </TFOOT>

        </TABLE>
        <hr/>

        <h4 class="descript">Tiparit  """  + str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time())))   +"""</h4>
        <h4 class="descript">Operator  """ +  str(mainWindow.maindindow.userInfo[1])  +  """  </h4>
        <h4 style="margin: auto; text-align: center">""" +  str(query("SELECT value FROM settings WHERE id=33")[0][0])   +  """</h4>
        """
        self.webView.setHtml(self.html)
        raise


    def printHtml(self,html):
        self.webView.setHtml(html)
        raise

