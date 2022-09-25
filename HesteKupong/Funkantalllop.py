import pypyodbc
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse)
def Funkantalllop(antlop):
    if con:
#         print("ja vi elsker dette landet og har forbindelse Funkantalllop")
   
     SQL = '''\
SELECT COUNT( Distinct Lop)
  FROM [Trav].[dbo].[BeregnetForm]
    --where Dato = (SELECT CONVERT (date, SYSDATETIME()))
  Where Dato = '2020-03-02'  
'''     
        
    cursor = con.cursor()
    cursor.execute(SQL)
    for a in cursor:
        print(a[0],"Antall lop")
        antlop = a[0]
        return antlop
    cursor.close() 

