from bs4 import BeautifulSoup
import requests

# !/usr/bin/python
coding = 'utf-8'


def FunkResultat():
    Lastedato = '20220417'
    # Lastedato = webdato
    Bane = 'Varig-Orkla-Arena'
    print(Bane, "Bane som det skal hentes resultat dato for auto")
    print(Lastedato, " Lastedato er i funksjon Leser reslutater Automatisk")
    r = requests.get('http://www.travsport.no/Sport/Resultater/{}'.format(Bane) + '/?date=' + Lastedato)
    r.content
    print(r, "innhold av  r i funkres")
    soup = BeautifulSoup(r.content, "html.parser")
    #     Hesttabell = soup.find_all('tbody')
    # print(Hesttabell[1],"hestetabell")
    #     antalltabeller = len(Hesttabell)
    #     datobanenavn = soup.find('div' , class_ ="article"
    # print(datobanenavn,"Datobanenavn")
    banenavn = " "
    for h2 in soup.find_all('h2')[1]:
        print(h2, "Innhold h2")
        banenavn = h2
        print(banenavn, "Innhold banenavn")
        # print(antalltabeller,"Antall tabeller")
        #     wkol = 0
        with open('D:\workplace_python\pythonapp\SjekkerResultater\DNTResulatListe.txt', 'a') as f:
            #         for tr in enumerate(Hesttabell[1]):
          teller = 0
          for tr in soup.find_all('tr')[2:]:
            print(tr, 'Skriver tr i tabell 1')
            tds = tr.find_all('td')
            #             antrader = len(tr)
            # print(antrader,"Antall rader")
            antkol = len(tds)
            print(antkol, "Antall kolloner")
            if antkol == 4:
                premisum = tds[0].text.strip()
                Distanse = tds[1].text.strip()
                Baneverdi = tds[2].text.strip()
                Startmetode = tds[3].text.strip()
                print(premisum, 'Her har vi premiesum')
                sjpremie = premisum[0:9]  # Total premiesum for lopet
                print(sjpremie, "sjpremie har verdi")
                if sjpremie == "Premiesum":
                    print(sjpremie, "Her har vi premisum")
                    tallpremiesum = premisum[10:]
                    print(tallpremiesum, "tall premiesum")
                print(Distanse, 'Her har vi Distanse')
                sjdistanse = Distanse[0:8]
                print(sjdistanse, "Sjdistanse har verdi")
                if sjdistanse == "Distanse":
                    lopdistanse = Distanse[9:]  # distanse i lopet finnes ogs� pr resultat

                    print(lopdistanse, "Distansen i lopet")
                print(Baneverdi, 'Her har vi Baneverdi')  # Denne brukes ikke
                print(Startmetode, 'Her har vi Startmedode')
                sjauto = Startmetode[0:11]
                print(sjauto, "Har vi startmeode?")
                if sjauto == "Startmetode":
                    utstartmetode = Startmetode[13:]
                    print(utstartmetode, "Startmetode til fil")

            #           wkol = 0
            plasingint = 0
            #             wkol = antkol
            lopnr = 0
            if antkol == 9:
                plassering = tds[0].text.strip()
                print(plassering, 'Plassering etter strip func')
                if plassering in (
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18',
                        '19'):
                    plasingint = int(plassering)
                if type(plasingint) == int:
                    print(plassering, 'Her har vi integer')
                else:
                    print(plassering, 'Not an integer or a floating point decimal!')

                print(tds[5], "Kmtid")
                kmtid = tds[5].text.strip()
                #                 sjgallop = kmtid
                sjgallop = kmtid.find('g')
                print(sjgallop, "Sjgallop har verdien")
                utgallop = "Ingen galopp "
                if sjgallop > 1:
                    utgallop = "galopp"
                    print(utgallop, "Her har vi galopp")
                if plasingint == 1:
                    lopnr = lopnr + 1
                    teller = teller + 1
                    print(teller, 'lop teller')  # Teller blir det samme som l�p nr

                f.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
                        (banenavn.strip(), tallpremiesum, lopdistanse, teller, utstartmetode, utgallop,
                         tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(),
                         tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(), tds[7].text.strip(),
                         tds[8].text.strip()))
                f.write('\n')

            else:
                # print(tds,"Antall kolonner  er ikke 9")
                lop = tr.find_all('caption')
#                 antlop = len(lop)
#    return
