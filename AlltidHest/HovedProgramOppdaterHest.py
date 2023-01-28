import pypyodbc
# from FunkoppdaterHest import FunkoppdaterHest
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=****')
# print(Lastedato.DatoKlasse)
if con:
    print("ja vi elsker dette landet og har forbindelse")
   
SQL = '''\
SELECT id_nr, Navn 

  FROM [Trav].[dbo].[AlleHesterBackup3]
  Where Nasjon  not in ('Norge')

'''     
cursor = con.cursor()
cursor.execute(SQL)
# prosentgallop = 0
#dato = cursor
#cursor.next()

for a in cursor:
#     print(a[0], a[1], a[2])
    
    id_nr = a[0]
    Navn     = a[1] 
    idnroppdatere = id_nr
    Hestenummer = id_nr
    if id_nr == None:
        print(Navn,"Problemer med id nr")
        with open('mangleridnrAllehester.txt', 'a') as f:
                
            f.write("%s;%s" % \
             ( id_nr,Navn))
            f.write('\n')
#     print(Hestenummer,"verdi til hestenummer i Hoved Program")
#     FunksjonlesResultat(id_nr)
    else:
        skilletegn = '*'
        posisjonstjerne=Navn.find(skilletegn)
        print(posisjonstjerne,'Posisjom til skilletegn')
        HeleNavn = Navn[0:posisjonstjerne]
#Sjekk om navn slutter pa (        
        print(HeleNavn,"Navn uten * (s)")
        posisjonslpar = HeleNavn.find('(')
        if  posisjonslpar > 0:
            HeleNavn = HeleNavn[0:posisjonslpar]
        with open('Allehesteroppdater.txt', 'a') as f:
                
            f.write("%s;%s" % \
             ( id_nr,HeleNavn))
            f.write('\n')
#         oppdater = FunkoppdaterHest(idnroppdatere,HeleNavn )
   
cursor.close() 
