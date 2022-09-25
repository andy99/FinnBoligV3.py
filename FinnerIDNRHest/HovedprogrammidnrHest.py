import pypyodbc
import os
if os.path.isfile("D:\workplace_python\FinnerIDNRHest\Hestmangleridnr.txt"):
    print("D:\workplace_python\FinnerIDNRHest\Hestmangleridnr.txt","blir slettet")
    os.remove("D:\workplace_python\FinnerIDNRHest\Hestmangleridnr.txt")
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
if con:
    print("ja vi har forbindelse Hovedprorgam Hester mangler idnr")
# SQL = '''\    
# SELECT Heste_navn, Navn, Id_nr
#   FROM [Trav].[dbo].[StartLister]
#   where Heste_navn <> Navn
# '''
SQL = '''\
SELECT Heste_navn,Bane, Dato
  FROM [Trav].[dbo].[StartLister]
  Where id_nr  IS NULL
'''         
cursor = con.cursor()
cursor.execute(SQL)
for a in cursor:
    Hestenavn = a[0]
    Bane      = a[1] 
    Dato     = a[2]
    with open('Hestmangleridnr.txt', 'a') as f:
        f.write("%s;%s;%s" % \
        (Hestenavn,Bane,Dato))
        f.write('\n')
cursor.close() 