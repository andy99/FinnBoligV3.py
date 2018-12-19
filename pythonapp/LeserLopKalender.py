from bs4 import BeautifulSoup
import requests 
import os
if os.path.isfile("D:\workplace_python\pythonapp\Lopkalender.txt"):
    print("D:\workplace_python\pythonapp\Lopkalender.txt","blir slettet")
    os.remove("D:\workplace_python\pythonapp\Lopkalender.txt")
coding='utf8'
r = requests.get("http://www.travsport.no/Sport/Terminliste/")
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 

r.content
soup = BeautifulSoup(r.content,"html.parser")
# lopdato=soup.find_all("h2")[1].get_text()
# print(lopdato,"Lopsdato")
# Starttabell = soup.find_all('table')
#print(Starttabell[1],"hestetabell")
#    antalltabeller = len(Hesttabell)
    #print(antalltabeller,"Antall tabeller")
wkol = 0
lop = 0
lopinformasjon=["Gunnar"]
with open('Lopkalender.txt', 'a') as f:
#         for tr in enumerate(Hesttabell[1]):
    teller = 0 
#     lop = 0
    for tr in soup.find_all('tr')[0:]:
        tds = tr.find_all('td')
        antrader = len(tr)
        print(antrader,"Antall rader")
        antkol = len(tds)
        print(antkol,"Antall koloner")
#         if antrader == 3:
#             print(tds[0] , " Her har vi antall kolloner =1innhold antal kolonner er 1")
        
#         print(antkol,"Antall kolloner") 

            
        if antkol == 3:    
            startnr = tds[1].text.strip()


                   
            f.write("%s;%s" % \
            (tds[0].text.strip(), tds[1].text.strip()))
            f.write('\n')
        else:
                #print(tds,"Antall kolonner  er ikke 7")
                lopinfo = tr.find_all('caption')
                antlop = len(lopinfo)