import pypyodbc
con = pypyodbc.connect
def Funksjekkidnr(Hestnummer,Navn):
#     Prgramm for å sjekke om idnr finnes i alle hester
#     print(Hestnummer,"Videre behandling av hestenummer i funksjonkvinner leser resultat") 
    id_nr = Hestnummer 
    navn =" "
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
        testinput = [id_nr]
        SQL = '''\
       SELECT Id_nr, navn 
        FROM [Trav].[dbo].[AlleHester2]
        where Id_nr = ?
                '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL,(testinput))
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
            id_nr      = b[0] 
            navn = b[1]
        cursor.close()    
#         print(plassering123,"Antall ikke gallopert gar ut av funksjonen")
    if id_nr == None:
        id_nr = 99999
        navn = "Feil i Hestenavn"
    if navn == None:
        navn = "Feil i navn"   
#     print(id_nr,"Som sjekkes  i funksjonen sjekkidnr")   
#     return id_nr
    return {'idnr':id_nr, 'navn':Navn }