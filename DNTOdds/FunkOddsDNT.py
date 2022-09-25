from bs4 import BeautifulSoup

coding = 'utf-8'
import requests

# Dette programmet kalles av  HovedProgramOdds.py
# Filen DNTodds.txt legges i mappen DNT odds
# !/usr/bin/python
print("FunkoddsDNT")
webdato = '20200309'


def FunkOddsDNT(webdato):
    print( webdato, " Webdato har verdienEr i program FunkoddsDNT")
   # Lastedato = '20210523'
    Lastedato = webdato
    Utdatoodds = Lastedato
    print(Lastedato, "lastedato har verdien")

    #     r = requests.get("http://www.travsport.no/Sport/Resultater/Biri-Travbane/?date=" + Lastedato)
    s = requests.get("http://www.travsport.no/Sport/Resultater/Sorlandets-travpark/?date=" + Lastedato)
    minipaddreese = requests.get("https://api.ipify.org").text
    print(minipaddreese)
    s.content
    soup = BeautifulSoup(s.content, "html.parser")
    # print(soup.text, "Innhold Soup")
    banenavn = soup.find('div', id="article")
    utbanenavn = banenavn.text.strip()
    print(utbanenavn)
    tables = soup.findChildren('table')
    lopnr = 0

    tabeller = soup.findChildren('table')
    lengdetabeller = len(tabeller)
    print(lengdetabeller, "tabell lengde er")
    tabell1 = tabeller[1]
    rader = tabell1.findChildren('tr')

    lop = 0
    tellerverdi = 0
    teller = 0
    listemedverdier = []
    antallrader = len(rader)
    print(antallrader, "antall rader")
    for rad in rader:
        celler = rad.findChildren('td')
        for cell in celler:
            verdi = cell.string
            # print(verdi, "Innhold Verdi")
            if verdi is not None:
                tellerverdi == 0
                antallverdi = len(verdi)
                if verdi[0:2] in ('P:', 'V:', 'T:', 'D:') or verdi[0:3] == 'TV:':
                  verdilengde = len(verdi)
                  if len(verdi) > 2:
                      teller = teller + 1
                      listemedverdier.append(verdi)
                      verdi = []

    #print(listemedverdier)

    lenlisteverdier = len(listemedverdier)
    #print(lenlisteverdier, "Lengde liste verdier")
    tabellinhold= listemedverdier
    #print(tabellinhold, "innhold tabell ")
    antall_lop = int(lenlisteverdier/32)
    print(antall_lop, "Antall record")
    with open('D:\workplace_python\DNTOdds\DNTodds.txt', 'a') as g:
        y = 0  # vinner odds
        z = 1  # Plass odds
        a = 2  # Tvilling odds
        b = 3  # trippel odds
        c = 4  # vinner omsetning
        d = 5  # plass omsetning
        e = 6  # tvilling omsetning
        f = 7  # trippel omsetning
        for x in range(0, antall_lop):
            vodds = tabellinhold[y]
            voddlen = len(vodds)
            voddsut = vodds[4:voddlen]
            if "/" in voddsut:
                print("Vi har dodt lop og må fjerne en")
                voddsut1 = voddsut.split("/")
                print(voddsut[0], "Vi har fjernet /  hvilken verdi har vi nå i vinnerodds  ")
                voddsut= voddsut1
            y = y + 8
            #
            plassodds = tabellinhold[z]
            plasslen = len(plassodds)
            plassoddsut = plassodds[4:plasslen]
            z = z + 8
            #           Tvilling odds
            # print(tabellinhold[a])
            tvillingodds = tabellinhold[a]
            tvillingoddslen = len(tvillingodds)
            tvillingoddsut = tvillingodds[4:tvillingoddslen]
            a = a + 8
            # Trippel odds
            trippelodds = tabellinhold[b]
            trippeloddslen = len(trippelodds)
            trippeloddsut = trippelodds[4:trippeloddslen]
            if "/" in trippeloddsut:
                print("Vi har dodt lop og må fjerne en")
                trippeloddsut1 = trippelodds.split("/")
                print(trippeloddsut1[1], "Vi har fjernet /  hvilken verdi har vi nå trippelodds  ")
                trippeloddsut = trippeloddsut1[1]
            b = b + 8
            # Vinner Omsetning
            vomsetning = tabellinhold[c]
            vomsetninglen = len(vomsetning)
            vomsetningut = vomsetning[4:vomsetninglen]
            c = c + 8
            # Plass Omsetning
            pomsetning = tabellinhold[d]
            pomsetninglen = len(pomsetning)
            pomsetningut = pomsetning[4:pomsetninglen]
            d = d + 8
            # Tvilling Omsetning
            tvomsetning = tabellinhold[e]
            tvomsetninglen = len(tvomsetning)
            tvomsetningut = tvomsetning[4:tvomsetninglen]
            e = e + 8
            # Trippel Omsetning
            tromsetning = tabellinhold[f]
            tromsetninglen = len(tromsetning)
            tromsetningut = tromsetning[4:tromsetninglen]
            f = f + 8

            lopnr = lopnr + 1
            g.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
                    (utbanenavn, lopnr, Utdatoodds, voddsut, vomsetningut, plassoddsut, pomsetningut, tvillingoddsut,
                     tvomsetningut, trippeloddsut, tromsetningut))
            g.write('\n')
            x = x + 1
    return


#webdato = '20220121'
#FunkOddsDNT(webdato)


#def vinnerodds(verdi):
#    verdivinner = verdi
