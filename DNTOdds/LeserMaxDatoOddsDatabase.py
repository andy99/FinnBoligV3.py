import pypyodbc
coding = 'utf-8'
con = pypyodbc.connect
print("Program Startet maxoddsdata")
def LeserMaxDatoOddsDatabase(webdato):
    print("Er i funksjonen")
    con = pypyodbc.connect(
        'Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
    print("Program Startet")
    if con:
      print("ja vi har forbindelse")

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
# henter ut aar

    datolengde = len(Dato)
    print(datolengde, "Dato lengde")
    aar = Dato[0:4]
    mm = Dato[5:7]
    print(aar)
    print(mm)
    dag = Dato[8:10]
    nydag = dag.strip()
    utdag = "01"
    utdag = nydag
    #    Finndagnr(utdag)
    #     mnd,aar=mndyyyy.split(' ')
    print(utdag, "Dag  er")
    if nydag == '1':
        nydagnr = '01'
    elif nydag == '2':
        nydagnr = '02'
    elif nydag == '3':
        nydagnr = '03'
    elif nydag == '4':
        nydagnr = '04'
    elif nydag == '5':
        nydagnr = '05'
    elif nydag == '6':
        nydagnr = '06'
    elif nydag == '7':
        nydagnr = '07'
    elif nydag == '8':
        nydagnr = '08'

    elif nydag == '9':
        nydagnr = '09'
    else:
        nydagnr = nydag

    webdato = aar + mm + nydagnr
    print(webdato, "Webdato")
    cursor.close()
