import pypyodbc
coding = 'utf-8'
con = pypyodbc.connect
print("Program Startet maxoddsdata")
def testfunki():
    print("Er i funksjonen")
    con = pypyodbc.connect(
        'Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
    print("Program Startet")
    if con:
        print("ja vi har forbindelse")
    else:
        print('Ingen forbindelse')
    SQL = '''\
 SELECT *
  FROM  [DWtrav].[dbo].[odds2]
  Where Dato = (Select Max(Dato)
  FROM  [DWtrav].[dbo].[odds2])
  order by Lop
'''
    cursor = con.cursor()
    cursor.execute(SQL)
    for a in cursor:
        print(a[2])
        Dato = a[2]