import pypyodbc
from Funkresauto import Funkresauto
from GyldigBaneRes import GyldigBaneRes
from Tellerantallbanerikkeop import Tellerantallbanerikkeop
import os
if os.path.isfile("D:\workplace_python\HesterResAutomatisk\DNTResulatListe.txt"):
    print("D:\workplace_python\HesterResAutomatisk\DNTResulatListe.txt","blir slettet")
    os.remove("D:\workplace_python\HesterResAutomatisk\DNTResulatListe.txt")

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
    
    
SQL = '''\
SELECT Distinct a.Bane,Lopdato

  FROM [Trav].[dbo].[Bane_Dato_Oppdatert] a,
       [Trav].[dbo].[Lopkalendar] b
  Where Dato > '2018-01-01'
    and   Lopdato < (SELECT CONVERT (date, SYSDATETIME()))
    and a.Bane = b.bane
   -- and a.Bane not like 'Ork%'
    and a.bane not like 'Kala%'
    and Dato < Lopdato
    order by lopdato

'''     
cursor = con.cursor()
cursor.execute(SQL)

#dato = cursor
#cursor.next()
antallbaner = Tellerantallbanerikkeop()
print(antallbaner,"antall baner til oppdatering")
for a in cursor:
#     print(c[0])
    Bane = a[0]
    Lopdato = a[1]
    #henter ut aar
    aar = Lopdato[0:4]
    maned = Lopdato[5:7]
    datolengde = len(Lopdato)
    dag = Lopdato[8:datolengde]
    print(aar,"aar finnerbaneoppdater")
    print(maned,"maned finnerbaneoppdater")
    print(dag,"dag finnerbaneoppdater")
    webdatores = aar + maned+dag
    print(Bane,"Bane")
    print(webdatores,"lopdato for henting av resultater")
    nybane = Bane.replace(' ','-')
    print(nybane,"sendes funk finn gyldig bane")
    if nybane[0] == 'S':
        nybane= 'Sor%'
    gyldigbane=GyldigBaneRes(nybane)
    print(gyldigbane,"Gyldig bane navn")
    Funkresauto(webdatores,gyldigbane)
cursor.close()
