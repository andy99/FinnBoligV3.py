import pypyodbc
from FunkFakta import FunkFakta
from Funkvinner import Funkvinner
from Funktrippel import Funktrippel
from Funkstarter import Funkstarter
from Funkplass import Funkplass
import os
if os.path.isfile("D:\workplace_python\TravAnalyse\GaloppprosentFelles.txt"):
    print("D:\workplace_python\TravAnalyse\GaloppprosentFelles.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\GaloppprosentFelles.txt")
#feil fil de som mangler idnr m hente nye data fra alltid hest    
if os.path.isfile("D:\workplace_python\TravAnalyse\Galoppprosentmangleridnr.txt"):
    print("D:\workplace_python\TravAnalyse\Galoppprosentmangleridnr.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Galoppprosentmangleridnr.txt")

global prosentgallop
utdata = 0
con = pypyodbc.connect
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=Trav;''user=Gunnar;' 'Pwd=gunnar')
# print(Lastedato.DatoKlasse)
if con:
    print("ja vi elsker dette landet og har forbindelse")
   
SQL = '''\
Select Heste_navn, Kusk, id_nr

  FROM [Trav].[dbo].[StartLister]
  
'''     
cursor = con.cursor()
cursor.execute(SQL)
# prosentgallop = 0
#dato = cursor
#cursor.next()

for a in cursor:
#     print(a[0], a[1], a[2])
    
    Hestenavn = a[0]
    Kusk      = a[1] 
    id_nr     = a[2]
    Hestenummer = id_nr
    if id_nr == None:
        print(Hestenavn,"Problemer med id nr")
        with open('Galoppprosentmangleridnr.txt', 'a') as f:
                
            f.write("%s;%s" % \
             ( Hestenummer,Hestenavn))
            f.write('\n')
#     print(Hestenummer,"verdi til hestenummer i Hoved Program")
#     FunksjonlesResultat(id_nr)
    else:
        prosentgallop=FunkFakta(Hestenummer)
        antstarter=Funkstarter(Hestenummer)
        plassering123=Funkplass(Hestenummer)
#         print(plassering123,Hestenummer,"sisteplassering")
        prosentvinner=Funkvinner(Hestenummer)
        prosenttrippel=Funktrippel(Hestenummer)
#     print( prosenttrippel,Hestenummer,"Hoved program prosent trippel" )
        with open('GaloppprosentFelles.txt', 'a') as f:
                
            f.write("%.0f;%.0f;%.0f;%.0f;%.0f;%s" % \
             ( prosentgallop,prosentvinner,prosenttrippel,antstarter,plassering123,Hestenummer))
            f.write('\n')

cursor.close() 



    