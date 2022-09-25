import pypyodbc
from Funkstarterkusk import Funkstarterkusk
from Funkkusk1plass import Funkkusk1plass
from FunkKusktrippel import FunkKusktrippel
from Funkkuskgalopp import Funkkuskgalopp
import os
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
if con:
    print("ja vi har forbindelse Hovedprorgam kusker")
    
if os.path.isfile("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt"):
    print("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Antallstarterkusk.txt")
SQL = '''\
SELECT Kuskidnr,Navn

  FROM [DWtrav].[dbo].[DIM_Kusker]

'''     
cursor = con.cursor()
cursor.execute(SQL)
for a in cursor:
#     print(a[0], a[1], a[2])
    
    Kuskidnr = a[0]
    Kuskenavn = a[1]
    if Kuskidnr == None:
#         print(Kuskidnr,"Problemer med Kuskidnr")
        with open('D:\workplace_python\TravAnalyse\Kuskmangleridnr.txt', 'a') as f:
                
            f.write("%s;%s" % \
             ( Kuskidnr,Kuskenavn))
            f.write('\n')
#     print(Hestenummer,"verdi til hestenummer i Hoved Program")
#     FunksjonlesResultat(id_nr)
    else:
        prosentvunnet=0
        Antallstartekusk=Funkstarterkusk(Kuskidnr)
        Antallvunnet=Funkkusk1plass(Kuskidnr)
        Anttalltrippel=FunkKusktrippel(Kuskidnr)
        Antallgalloper=Funkkuskgalopp(Kuskidnr) 
#         NavnKusk=Funkstarterkusk(Kuskidnr)
#         antallstartkuskidnr=Funkstarterkusk(Kuskidnr)
        if Antallvunnet > 0:
            prosentvunnet = (Antallvunnet/Antallstartekusk) * 100
            prosenttrippel = (Anttalltrippel/Antallstartekusk) * 100
            prosentgallop  = (Antallgalloper/Antallstartekusk) * 100
        else:
            prosentvunnet=0 
            prosenttrippel =0  
            prosentgallop = 0  
        with open('D:\workplace_python\TravAnalyse\Antallstarterkusk.txt', 'a') as f:
            
            f.write("%s;%s;%.2f;%s;%.2f;%s;%.2f;%s;%s" % \
            (Antallstartekusk,Antallvunnet,prosentvunnet,Anttalltrippel,prosenttrippel,Antallgalloper,prosentgallop,Kuskenavn,Kuskidnr))
            f.write('\n')
        
            

cursor.close() 

# global prosentgallop
# utdata = 0