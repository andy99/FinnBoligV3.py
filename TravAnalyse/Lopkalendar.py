import pypyodbc
con = pypyodbc.connect
def Lopkalendar():
#     return prosentgallop
    print("Videre behandling av hestenummer i funksjon leser lopkalendag") 
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
        print("ja vi har forbindelse")
        SQL = '''\
        SELECT bane
       FROM [Trav].[dbo].[Lopkalendar]
        where Lopdato = (SELECT CONVERT (date, SYSDATETIME())) 
        and bane not like 'Harst%'     


        '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL)
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
            print(b,'Antall baner lopsdag')
            lopsBane = b[0]
#             lopsbane2 = b[1]
#             Dato = b[1] 
            print(lopsBane,"Lopsbane har verdien") 
#             print(lopsbane2,"Lopsbane  2 har verdien") 
#             print(Dato,"Dato sist oppdater")
            return lopsBane
        cursor.close()    