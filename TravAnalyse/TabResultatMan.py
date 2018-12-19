import pypyodbc
con = pypyodbc.connect
def TabResultatMan():
#     return prosentgallop
    print("Videre behandling av hestenummer i funksjon leser lopkalendag for sjekk av resultater") 
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
        print("ja vi har forbindelse i TabManResultat")
        SQL = '''\
       Insert into [Trav].[dbo].[Resultat_Mangler] (Lopdato, b.bane)
       SELECT Distinct Lopdato, b.bane
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
        cursor.commit()
        cursor.close()    