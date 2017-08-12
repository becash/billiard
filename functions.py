appName = "Trio Billiard"
import random
import hashlib
from PySide import QtCore
import mysql.connector as mysql
# from hive.classes_becash import *
import firebirdsql
import datetime
import time
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#######################   INI   CONFIG
settingsConfig = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
# develop = int(settingsConfig.value("Developing/Program"))




########LOGAREA IN FAIL
logLevel = int(int(settingsConfig.value("Developing/LoggingLevel")))

# Level	Numeric value
# CRITICAL	0
# WARNING	1
# DEBUG	    2

LOG_FILENAME = '__loggingPython.log'

if logLevel==0:
    logging.basicConfig(level=logging.CRITICAL,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=LOG_FILENAME,
                        filemode='a')
if logLevel==1:
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=LOG_FILENAME,
                        filemode='a')
if logLevel==2:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=LOG_FILENAME,
                        filemode='a')

def timestamp():
    return str(str(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time()))))+':   '


# developCOM = int(settingsConfig.value("Developing/Comport"))
# logging.info(settingsConfig.allKeys())
# logging.info(settings.value("Settings/NumFields"))
# settings.setValue("Settings/NumFields", str(time.time()))

    #generator guid
import uuid
def getNewSID():
    return str(uuid.uuid1())


def eroarePopup(message):
    logging.info('-----eroarePopup-----')
    logging.warning(message)
    from PySide import QtCore, QtGui
    import sys
    try:
        class Program(QtGui.QDialog):
            def __init__(self, parent=None):
                super(Program, self).__init__(parent)
                self.setWindowTitle("Initialization Error")
                self.label1 = QtGui.QLabel(message)
                layout = QtGui.QVBoxLayout()
                layout.addWidget(self.label1)
                self.setLayout(layout)
                self.setLayout(layout)

        app = QtGui.QApplication(sys.argv)
        form = Program()
        form.show()
        app.exec_()
    except:
        QtGui.QMessageBox.warning(None, appName, message)



if (int(settingsConfig.value("FirebirdSettings/EnableFirebird"))):
    def queryFirebird(query):
        logging.info(query)
        responce = []
        try:
            con = firebirdsql.connect(
                charset='UTF8',
                host=settingsConfig.value("FirebirdSettings/Host"),
                user=settingsConfig.value("FirebirdSettings/User"),
                password=settingsConfig.value("FirebirdSettings/Password__"),
                database=settingsConfig.value("FirebirdSettings/Database"))
        except Exception as e:
            eroarePopup(str(e))
        cur = con.cursor()
        cur.execute(query)

        try:
            for c in cur.fetchall():
                responce.append(c)
        except Exception as e:
            eroarePopup(str(e))
        con.commit()
        con.close()
        return responce


# Open database connection
def query (query):

    #prima cerere>>  verificam  daaca  baza e accesifila
    try:
        db = mysql.connect(
            host=settingsConfig.value("MysqlSettings/Host"),
            user=settingsConfig.value("MysqlSettings/User"),
            password=settingsConfig.value("MysqlSettings/Password__"),
            database=settingsConfig.value("MysqlSettings/Database"))
    except Exception as e:
        eroarePopup("Eroare la conectarea cu Mysql: "+str(e))
        logging.info(str(e))
        raise


    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    logging.info('---------------------Cerere Mysql------------')
    try:
        logging.info(query)
    except Exception as e:
        eroarePopup("Eroare in cererea  Mysql: "+str(e))
        logging.info(str(e))
        raise


    cursor.execute(query)
    # Fetch a single row using fetchone() method.
    if cursor._have_unread_result():
        data = cursor.fetchall()
        logging.info('---------------------Sfirshit Mysql------------')
        return data

    if cursor.lastrowid:
        logging.info('last insert id')
        logging.info(cursor.lastrowid)
        db.commit()
        return cursor.lastrowid
    db.commit()
    logging.info(cursor.stored_results())
    logging.info('---------------------RASPUNS GOL------------')
    # disconnect from server
    db.close()
    return False


###ROTUNGIREA TIMPULUI
def roundTime(dt=None, roundTo=60):
    logging.info('---------------------roundTime------------')
    """Round a datetime object to any time laps in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """
    if dt == None : dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    # // is a floor division, not a comment on following line:
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)


def clearOldOrders():
    logging.info('clearing')
    # print("curatim otderele vechi")
    old = query("SELECT value FROM settings WHERE id=40")[0][0]
    oldUnix = int(time.time()) - (int(old)*86400)
    query("DELETE FROM orders WHERE sync=1 AND at<" + str(oldUnix))



curentTimePeriod=None
perioadele = query("SELECT `value` FROM settings WHERE id IN (70,80,90) ORDER BY id  ")

def getCurentPeriod(unixTime=None):
    logging.info('-----getCurentPeriod-----')
    global curentTimePeriod
    global perioadele
    perioadaCurenta=-1
    logging.info(perioadele)
    for i in perioadele:
        if int(i[0]) >= int(time.strftime("%H",time.localtime(time.time())))+1:
            break
        perioadaCurenta += 1
    if perioadaCurenta == -1:
        perioadaCurenta =2
    curentTimePeriod =perioadaCurenta
    return perioadaCurenta

def getPeriodByTime(unixTimme):
    global curentTimePeriod
    global perioadele
    perioadaCurenta=-1
    for i in perioadele:
        if int(i[0]) >= int(time.strftime("%H",time.localtime(unixTimme)))+1:
            break
        perioadaCurenta += 1
    if perioadaCurenta == -1:
        perioadaCurenta =2
    return perioadaCurenta


def getSummForGame(order):
    ###calculam summa pentru toata joaca,  avind in vedere perioadele de timp
    logging.info('-----getSummForGame-----')
    logging.info(order)
    finish=order[4]
    if finish==None:
        finish=int(time.time())
    summa =0
    while finish > order[3]:
        pretulMinutei = order[9+getPeriodByTime(finish)]
        summa+=pretulMinutei
        finish-=60
    # return   float(summa)  #    returneaza  summa  cu  banuti
    return   int(summa)  #    returneaza  summa  cu  banuti







def sendEmail(destinatar,html):
    try:
         # Gmail Sign In
        gmail_sender = query("SELECT value FROM settings WHERE id=34")[0][0]
        gmail_passwd = query("SELECT value FROM settings WHERE id=35")[0][0]
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = gmail_sender
        msg['To'] = destinatar

        # Create the body of the message (a plain-text and an HTML version).
        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
        # html = """\
        # <html>
        #   <head></head>
        #   <body>
        #     <p>Hi!<br>
        #        How are you?<br>
        #        Here is the <a href="https://www.python.org">link</a> you wanted.
        #     </p>
        #     <h1>222222222</h1>
        #
        #   </body>
        # </html>
        # """

        # Record the MIME types of both parts - text/plain and text/html.
        # part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        # msg.attach(part1)
        msg.attach(part2)

        try:
            server.sendmail(gmail_sender, [destinatar], msg.as_string())
            server.quit()
            return 1
        except Exception as e :
            server.quit()
            return str(e)
    except Exception as e :
        logging.warn("Eroare la expedierea mailui cu raportul")
        logging.warn(str(e))
        print(str(e))
        return 0



# ####################################TEXT PENTRU DIAGNOSTICA
if __name__ == '__main__':
    result = query("SELECT * FROM users")
    logging.info(getNewSID())
    logging.info(result)


