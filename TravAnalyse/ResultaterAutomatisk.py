from bs4 import BeautifulSoup
import requests 
import os
# import time
from GyldigeBanerNavn import GyldigeBanerNavn
from sjekkresultater import sjekkresultater
from tellantallresultatbane import tellantallresultatabaner
from TabResultatMan import TabResultatMan
from SlettResMan import SlettResMan
from datetime import date
dagensdato = date.today()
SlettResMan()
TabResultatMan()
#Leser lopskalender
resultatinfo=sjekkresultater()
antallbaner = tellantallresultatabaner()
print(antallbaner," Antall Resultat lops bane")
print(resultatinfo,"Resultat lops bane")
# For testing
# Bane ='Be%'
Bane=resultatinfo[0]
nybane= Bane.replace(' ', '-')
finnstrek=nybane.find('-')
nybane2 =nybane[0:finnstrek-1]+"%"
#Finner gyldig bane
nybane3 = GyldigeBanerNavn(nybane2)
print(finnstrek,"Posisjon strek")
print(nybane2,"nybane2")
print(nybane3,"nybane3")
inndato = resultatinfo[1]
inndatoaar =inndato[0:4]
inndatomnd =inndato[5:7]
inndatodag =inndato[8:10]
print(inndatoaar,"Her aar Gunnar")
print(inndatomnd,"Her mnd Gunnar")
print(inndatodag,"Her dag Gunnar")
print(Bane,"Her bane som vi skal laste Resultater for")
print(nybane,"Her bane med strek --som vi skal laste Resultater for")
print(inndato,"Her dato som vi skal laste Resultater for")
bane=Bane
if bane[0] == 'S':
    bane= 'Sor%'
    print(bane,"Vi skal ha bane sor")
    gyldigbane = bane
print(dagensdato,"dagen i dag")
testdato=dagensdato.strftime('%Y%m%d')
#Bane=GyldigeBanerNavn(gyldigbane)
print(Bane,"Etter kall til resultat bane")
#inndata = testdato
inndato = inndatoaar + inndatomnd + inndatodag
print(nybane3,"Hvilken bane")
print(inndato,"Hvilken dato")
if os.path.isfile("D:\workplace_python\TravAnalyse\Dntresultatlistertest.txt"):
    print("D:\workplace_python\TravAnalyse\Dntresultatlistertest.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Dntresultatlistertest.txt")
coding='utf8'
# & allelastedato
resultatliste = requests.get('http://www.travsport.no/Sport/Resultater/{}'.format(nybane3)+'/?date=' + inndato)
#webbane = requests.get('http://www.travsport.no/Sport/Startlister/{}'.format(Bane))   #Dette virker
#startliste = requests.get('http://www.travsport.no/Sport/Startlister/{}'.format(Bane)+'/?date=' + inndata )   #Dette virker 

#print(resultatliste," S har vi funnet en webside") 
# print(t," T har vi funnet en webside")
soup = BeautifulSoup(resultatliste.content,"html.parser")
#print(soup,"Hva er soup")
lopdato=soup.find_all("h2")[1].get_text()
print(lopdato,"Lopsdato")
Starttabell = soup.find_all('table')
#print(Starttabell[1],"hestetabell")
#    antalltabeller = len(Hesttabell)
    #print(antalltabeller,"Antall tabeller")
for h2 in soup.find_all('h2')[1]: 
        print(h2,"Innhold h2")
        banenavn =h2
        print(banenavn,"Innhold banenavn")
            
wkol = 0
lop = 0
lopinformasjon=["Gunnar"]
with open('D:\workplace_python\TravAnalyse\Dntresultatlistertest.txt', 'a') as f:
#         for tr in enumerate(Hesttabell[1]):
    teller = 0 
#     lop = 0
    teller = 0 
    for tr in soup.find_all('tr')[2:]:
            #print(tr,'Skriver tr i tabell 1')
            tds = tr.find_all('td')
#             antrader = len(tr)
            #print(antrader,"Antall rader")
            antkol = len(tds)
            print(antkol,"Antall kolloner")
            if antkol == 4:
                premisum = tds[0].text.strip()
                Distanse = tds[1].text.strip()
                Baneverdi = tds[2].text.strip()
                Startmetode = tds[3].text.strip()
                print (premisum,'Her har vi premiesum')
                sjpremie = premisum[0:9] #Total premiesum for lopet
                print(sjpremie,"sjpremie har verdi")
                if sjpremie == "Premiesum":
                    print(sjpremie,"Her har vi premisum")
                    tallpremiesum = premisum[10:]
                    print(tallpremiesum,"tall premiesum")
                print (Distanse,'Her har vi Distanse')
                sjdistanse = Distanse[0:8]
                print(sjdistanse,"Sjdistanse har verdi")
                if sjdistanse == "Distanse":
                    lopdistanse = Distanse[9:] #distanse i lopet finnes ogsa pr resultat 
                    
                    print(lopdistanse,"Distansen i lopet")
                print (Baneverdi,'Her har vi Baneverdi')   #Denne brukes ikke
                print (Startmetode,'Her har vi Startmedode')
                sjauto = Startmetode[0:11]
                print(sjauto,"Har vi startmeode?")
                if sjauto == "Startmetode":
                    utstartmetode = Startmetode[13:]
                    print(utstartmetode,"Startmetode til fil")
                    
#           wkol = 0
            plasingint = 0
#             wkol = antkol
            lopnr = 0
            if antkol == 9:
                plassering = tds[0].text.strip()
                print(plassering,'Plassering etter strip func')
                if plassering in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'):
                    plasingint = int(plassering)
                if type(plasingint) == int:
                    print (plassering,'Her har vi integer')
                else:
                    print (plassering,'Not an integer or a floating point decimal!' )                   
                                              
                print(tds[5],"Kmtid")
                kmtid = tds[5].text.strip()
#                 sjgallop = kmtid
                sjgallop = kmtid.find('g')
                print(sjgallop,"Sjgallop har verdien")
                utgallop="Ingen galopp "
                if sjgallop > 1:
                    utgallop = "galopp"
                    print(utgallop,"Her har vi galopp")
                if plasingint  == 1 :
                    lopnr = lopnr +1
                    teller = teller + 1
                    print(teller,'lop teller') #Teller blir det samme som lop nr
                                                  
                 
                f.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
                 ( banenavn.strip(), tallpremiesum, lopdistanse, teller,utstartmetode,utgallop, tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(),tds[7].text.strip(),tds[8].text.strip()))
                f.write('\n')
                  
            else:
                #print(tds,"Antall kolonner  er ikke 9")
                lop = tr.find_all('caption')
#                 antlop = len(lop)