import pypyodbc
coding='utf-8'
from FunksjonleserWeb import FunksjonleserWeb
from FunkWebodds import FunkWebodds
from FunkWeboddsTest import FunkWeboddsTest
import os
# if os.path.isfile("D:\workplace_python\pythonapp\DNTResulatListe.txt"):
#     print("D:\workplace_python\pythonapp\DNTResulatListe.txt","blir slettet")
#     os.remove("D:\workplace_python\pythonapp\DNTResulatListe.txt")

if os.path.isfile("D:\workplace_python\pythonapp\DNTodds.txt"):
    print("D:\workplace_python\pythonapp\DNTodds.txt","blir slettet")
    os.remove("D:\workplace_python\pythonapp\DNTodds.txt")    

con = pypyodbc.connect

class Lastedato(object):
    
    def __init__(self,DatoKlasse):
        self.DatoKlasse
    DatoKlasse ='01.01.1991'
    
#import sys
#con = connection = pypyodbc.connect('Driver={SQL Server};'
#connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
print(Lastedato.DatoKlasse)
if con:
    print("ja vi har forbindelse")
#     webdato='20200302'          Dette er for Testing
#     FunkWeboddsTest(webdato)
    
SQL = '''\
SELECT  [Resultat_Dato]
  FROM [Trav].[dbo].[Travdatoer]
'''     
cursor = con.cursor()
cursor.execute(SQL)

#dato = cursor
#cursor.next()
for a in cursor:
#     print(c[0])
    Dato = a[0]
    #henter ut aar
    datolengde = len(Dato)
#     print(datolengde,"Dato lengde")
    aar = Dato[17:21]
    ukeDag,ddmmmyyyy = Dato.split(',')
#     print(UkeDag,"Dag")
    print(ddmmmyyyy,"ddmmmyyyy")
    dag,mndyyyy = ddmmmyyyy.split('.')
    nydag = dag.strip()
    utdag = "01"
    utdag = nydag
#    Finndagnr(utdag)
#     mnd,aar=mndyyyy.split(' ')
    print(utdag,"Dag  er")
    if nydag == '1':
        nydagnr = '01'
    elif nydag == '2':
        nydagnr = '02'
    elif nydag == '3':
        nydagnr = '03'
    elif nydag == '4':
        nydagnr = '04'
    elif nydag == '5':
        nydagnr = '05'
    elif nydag == '6':
        nydagnr = '06'
    elif nydag == '7':
        nydagnr = '07'
    elif nydag == '8':
        nydagnr = '08'
    elif nydag == '9':
        nydagnr = '09'
    else:
        nydagnr = nydag                            
            

                             
    print(mndyyyy,"mnd År er")
    aar=mndyyyy[5:9]
    mnd =mndyyyy[1:4]
    if mnd == 'sep':
        aar=mndyyyy[6:10]
    
    print(mnd,"Maned er")
    print(aar,"Verdi aar")
    if mnd == 'jan':
        mndnr = '01'
    elif mnd == 'feb':
        mndnr = '02' 
    elif mnd == 'mar':
        mndnr = '03'    
    elif mnd == 'apr':
        mndnr = '04' 
    elif mnd == 'mai':
        mndnr = '05'
    elif mnd == 'jun':
        mndnr = '06' 
    elif mnd == 'jul':
        mndnr = '07'  
    elif mnd == 'aug':
        mndnr = '08' 
    elif mnd == 'sep':
        mndnr = '09' 
    elif mnd == 'okt':
        mndnr = '10' 
    elif mnd == 'nov':
        mndnr = '11'  
    elif mnd == 'des':
        mndnr = '12'   
    else:
        print("Feil i månedsnr") 
        
        
    print(mndnr,"Maanedsnr")
    webdato = aar + mndnr + nydagnr
    print(webdato,"Webdato")
#     FunksjonleserWeb(webdato)
#     FunkWebodds(webdato)
    FunkWeboddsTest(webdato)
cursor.close()








