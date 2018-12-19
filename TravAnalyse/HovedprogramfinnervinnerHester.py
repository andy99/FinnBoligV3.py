import pypyodbc
from Beregnerform import Beregnerform
utdata = 0
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse)
if con:
    print("forbindelse")

#Finner antall lop
SQL = '''\
SELECT COUNT(distinct lop)

  FROM [Trav].[dbo].[StartListerDrammen]
  where Dato = '2018-07-31'
'''     
cursor = con.cursor()
cursor.execute(SQL)
# prosentgallop = 0
#dato = cursor
#cursor.next()
lop = 0

for a in cursor:
    print(a[0])    
    Antalllop = a[0]
    print(Antalllop,"Antall lop i Hoved Program")
    while lop < Antalllop:
        lop = lop + 1
        Beregnerform(lop)
   
        print(lop,"viser alle lopnr i Hovedprogram")
#     for c in  Antalllop:
#         print(c,"antall lop Hoved from for loop")
#         
cursor.close() 