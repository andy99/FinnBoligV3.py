from bs4 import BeautifulSoup
import requests 
import os
#import LeserDNTdatofradatabase
# from token import NEWLINE
coding='utf8'
if os.path.isfile("D:\workplace_python\pythonapp\Kuskeinfo.txt"):
    print("D:\workplace_python\pythonapp\Kuskeinfo.txt","blir slettet")
    os.remove("D:\workplace_python\pythonapp\Kuskeinfo.txt")
num = 415
while num < 416:
#     num = 9
#    Lastedato.Dato
    #print(LeserDNTdatofradatabase.Lastedato)
    #r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
#     r = requests.get("http://www.travsport.no/Sport/Resultater/Bergen-Travpark/")
    r = requests.get("http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-kusk/?modus=0&search=Svein+Ove+Wassberg")
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    print(soup,"innhold soup")
    Kusktabell = soup.find_all('table')
    print(Kusktabell[1],"Kusktabell")
    antalltabeller = len(Kusktabell)
    
    print(antalltabeller,"Antall tabeller")
    wkol = 0
    with open('Kuskeinfo.txt', 'a') as f:
#         for tr in enumerate(Hesttabell[1]):
        teller = 0 
        for tr in soup.find_all('tr')[2:]:
            print(tr,'Skriver tr i tabell 1')
            tds = tr.find_all('td')
            antrader = len(tr)
            
            print(antrader,"Antall rader")
            antkol = len(tds)
            print(antkol,"Antall kolloner") 
            wkol = 0
            wkol = antkol
            lopnr = 0
            if antkol == 4:                              
                #print(tds,'innhold td')
                #beregne lopsnr
                f.write(" %s;" % \
                ( tds[0].text.strip()))
                f.write('\n')
                f.write(" %s;" % \
                ( tds[1].text.strip()))
                f.write('\n')
                f.write(" %s;" % \
                ( tds[2].text.strip()))
                f.write('\n') 
                f.write(" %s;" % \
                ( tds[3].text.strip()))
                f.write('\n')            
            else:
                #print(tds,"Antall kolonner  er ikke 7")
                lop = tr.find_all('caption')
                antlop = len(lop)
#                 if antlop > 0 :
#                     print(lop[0],"lopsnr")