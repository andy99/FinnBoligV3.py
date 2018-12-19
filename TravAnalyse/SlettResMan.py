import pypyodbc
con = pypyodbc.connect
def SlettResMan():
#     return prosentgallop
    print("Videre behandling av hestenummer i funksjon leser lopkalendag for sjekk av resultater") 
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
        print("ja vi har forbindelse i TabManResultat")
        SQL = '''\
       Delete
       from [Trav].[dbo].[Resultat_Mangler]
       '''

        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL)
        cursor.commit()
        cursor.close()    