# Hoved program for uthent av resultatdatoer Bjerke
from bs4 import BeautifulSoup
import requests
import os

# import LeserDNTdatofradatabase
# from token import NEWLINE
coding = 'utf8'
if os.path.isfile("D:\workplace_python\DNTOdds\Dntresultatdatoer.txt"):
    print("D:\workplace_python\DNTOdds\Dntresultatdatoer.txt", "blir slettet")
    os.remove("D:\workplace_python\DNTOdds\Dntresultatdatoer.txt")
Bane = 'Bergen-travpark'
num = 415
while num < 416:
    #     num = 9
    #    Lastedato.Dato
    # print(LeserDNTdatofradatabase.Lastedato)
    # r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
    #     r = requests.get("http://www.travsport.no/Sport/Resultater/Bergen-Travpark/")
    #     r = requests.get("http://www.travsport.no/Sport/Resultater/Banenavn/")
    r = requests.get('http://www.travsport.no/Sport/Resultater/{}'.format(Bane))
    #                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content, "html.parser")
    Hesttabell = soup.find_all('tbody')
    #    print(Hesttabell[1],"hestetabell")
    antalltabeller = len(Hesttabell)

    print(antalltabeller, "Antall tabeller")
    wkol = 0
    with open('D:\workplace_python\DNTOdds\Dntresultatdatoer.txt', 'a') as f:
        #         for tr in enumerate(Hesttabell[1]):
        teller = 0
        for tr in soup.find_all('tr')[2:]:
            # print(tr,'Skriver tr i tabell 1')
            tds = tr.find_all('td')
            antrader = len(tr)

            # print(antrader,"Antall rader")
            antkol = len(tds)
            # print(antkol,"Antall kolloner")
            wkol = 0
            wkol = antkol
            lopnr = 0
            if antkol == 4:
                # print(tds,'innhold td')
                # beregne lopsnr
                f.write(" %s;%s" % \
                        (Bane, tds[0].text.strip()))
                f.write('\n')
                f.write(" %s; %s" % \
                        (Bane, tds[1].text.strip()))
                f.write('\n')
                f.write(" %s;%s" % \
                        (Bane, tds[2].text.strip()))
                f.write('\n')
                f.write(" %s;%s" % \
                        (Bane, tds[3].text.strip()))
                f.write('\n')
            else:
                # print(tds,"Antall kolonner  er ikke 7")
                lop = tr.find_all('caption')
                antlop = len(lop)
#                 if antlop > 0 :
#                     print(lop[0],"lopsnr")
