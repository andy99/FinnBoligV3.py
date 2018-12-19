from bs4 import BeautifulSoup
import requests 
import os
# import time
from GyldigeBanerNavn import GyldigeBanerNavn
from Lopkalendar import Lopkalendar
from datetime import date
dagensdato = date.today()
#Leser lopskalender
dagenslop=Lopkalendar()
print(dagenslop,"Dagen lops bane")
# For testing
# Bane ='Be%'
Bane=dagenslop
gyldigbane = dagenslop[0:4]+"%"
print(gyldigbane,"Her bane som vi skal laste startlister for")
bane=gyldigbane
if bane[0] == 'S':
    bane= 'Sor%'
    print(bane,"Vi skal ha bane sor")
    gyldigbane = bane
print(dagensdato,"dagen i dag")
testdato=dagensdato.strftime('%Y%m%d')
Bane=GyldigeBanerNavn(gyldigbane)
print(Bane,"Etter kall til finn gyldig bane")
inndata = testdato
print(testdato,"etterformattering")
print(inndata,"Inndata")
# aar = dagensdato()
# print(aar,"Ar er ")
t = dagensdato.timetuple()
# print(t,"Viser t")
# for i in t:
#     print(i,"Viser dato?")
#     aar = t(0)
#     print(aar,"viser aar")
# bane = "Biri-Travbane"
# ("http://www.travsport.no/Sport/Resultater/Bjerke-Travbane/?date=" & allelastedato)
print(Bane,"Hvilken bane")
if os.path.isfile("D:\workplace_python\TravAnalyse\DntStartListertest.txt"):
    print("D:\workplace_python\TravAnalyse\DntStartlistertest.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\DntStartListertest.txt")
coding='utf8'
# & allelastedato
webbane = requests.get('http://www.travsport.no/Sport/Startlister/{}'.format(Bane))   #Dette virker
startliste = requests.get('http://www.travsport.no/Sport/Startlister/{}'.format(Bane)+'/?date=' + inndata )   #Dette virker 

print(startliste," S har vi funnet en webside") 
# print(t," T har vi funnet en webside")
soup = BeautifulSoup(startliste.content,"html.parser")
# print(soup,"Hva er soup")
lopdato=soup.find_all("h2")[1].get_text()
print(lopdato,"Lopsdato")
Starttabell = soup.find_all('table')
#print(Starttabell[1],"hestetabell")
#    antalltabeller = len(Hesttabell)
    #print(antalltabeller,"Antall tabeller")
wkol = 0
lop = 0
lopinformasjon=["Gunnar"]
with open('DntStartListertest.txt', 'a') as f:
#         for tr in enumerate(Hesttabell[1]):
    teller = 0 
#     lop = 0
    for tr in soup.find_all('tr')[0:]:
        tds = tr.find_all('td')
        antrader = len(tr)
#         print(antrader,"Antall rader")
        antkol = len(tds)
#         if antrader == 3:
#             print(tds[0] , " Her har vi antall kolloner =1innhold antal kolonner er 1")
        
        print(antkol,"Antall kolloner") 
        wkol = 0
        wkol = antkol
        lopnr = 0
#         lop = 0
        if antkol == 1:
            print(tds[0].text.strip(), "Hva er innholdet nar kun 1 kollone")
            lopinformasjon = tds[0].text.strip()
            print(lopinformasjon, "Hva er Lopinformasjon")
            print( lopinformasjon.find(".Premier"))
            startmetodefinn = lopinformasjon.find("Autostart")
            print(startmetodefinn,"Hva er verdien pa startmetode finn")
            if startmetodefinn > 0:
                startmetode = "Autostart"
            else:
                startmetode = "Volestart"    

        if antkol == 7:    
            startnr = tds[1].text.strip()
            if startnr in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'):
                    startnrint = int(startnr)


            if startnrint == 1:
                lop += 1 
                lopnr = lopnr + lop
#                 print(lop,"Lop skal plusses med en for ") 
#                 print(lopnr,"Lopnr skal plusses med en for ")                     
            f.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
            (startmetode,lopdato,lop,tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(),tds[3].text.strip(), tds[4].text.strip(),tds[5].text.strip(),tds[6].text.strip()))
            f.write('\n')
        else:
                #print(tds,"Antall kolonner  er ikke 7")
                lopinfo = tr.find_all('caption')
                antlop = len(lopinfo)