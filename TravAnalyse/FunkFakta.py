import pypyodbc
con = pypyodbc.connect
def FunkFakta(Hestnummer):
#     return prosentgallop
#     print(Hestnummer,"Videre behandling av hestenummer i funksjon leser resultat") 
    id_nr = Hestnummer 
    antstarter=0
    ingengalopp=0 
    galopp=0
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
#         print("ja vi har forbindelse")
#         testinput = [30088706]
        testinput = [id_nr]
        print(testinput,"Behandler dette id_nr")
        SQL = '''\
        SELECT Hestenavn ,id_nr, Kusk, Galoppind
        FROM [Trav].[dbo].[Fakta_lop]
        where id_nr = ?
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
            Galoppind = b[3]
#             print(Galoppind,"Hvilken verdi har galoppind?")
            if Galoppind == 'Ingen galopp ':
                ingengalopp = ingengalopp + 1 
#                 print(ingengalopp,"Antall ikke gallopert")
            else:
                galopp = galopp + 1  
                Hestenummer = id_nr
#             print(Hestenummer,"verdi til hestenummer etter kall til fakta lop")
#             print(ingengalopp,"Antall ikke gallopert")
#             print(galopp,"Antall gallopert")
        cursor.close()    
#     print(ingengalopp,"Antall ikke gallopert gar ut av funksjonen")
#     print(galopp,"Antall gallopert gar ut av funksjonen")
    antstarter = ingengalopp + galopp
    if antstarter > 0:
        prosentgallop = galopp * 100 / antstarter
    else:
        prosentgallop =0 
#     print(prosentgallop,"Galopp % i funfakta program test data")  
    
    return prosentgallop



#     