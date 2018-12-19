from bs4 import BeautifulSoup
import requests 
from FunksjonleserWeb import FunksjonleserWeb
#!/usr/bin/python
coding='utf-8'
Lastedato = '20060202'
#coding='utf8'
FunksjonleserWeb(Lastedato)
num = 415
while num < 416:
#     num = 9
    print(num)
    #r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
    r = requests.get("http://www.travsport.no/Sport/Resultater/Bergen-Travpark/?date=" + Lastedato)
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    Hesttabell = soup.find_all('tbody')
    #print(Hesttabell[1],"hestetabell")
    antalltabeller = len(Hesttabell)
    datobanenavn = soup.find('div' , class_ ="article")
    #print(datobanenavn,"Datobanenavn")
    banenavn = " "
    for h2 in soup.find_all('h2')[1]:
        print(h2,"Innhold h2")
        banenavn =h2
        print(banenavn,"Innhold banenavn")
        
        
    #print(antalltabeller,"Antall tabeller")
    wkol = 0
    with open('DNTResulatListe.txt', 'a') as f:
#         for tr in enumerate(Hesttabell[1]):
        teller = 0 
        for tr in soup.find_all('tr')[2:]:
            #print(tr,'Skriver tr i tabell 1')
            tds = tr.find_all('td')
            antrader = len(tr)
            #print(antrader,"Antall rader")
            antkol = len(tds)
            #print(antkol,"Antall kolloner") 
            wkol = 0
            wkol = antkol
            lopnr = 0
            if antkol == 9:
                plassering = tds[0].text.strip()
                print(plassering,'Plassering etter strip func')
                if plassering in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14'):
                    plasingint = int(plassering)
                if type(plasingint) == int:
                    print (plassering,'Her har vi integer')
                else:
                    print (plassering,'Not an integer or a floating point decimal!' )                   
                                              
                
                if plasingint  == 1 :
                    lopnr = lopnr +1
                    teller = teller + 1
                    print(teller,'lop teller')
                                                  
                 
                f.write(" %s; %s; %s; %s; %s; %s; %s; %s; %s, %s,%s" % \
                 ( banenavn.strip(),teller, tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(),tds[7].text.strip(),tds[8].text.strip()))
                f.write('\n')  
            else:
                #print(tds,"Antall kolonner  er ikke 9")
                lop = tr.find_all('caption')
                antlop = len(lop)

