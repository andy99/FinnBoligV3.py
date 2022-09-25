from bs4 import BeautifulSoup
import requests 
import os
from funkformatdato import funkformatdato
#import LeserDNTdato
# from token import NEWLINE
coding='utf8'
if os.path.isfile("D:\workplace_python\TravAnalyse\Bergenresultatdatoer.txt"):
    print("D:\workplace_python\TravAnalyse\Bergenresultatdatoer.txt","blir slettet")
    os.remove("D:\workplace_python\TravAnalyse\Bergenresultatdatoer.txt")
num = 415
while num < 416:
#     num = 9
#    Lastedato.Dato
    #print(LeserDNTdato.Lastedato)
    #r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
#     r = requests.get("http://www.travsport.no/Sport/Resultater/Bergen-Travpark/")
    r = requests.get("http://www.travsport.no/Sport/Resultater/Bergen-Travpark/")
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    Hesttabell = soup.find_all('tbody')
    #print(Hesttabell[1],"hestetabell")
    antalltabeller = len(Hesttabell)
    banenavn ='Bergentravpark'
    baneid   = '8'
    #print(antalltabeller,"Antall tabeller")
    wkol = 0
    with open('Bergenresultatdatoer.txt', 'a') as f:
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
            if antkol == 4:                              
                #print(tds,'innhold td')
                #beregne lopsnr
                rdato0=tds[0].text.strip()
                reslutdato0 = funkformatdato(rdato0)
                rdato1=tds[1].text.strip()
                reslutdato1 = funkformatdato(rdato1)
                rdato2=tds[2].text.strip()
                reslutdato2 = funkformatdato(rdato2)
                rdato3=tds[3].text.strip()
                reslutdato3 = funkformatdato(rdato3)
                print(reslutdato0,'Formatterert resultat dato')
                f.write(" %s;%s;%s" % \
                ( reslutdato0,banenavn,baneid ))
                f.write('\n')
                f.write(" %s;%s;%s" % \
                ( reslutdato1,banenavn,baneid))
                f.write('\n')
                f.write(" %s;%s;%s" % \
                ( reslutdato2,banenavn,baneid))
                f.write('\n') 
                f.write(" %s;%s;%s" % \
                ( reslutdato3,banenavn,baneid))
                f.write('\n')            
            else:
                #print(tds,"Antall kolonner  er ikke 7")
                lop = tr.find_all('caption')
                antlop = len(lop)