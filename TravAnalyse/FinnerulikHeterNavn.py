import pypyodbc
import os
from Funksjekkidnr import Funksjekkidnr
from UpdateUlikenavn import UdateUlikenavn
if os.path.isfile("D:\workplace_python\TravAnalyse\Sjekkidnr.txt"):
    print("D:\workplace_python\TravAnalyse\Sjekkidnr.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Sjekkidnr.txt")
con = pypyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-0CMQN56;''Database=DWtrav;''user=Gunnar;' 'Pwd=gunnar')
if con:
    print("ja vi har forbindelse Hovedprorgam Finnerulikheternavn")
# SQL = '''\    
# SELECT Heste_navn, Navn, Id_nr
#   FROM [Trav].[dbo].[StartLister]
#   where Heste_navn <> Navn
# '''
SQL = '''\
Select  distinct Heste_navn, Navn, id_nr, Bane, dato

  FROM [Trav].[dbo].[StartLister]
  Where Heste_navn <> Navn
  and Navn <> ' '
    
'''         
cursor = con.cursor()
cursor.execute(SQL)
navnulike = False
for a in cursor:
#     print(a[0], a[1], a[2])
    
    Hestenavn = a[0]
    Navn      = a[1] 
    id_nr     = a[2]
    Bane      = a[3] 
    Dato      = a[4]     
    sjnavnlen = len(Navn)
    sjnavn = (Navn[0:sjnavnlen-4])
    sjnavn=sjnavn.strip()
    Navn = Navn.strip()
    Hestenavn = Hestenavn.strip()
    navnulike = False
    
    
#     print (sjnavn,"Verdi til sjnavn")
# Sjekker om * i navnet
    stjerne=Navn.find("*",0, sjnavnlen)
#     print(stjerne,"Har vi stjerne i navnet")
#     print(Hestenavn,"Skriver Hestenavn")
#     print(Navn,"Skriver Navn")
#     print(sjnavn,"Skriver sjNavn")
#     print(id_nr,"Skriver id_nr")
    if sjnavn != Hestenavn:
        navnulike = True
    if stjerne > 0:
        navnulike = False
#         print(Navn,"Navne er like")
    if navnulike ==True:
        RetHestenavn=Funksjekkidnr(id_nr,Navn)
        print(RetHestenavn,"Rett hestenavn er ")
        uidnr = RetHestenavn["idnr"]
        unavn = RetHestenavn["navn"]
        SQL1 = '''\
        SELECT *
         FROM [Trav].[dbo].[StartLister]
         Where Id_Nr =30085797
        '''
#         cursor.execute(SQL1)
        print(uidnr,"Idnr som skal rettes updateres")
        print(unavn,"Navn  som skal rettes updateres")
        oppdaterenavn = UdateUlikenavn(uidnr,unavn)
        with open('Sjekkidnr.txt', 'a') as f:
            f.write("%s;%s;%s;%s;%s" % \
             ( id_nr,Hestenavn,Navn,Bane,Dato))
            f.write('\n')
#     id_nrallehester = Funksjekkidnr(id_nr)
cursor.close() 