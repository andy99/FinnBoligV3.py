import pypyodbc
con = pypyodbc.connect
Antallstartekusk=0
def Funkkusk1plass(Kuskidnr):
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         print("ja vi har forbindelse Funkstarter kusk")
    
        Kuskid = [Kuskidnr]   
#         print(Kuskid, "Hvilken kusk er det behandler") 
        SQL = '''\
SELECT count (DIM_Kusker.Navn) as antall, navn, DIM_Kusker.Kuskidnr
FROM            DIM_Kusker  JOIN
                         [Lager fakta tabell resultater] ON DIM_Kusker.Kuskidnr = [Lager fakta tabell resultater].Kuskidnr
WHERE        ([Lager fakta tabell resultater].Plasserinint = 1) and ([Lager fakta tabell resultater].Kuskidnr = ?)
group by navn, DIM_Kusker.Kuskidnr
ORDER BY  antall desc

'''     
        cursor = con.cursor()
        cursor.execute(SQL,(Kuskid))
#         cursor.execute(SQL)
        Antallvunnet = 0
#         print("funkstarter kusk funksjon ")
#Skrive fil skal flyttes til Hovedprogram
        for a in cursor:
#             print(a[0],'Verdier til a[0]')
            if a[0] > 0:
                Antallvunnet = a[0]
#                 NavnKusk = a[1]
#                 Kuskidnr=a[2]
            else:
                Antallvunnet = 0    
#                 Navnkusk =' '
        cursor.close()
    if Kuskidnr == None:
        print('Ingen strarter') 
        Antallvunnet = 0   
    return Antallvunnet