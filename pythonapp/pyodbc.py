import pypyodbc
#import sys
#con = connection = pypyodbc.connect('Driver={SQL Server};'
#connection = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')

if con:
    print("ja vi har forbindelse")
    
    
SQL = '''\
SELECT TOP 1000 [Resultat_Dato]
  FROM [Trav].[dbo].[Travdatoer]
'''     
cursor = con.cursor()
cursor.execute(SQL)

for c in cursor:
    print(c[0])
cursor.close()

SQL1 = '''\
SELECT count(Resultat_Dato) 
  FROM [Trav].[dbo].[Travdatoer]
'''    
cursor = con.cursor()         
cursor.execute(SQL1)
for a in cursor:
    print(a[0],"Antall rader")

con.close()    