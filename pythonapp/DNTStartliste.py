from bs4 import BeautifulSoup
import requests 
coding='utf8'
num = 415
while num < 416:
#     num = 9
    print(num)
    #r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
    r = requests.get("http://www.travsport.no/Sport/Startlister/Bjerke-Travbane/?date=20180110")
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    Hesttabell = soup.find_all('tbody')
    #print(Hesttabell[1],"hestetabell")
    antalltabeller = len(Hesttabell)
    #print(antalltabeller,"Antall tabeller")
    wkol = 0
    with open('Dntstartliste.txt', 'a') as f:
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
            if antkol == 7:                              
                #print(tds,'innhold td')
                #beregne lopsnr
                gmlstartnrint = 0
                startnr = tds[1].text.strip()
                startnrint = int(startnr)
                
                gmlstartnrint = 0
                if startnrint == 1 :
                    lopnr = lopnr +1
                    teller = teller + 1
                    print(teller,'lop teller')
                    
                    nylopnr = lopnr
                    print(lopnr,"Lopnr er  i ja loop")
                    gmlstartnr =startnrint
                    if gmlstartnrint > startnrint :
                        lopnr = lopnr +1
                else:
                    lopnr = nylopnr
#                     #gmlstartnr =startnrint
                    gmlstartnr = tds[1].text.strip()
                    gmlstartnrint = int(gmlstartnr)
                    print(gmlstartnr,"Forrige startnr")  
                    print(startnr,"Startnr er i nei loop startnr <> 1")
                f.write(" %s, %s, %s, %s, %s, %s, %s, %s" % \
                 ( teller, tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip()))
                f.write('\n')  
            else:
                #print(tds,"Antall kolonner  er ikke 7")
                lop = tr.find_all('caption')
                antlop = len(lop)
#                 if antlop > 0 :
#                     print(lop[0],"lopsnr")
                 
        
         
        
    
#     with open('AlltidHest.txt', 'a') as f:
#         for tr in soup.find_all('tr'):
#             print(tr,"Innhold tabell rad")
#             tds = tr.find_all('td')
#             print(tds,"innhold tds")
#             f.write("Regnr: %s" % \
#                 ( tds))
#             f.write('\n')   
#             