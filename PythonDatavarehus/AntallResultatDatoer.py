#Finner antall resultat datoer bane
from bs4 import BeautifulSoup
import requests 
import os
#import LeserDNTdatofradatabase
# from token import NEWLINE
coding='utf8'
Bane='Klosterskogen-travbane'   
r = requests.get('http://www.travsport.no/Sport/Resultater/{}'.format(Bane))
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 
num = num + 1
antradesamenlagt = 0
r.content
soup = BeautifulSoup(r.content,"html.parser")
print(soup,"Innhold Soup")
Hesttabell = soup.find_all('href')
print(Hesttabell,"hestetabell")
antalltabeller = len(Hesttabell)

for tr in soup.find_all('tr')[2:]:
            #print(tr,'Skriver tr i tabell 1')
#            tds = tr.find_all('td')
            antrader = len(tr)
            antradesamenlagt = antrader + antradesamenlagt
            print(antrader,"Antall rader")
            print(antradesamenlagt,"antradesamenlagt")
antresultatdatoer = antradesamenlagt
print(antresultatdatoer,"Antall datoer")

