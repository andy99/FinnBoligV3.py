import pypyodbc
con = pypyodbc.connect
def UdateUlikenavn(Hestnummer,Navn):
    print("oppdatete sette Heste_navn = Navn") 
    id_nr = Hestnummer 
    onavn = Navn
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
        testinput = [onavn,id_nr]
        SQL = '''\
        update [Trav].[dbo].[StartLister]
        set Heste_Navn  = ?
         where Id_nr  = ?;
         commit;         
                '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL,(testinput))
#         cursor.execute(SQL)
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
#         for b in cursor:
#             TestHestenavn    = b[0] 
#             Testidnr = b[1]
#             print(TestHestenavn,"Heste navn som skal oppdateres")
#             print(Testidnr,"id_nr  som skal oppdateres")
        cursor.close()    
#         print(plassering123,"Antall ikke gallopert gar ut av funksjonen")
    
