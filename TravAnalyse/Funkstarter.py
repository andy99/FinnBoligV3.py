import pypyodbc
con = pypyodbc.connect
def Funkstarter(Hestnummer):
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
    
            Galoppind = b[3]
#             print(Galoppind,"Hvilken verdi har galoppind?")
            if Galoppind == 'Ingen galopp ':
                ingengalopp = ingengalopp + 1 
#                 print(ingengalopp,"Antall ikke gallopert")
            else:
                galopp = galopp + 1  

        cursor.close()    
    antstarter = ingengalopp + galopp
    if antstarter > 0:
        antstarter = antstarter
      
    else:
        antstarter=0 
#     print(antstarter,"Antall starter i funkstarter program")  
    
    return antstarter



#     