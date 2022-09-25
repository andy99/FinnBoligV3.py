from bs4 import BeautifulSoup
print("Hallo Gunnar")
coding='utf-8'
import requests 
#!/usr/bin/python

def FunkWebodds(webdato):
    #     Lastedato = '20180313'
    Lastedato = webdato
    print(webdato," Na er vi i FunkWebodds Gunnar ")
#     print(Lastedato," Lastedato er i funksjon Leser hestedata Gunnar Hurra ")  
    #r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
#     r = requests.get("http://www.travsport.no/Sport/Resultater/Leangen-Travbane/?date=" + Lastedato"
    r = requests.get("http://www.travsport.no/Sport/Resultater/Biri-Travbane/?date=" + Lastedato)
    s = requests.get("http://www.travsport.no/Sport/Resultater/Leangen-Travbane/?date=" + Lastedato)
    s.content
    soup = BeautifulSoup(s.content,"html.parser")
#     Hesttabell = soup.find_all('tbody')[0]
#     antalltabeller = len(Hesttabell)
    datobanenavn = soup.find('div' , class_ ="article")
    txtalign = soup.find_all('td' , class_ ="textalign")
#     print(txtalign,"innhold txtalign")
    banenavn =  soup.find('div', id="article")
    utbanenavn = banenavn.text.strip()
    lopnr = 0
#     utvinnerodds = 0    
    utvinneroms=0
    with open('D:\workplace_python\DNTOdds\DNTodds.txt', 'a') as g:
#         for tr in soup.find_all('tr')[0]:
        teller = 0 
        for th in soup.find_all('th'):
            koloverskift = th.text
            print(koloverskift, "Innhold kol overskrift")
            sjkolsskrift = koloverskift[0:4]
            print(sjkolsskrift, "Innhold kol sjoverskrift Gunnar")
            if sjkolsskrift == 'Odds':
                for tr in  soup.find_all('tr')[0:-1]:
                    tds =  tr.find_all('td')
                    antkol = len(tds)
                    print(antkol,"antall kolonner Gunnar nar vi har Odds data")
#             lopnr = 0 
                    if antkol == 4:
                        print(tds,"antall kolonner 4")  
                        innvinnerodds = tds[0].text.strip()
                        innplassodds = tds[1].text.strip()
                        inntvillingodds=tds[2].text.strip()                    
                        inntrippellodds=tds[3].text.strip()
                        print(innvinnerodds,"antall kolonner og vinner odds?")
                        sjvinnerodds = innvinnerodds[0:2]
                        print(sjvinnerodds,"Har vi vinnerodds V: ?")
                        if sjvinnerodds == "V:":
                            vinnerodds = innvinnerodds
                            vodds = vinnerodds.count(",")
                            vodds = 1
                            print(vodds,"vodds teller har verdi")        
                            teller = teller + 1
                            if vodds == 1:
                                lopnr = lopnr +1
                                voddlen =len(vinnerodds)
                                print(voddlen,"Vinner odds lengde")
                                print(vinnerodds,"Vinner odds innhold")
                                utvinnerodds = vinnerodds[4:voddlen]
                                lenplassodds = len(innplassodds)
                                utplassodds  = innplassodds[4:lenplassodds]
                                lentvillingodds = len(inntvillingodds)
                                uttvillingodds=inntvillingodds[4:lentvillingodds]
                                lentrippelodds = len(inntrippellodds)
                                uttrippellodds=inntrippellodds[4:lentrippelodds]
                                g.write("%s;%s;%s;%s;%s;%s;%s" % \
                               (lopnr, utbanenavn, webdato, utvinnerodds, utplassodds, uttvillingodds, uttrippellodds))
                                g.write('\n')
#     print(datobanenavn,"Datobanenavn")
#     banenavn = " "
    return
#Gunnar(FunkWebodds)