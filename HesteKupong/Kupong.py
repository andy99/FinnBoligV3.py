import pypyodbc
from Funkantalllop import Funkantalllop
from Funkbesteform import Funkbesteform
import os
utdata = 0
antlop= 0
lopnr = 0
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse
antalllop = Funkantalllop(antlop)
# lopnr = [antalllop]
lopnr = antalllop
# print(antalllop,"Antall lop Hoved program")
if con:
#     print("ja vi elsker dette landet og har forbindelse til databasen Hoved program")
#     while lopnr > 1:
    for i in range(1,lopnr+1):    
        print(lopnr,"Antall lop Hoved program inne loop")
#         print(i,"Verdi til I")
        SQL = '''\
SELECT Lop, Startnr, Kusk, StartMetode,Bane,Heste_navn,Galoppprosent,Trippelprosent, FormfaktorTotal,id_nr
  FROM [Trav].[dbo].[BeregnetForm]
 --
 -- where Dato = (SELECT CONVERT (date, SYSDATETIME())) and Lop = ?
  Where Dato = '2020-03-02'
   and Lop = ?
 order by lop, FormfaktorTotal

''' 
        
        cursor = con.cursor()
        cursor.execute(SQL,[i])
        for a in cursor:
            print(a[0], a[1], a[2],a[9])
            Lop           = a[0]
            Startnr       = a[1]
            Kusk          = a[2]
            StartMetode   = a[3] 
            Bane          = a[4]
            Heste_navn    = a[5] 
            Galoppprosent = a[6]
            Trippelprosent= a[7] 
            FormfaktorTotal= a[8]
            id_nr          = a[9]
            Hesteform = Funkbesteform(id_nr,FormfaktorTotal,Lop)
       
    cursor.close() 
