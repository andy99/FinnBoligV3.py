import pypyodbc
coding = 'utf-8'
# Dette programmet finner siste oppdater oddsdata
# Programmet kalles fra HovedProgramm som ligger på DNTodds

def Funkmaxtravdatoer(webdato):
    con = pypyodbc.connect
    print("Program Startet maxoddsdata")
    print("Er i funksjonen")
    con = pypyodbc.connect(
        'Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
    print("Program Startet")
    if con:
        print("ja vi har forbindelse")
    SQL = '''\
 SELECT Distinct Bane, max(Dato)
  FROM [Trav].[dbo].[odds]
  Where Baneid = 6
  Group By Bane
  '''
    cursor = con.cursor()
    cursor.execute(SQL)
    for a in cursor:
        print(a[0])
        print(a[1])
        Dato = a[1]
    cursor.close()
    utdato = Dato.translate({ord('-'): None})
    return utdato
