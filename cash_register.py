#!/usr/bin/env python
from functions import *

#S,1,______,_,__;Martini Bian;151.75;2.000;1;1;1;0;0;
#S,1,______,_,__;ФилеКуриное1;75.00;2.000;1;1;1;0;0;
#S,1,______,_,__;Шашлык1кг;110.00;0.350;1;1;1;0;0;
#//
#//// Свободный тест
#P,1,______,_,__;Spasibo za pokupku;;;;;
#//
#//// Конец чека (закрытие чека)
#T,1,______,_,__;0;492.00;;;;



def printGameCheck(suuma):
    try:
        f = open(query("SELECT value FROM settings WHERE id=54")[0][0], 'w')
        f.write("S,1,______,_,__;"+  query("SELECT value FROM settings WHERE id=53")[0][0]  +";"+  '{0:.2f}'.format(float(suuma))  +";1.000;"+  query("SELECT value FROM settings WHERE id=55")[0][0]  +";"+  query("SELECT value FROM settings WHERE id=56")[0][0]  +";1;0;0;"+ '\n')
        f.close()
    except Exception as e:
        logging.warning("ERROR when create cash register file  CHECK ")
        logging.warning(str(e))
        eroarePopup(str(e))
        return False
    else:
        return True




def printZ_Report():
    try:
        f = open(query("SELECT value FROM settings WHERE id=54")[0][0], 'w')
        f.write("A,1,______,_,__;;;Z;;;;"+ '\n')
        f.close()
    except Exception as e:
        logging.warning("ERROR when create cash register file   ZREPORT")
        logging.warning(str(e))
        eroarePopup(str(e))
        return False
    else:
        return True

