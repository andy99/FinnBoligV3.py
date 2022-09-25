import pypyodbc
coding='utf-8'
con = pypyodbc.connect
#Finner max dato i odds2, dette siste oddsdata loadet for banen
maxdato = 0
def Maxoddsdata(maxdato):
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
        print(maxdato,"Vi har forbindelse")
    SQL = '''\
SELECT Max(Dato)
  FROM [DWtrav].[dbo].[odds2]
  Where Baneid = 4
'''     
    cursor = con.cursor()
    cursor.execute(SQL)
#dato = cursor
#cursor.next()
    for a in cursor:
        print(a[0],'Skriver verdi i a0')
        Dato = a[0]
        maxdato = Dato
#        return maxdato
    cursor.close()
    print(maxdato,"maxdato innhold etter cursor Gunnar")
    Datout = Dato
    return maxdato
#  if Datout == None:
#      print('Ingen Dato funnet') 
#     Datout  = 0
#    else:
#       return Datout
#Return Datout
