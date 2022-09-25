import pypyodbc
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
    and a.Bane not like 'Ork%'
    and Dato < Lopdato
    order by lopdato
'''     
cursor = con.cursor()
cursor.execute(SQL)

#dato = cursor
#cursor.next()
for a in cursor:
#     print(c[0])
    Bane = a[0] 
#     Dato = a[1]
    Lopdato = a[1]
    #henter ut aar
    print(Bane,"Innhold Bane")
#     print(Dato,"Innhold Dato")
    print(Lopdato,"Innhold Lopdato")
    datolengde = len(Lopdato)
#     print(datolengde,"Dato lengde")
    aar = Lopdato[0:4]
    maned = Lopdato[5:7]
    dag = Lopdato[8:datolengde]
    print(aar,"aar finnerbaneoppdater")
    print(maned,"maned finnerbaneoppdater")
    print(dag,"dag finnerbaneoppdater")
    webdatores = aar + maned+dag
    bane="Leangen-Travbane"    
    print(webdatores,"Webdatores")
cursor.close()
