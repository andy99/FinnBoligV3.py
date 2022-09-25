import pypyodbc
import os
con = pypyodbc.connect
class Lastedato(object):
    def __init__(self,DatoKlasse):
        self.DatoKlasse
    DatoKlasse ='01.01.1991'

if os.path.isfile("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt"):
    print("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt")
        
#import sys
#con = connection = pypyodbc.connect('Driver={SQL Server};'
#connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
print(Lastedato.DatoKlasse)
if con:
    print("ja vi har forbindelse")
    
    
SQL = '''\
SELECT count (DIM_Kusker.Navn) as antall, navn, DIM_Kusker.Kuskidnr
FROM            DIM_Kusker  JOIN
                         [Lager fakta tabell resultater] ON DIM_Kusker.Kuskidnr = [Lager fakta tabell resultater].Kuskidnr
--WHERE        ([Lager fakta tabell resultater].Plasserinint = 1)
group by navn, DIM_Kusker.Kuskidnr
ORDER BY  antall desc

'''     
cursor = con.cursor()
cursor.execute(SQL)

#dato = cursor
#cursor.next()
with open('Antallstarterkusk.txt', 'a') as f:
    for a in cursor:
        Antallstartekusk = a[0]
        NavnKusk = a[1]
        Kuskidnr=a[2]
        f.write("%s;%s;%s" % \
        (Antallstartekusk,NavnKusk,Kuskidnr))
        f.write('\n')
#         print(Antallstartekusk,'Antallstarter')
#         print(NavnKusk,'NavnKusk')
#         print(Kuskidnr,'Kuskidnr')

cursor.close()








