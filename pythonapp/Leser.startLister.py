# Leser rstartlisterhttp://www.travsport.no/Sport/StartLister/Leangen-Travbane/?date=20180423
from bs4 import BeautifulSoup
import requests 
#import LeserDNTdatofradatabase
# from token import NEWLINE
coding='utf8'
r = requests.get("http://www.travsport.no/Sport/StartLister/Leangen-Travbane/?date=20180429")
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 

r.content
soup = BeautifulSoup(r.content,"html.parser")
lopdato=soup.find_all("h2")[1].get_text()
print(lopdato,"Lopsdato")
Starttabell = soup.find_all('table')
#print(Starttabell[1],"hestetabell")
#    antalltabeller = len(Hesttabell)
    #print(antalltabeller,"Antall tabeller")
wkol = 0
lop = 0
with open('DntStartleangen.txt', 'a') as f:
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
        
#         print(antkol,"Antall kolloner") 
        wkol = 0
        wkol = antkol
        lopnr = 0
#         lop = 0
        if antkol == 7:    
            startnr = tds[1].text.strip()
            if startnr in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'):
                    startnrint = int(startnr)
#             print(startnrint,"Startnr") 
#             startnrint 

#             if type(startnrint) == int:
#                 print (startnr,'Her har vi integer')
#             else:
#                 print (Startnr,'Not an integer or a floating point decimal!' )                   
#                                               
            if startnrint == 1:
                lop += 1 
                lopnr = lopnr + lop
#                 print(lop,"Lop skal plusses med en for ") 
#                 print(lopnr,"Lopnr skal plusses med en for ")                     
            f.write("%s;%s;%s;%s;%s;%s" % \
            (lopdato,lop,tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(),tds[3].text.strip()))
            f.write('\n')
        else:
                #print(tds,"Antall kolonner  er ikke 7")
                lopinfo = tr.find_all('caption')
                antlop = len(lopinfo)
#                 print(lop,'Hva er inholder her? er lop')
#                 print(antlop,"Er dette antall lop?")
#                 if antlop > 0 :
#                     print(lop[0],"lopsnr")
                 