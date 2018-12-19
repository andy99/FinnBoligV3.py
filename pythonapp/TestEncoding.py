from bs4 import BeautifulSoup
import requests
#from RaderKolloner import tabell_rader
#from idlelib.replace import replace
#r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=123599" )
r = requests.get("http://www.alltidhest.org/Horses/Page/1" )
#print('Hello Gunnar ')
r.content
#print(r.content,"Hello Gunnar")
soup = BeautifulSoup(r.content,"html.parser")
#print(r.content)
test1=r.content
rad= []
nytekst = []
tabell_rader =[]
tabell = soup.find("table")
#tabell_rader = tabell.find_all('tr')
#print(tabell,"hallo gunnar her er tabellen")
#tabell_rader[0] er overskrift
#print(tabell_rader[0],"hallo Niko her er tabell raden")
# for td in tabell_rader:
#     td = td.find_all('td')
#     rad = [m.text.strip() for m in td]
#     tekst = td[0].text
#     print(rad,"Data i tabell rad")
#     
with open('output.txt', 'w') as f:
    for tr in soup.find_all('tr')[2:]:
        tds = tr.find_all('td')
        print(tds[0].text + tds[1].text)
        f.write("ID: %s, Regnr: %s, Navn: %s, Regnr: %s, Alder :%s, Kjonn:%s, Farge: %s, Land: %s" % \
              (tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(),tds[7].text.strip()))
        f.write('\n')
            
   

# antrader = len(rad) - 1
# print(antrader,"Antall rader")
# tabell_rader = rad
# for i, value in enumerate(tabell_rader):
#     print(i,tabell_rader[antrader],"tabell rader")
#     with open("Hestedata3.txt","w") as r:
#         r.write(tabell_rader[antrader])
# #         
# while antrader < 8 and antrader > 0:
#     print(antrader,"Antallrader mindre enn 7?")
#     print(tabell_rader[antrader],"Innhold tabell")
#     antrader = antrader - 1
#     
