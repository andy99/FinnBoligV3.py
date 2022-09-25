import pypyodbc
coding='utf-8'
from FunkWebodds import FunkWebodds
import os
# if os.path.isfile("D:\workplace_python\pythonapp\DNTResulatListe.txt"):
#     print("D:\workplace_python\pythonapp\DNTResulatListe.txt","blir slettet")
#     os.remove("D:\workplace_python\pythonapp\DNTResulatListe.txt")
# 
# if os.path.isfile("D:\workplace_python\pythonapp\DNTodds.txt"):
#     print("D:\workplace_python\pythonapp\DNTodds.txt","blir slettet")
#     os.remove("D:\workplace_python\pythonapp\DNTodds.txt")    

con = pypyodbc.connect

class Lastedato(object):
    
    def __init__(self,DatoKlasse):
        self.DatoKlasse
    DatoKlasse ='01.01.1991'
    webdato = '20200309'
#import sys
#con = connection = pypyodbc.connect('Driver={SQL Server};'
#connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    FunkWebodds(webdato)









