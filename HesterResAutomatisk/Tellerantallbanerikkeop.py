import pypyodbc
con = pypyodbc.connect

def Tellerantallbanerikkeop():
    
    def __init__(self,DatoKlasse):
        self.DatoKlasse
    DatoKlasse ='01.01.1991'
#import sys
#con = connection = pypyodbc.connect('Driver={SQL Server};'
#connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
if con:
    print("ja vi har forbindelse")
    
    
SQL = '''\
SELECT count(Distinct a.Bane)

  FROM [Trav].[dbo].[Bane_Dato_Oppdatert] a,
       [Trav].[dbo].[Lopkalendar] b
  Where Dato > '2018-01-01'
    and   Lopdato < (SELECT CONVERT (date, SYSDATETIME()))
    and a.Bane = b.bane
    and a.Bane not like 'Ork%'
    and Dato < Lopdato

'''     
cursor = con.cursor()
cursor.execute(SQL)

#dato = cursor
#cursor.next()
for a in cursor:
#     print(c[0])
    Antallbanerikkeopp = a[0] 
    print(Antallbanerikkeopp,"Antallbaner ikke oppdater")
#    print(Dato,"Innhold Dato")
 
cursor.close()
