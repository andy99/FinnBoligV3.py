import pypyodbc
con = pypyodbc.connect
def GyldigBaneRes(Banenavn):
#     return prosentgallop
    print(Banenavn,"Videre behandling av hestenummer i funksjon leser resultat") 
    con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
    if con:
#         ingengalopp=0 
#         galopp=0
        print("ja vi har forbindelse er i sub rutne finner gyldig bane navn")
#         testinput = [30088706]
        print(Banenavn,"er subrutine finn gyldig banenavn")
#         if Banenavn == 'Sørlandets-Travpark':
#             Banenavn = 'Sorlandets-travpark'
        if Banenavn == 'Orkla-Arena':
            Banenavn ='Varig-Orkla-Arena'
        testinput = [Banenavn]
        SQL = '''\
        SELECT [Bane]
      ,[Dato]
      FROM [Trav].[dbo].[Bane_Navn_Gyldige]
      where Bane like ?


        '''  
        cursor = con.cursor()
#Virker med liste 
        cursor.execute(SQL,(testinput))
#         print(testinput,"Videre behandling etter sql kall fakta tabell") 
#         ingengalopp=0 
#         galopp=0
        for b in cursor:
            
 
            Bane = b[0]
            Dato = b[1] 
            print(Bane," finner gyldig bane navn Bane som vi laster resultater fra") 
            print(Dato,"Dato sist oppdater")
            return Bane
        cursor.close()    
