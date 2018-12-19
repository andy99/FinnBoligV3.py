import pypyodbc
con = pypyodbc.connect
def Funkvinner(Hestnummer):
#     return prosentvinner
#     print(Hestnummer,"Videre behandling av hestenummer i funksjonkvinner leser resultat") 
    id_nr = Hestnummer 
    vinner=0 
    
    ikkevinner= 0
    prosentvinner=0
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
#         print("ja vi har forbindelse")
#         testinput = [30088706]
        testinput = [id_nr]
        SQL = '''\
        SELECT Hestenavn ,id_nr, Kusk, Plassering
        FROM [Trav].[dbo].[Fakta_lop]
        where id_nr = ?
        and Totalpremiesum > 0
                '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL,(testinput))
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
             
#             print(b[0], b[1], b[2],b[3],"Data vi verider fra FAKTA lop?")    
            Hestenavn = b[0]
            id_nr      = b[1] 
            kusk     = b[2]
            plassering = b[3]
            if plassering == '1':
               vinner = vinner + 1 
#                print(vinner,"Antall Vinner")
            else:
               ikkevinner = ikkevinner + 1  
#             Hestenummer = id_nr
#             print(Hestenummer,"verdi til hestenummer etter kall til fakta lop")

        cursor.close()    
#     print(ingengalopp,"Antall ikke gallopert gar ut av funksjonen")
#     print(galopp,"Antall gallopert gar ut av funksjonen")
    antstarter = vinner + ikkevinner
    if antstarter > 0:
        prosentvinner = vinner * 100 / antstarter
    else:
        prosentvinner =0 
#     print(prosentvinner,"vinnerprosent % i funfakta program test data")  
    
    return prosentvinner
