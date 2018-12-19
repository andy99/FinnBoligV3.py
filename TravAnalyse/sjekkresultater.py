import pypyodbc
con = pypyodbc.connect
def sjekkresultater():
#     return prosentgallop
    print("Videre behandling av hestenummer i funksjon leser lopkalendag for sjekk av resultater") 
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
        print("ja vi har forbindelse")
        SQL = '''\
        SELECT Distinct a.Bane, dato,Lopdato, b.bane

        FROM [Trav].[dbo].[Bane_Dato_Oppdatert] a,
             [Trav].[dbo].[Lopkalendar] b
            Where Dato > '2018-01-01'
            and   Lopdato < (SELECT CONVERT (date, SYSDATETIME()))
           and a.Bane = b.bane
          and Dato < Lopdato
           order by lopdato

        '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL)
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
            print(b,'Antall baner reslutat')
            lopsBane = b[0]
            lopsdato = b[2]
#             Dato = b[1] 
            print(lopsBane,"Lopsbane har verdien") 
#             print(lopsbane2,"Lopsbane  2 har verdien") 
#             print(Dato,"Dato sist oppdater")
            return lopsBane,lopsdato
        cursor.close()    