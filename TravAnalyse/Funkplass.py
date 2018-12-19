import pypyodbc
con = pypyodbc.connect
def Funkplass(Hestnummer):
#     return prosentvinner
#     print(Hestnummer,"Videre behandling av hestenummer i funksjonkvinner leser resultat") 
    id_nr = Hestnummer 
    plassering123= 0
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
#         print("ja vi har forbindelse")
#         testinput = [30088706]
        testinput = [id_nr]
        SQL = '''\
        SELECT top 3 id_nr,Plassering,dato
        FROM [Trav].[dbo].[Fakta_lop]
        where id_nr = ?
        and Totalpremiesum > 0
        order by dato desc
                '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL,(testinput))
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
            id_nr      = b[0] 
            plassering = b[1]
            if plassering < '4' and plassering  > '0':
                plassering123 = plassering123 + 10 
        cursor.close()    
#         print(plassering123,"Antall ikke gallopert gar ut av funksjonen")
#     print(galopp,"Antall gallopert gar ut av funksjonen")
    
    return plassering123
