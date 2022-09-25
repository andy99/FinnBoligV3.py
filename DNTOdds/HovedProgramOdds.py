coding = 'utf-8'
from FunkWeboddsTest import FunkWeboddsTest
from FunkMaxtravdatoer import Funkmaxtravdatoer
from FunkOddsDNT import FunkOddsDNT
import os
import pypyodbc
if os.path.isfile("D:\workplace_python\DNTOdds\DNTodds.txt"):
    print("D:\workplace_python\DNTOdds\DNTodds.txt", "blir slettet")
    os.remove("D:\workplace_python\DNTOdds\DNTodds.txt")
webdato = '00000'
maxdato = Funkmaxtravdatoer(webdato)
webdato = maxdato
print(maxdato, "Dato fra program Funkmaxtravdatoer DENNE viser hva siste oddsdata pr bane")
maxdato = [maxdato]
#dato = FunkOddsDNT(webdato)
dato = 0
con = pypyodbc.connect(
    'Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
print("Program Startet")
if con:
    print("ja vi har forbindelse")
SQL = '''\
SELECT   Dato
      FROM [Trav].[dbo].[Travdatoer]
	  Where Dato > ?
	  and Bane = ' Sorlandets-travpark'
 '''
cursor = con.cursor()
cursor.execute(SQL,(maxdato))
for a in cursor:
    print(a[0])
    Dato = a[0]
    if Dato is not None:
        utdato = Dato.translate({ord('-'): None})
        Utdato = FunkOddsDNT(utdato)
cursor.close()
#utdato = Dato.translate({ord('-'): None})


print(dato, "har kallt funkoddsDNT")
