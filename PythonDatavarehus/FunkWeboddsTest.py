from bs4 import BeautifulSoup
coding='utf-8'
import requests
# Dette programmet kalles av  DNTResultatdatoerBjerke.py
# Filen DNTodds.txt legges i mappen pythonapp
#!/usr/bin/python
def FunkWeboddsTest(webdato):
    #     Lastedato = '20200309'  For Testing
    Lastedato = webdato   
    Utdatoodds = Lastedato
      
#     r = requests.get("http://www.travsport.no/Sport/Resultater/Biri-Travbane/?date=" + Lastedato)
    s = requests.get("http://www.travsport.no/Sport/Resultater/Jarlsberg-travbane/?date=" + Lastedato)
    s.content
    soup = BeautifulSoup(s.content,"html.parser")
#     print(soup.text,"Innhold Soup")
#     datobanenavn = soup.find('div' , class_ ="article")
#     print(datobanenavn, "Innhold dato banenavn")
#     txtalign = soup.find_all('td' , class_ ="textalign")
    banenavn =  soup.find('div', id="article")
    utbanenavn = banenavn.text.strip()
    lopnr = 0
    tables = soup.findChildren('table')
    table = tables[1]
    CAArray = []
    teller=0
    rows = table.findChildren('tr')
#     with open('DNTodds.txt', 'a') as f:
    for row in rows:
        cells = row.findChildren('td') # has all of the table's elements
        elements = []
        for cell in cells:
            value = cell.string
            if value is not None:
    #                     print(value[0:2],"innhold Value 0 til 1 etter if test none")
                if value[0:2] in ('P:','V:','T:', 'D:') or value[0:3] == 'TV:':
                    elements.append(value)
                    teller = teller + 1
    #                         print(teller,"innhold Teller")
                    print(elements,"elements etter append Gunnar")
    #   antall lop er det samme som element/2
                    elementlen = len(elements)
                    antallelementer = elementlen
#                     print(elementlen,"element lengde")
    #                         break
                if len(elements) > 2:
                    teller = teller + 1
                    for innhold in elements:
    #                             print(innhold,"Innhold test Gunnar")
#                         kParsed = str(elements[0])
#                         NParsed = str(elements[1])
    #                             print(teller,"Max antall elementer Gunnar")
    #                             print(elements,"innhold elementer Gunnar har alle data som skal skrives")
                        CAArray.append(elements)
                           
#     print(elements,"Innhold elements")
    tabellinhold = (CAArray[0])
    print(tabellinhold,"Innhold tabell")
    lentab = len(tabellinhold )
    print(lentab,"tabellinhold ")
    antrecords = lentab/8
    antall_lop = int(antrecords)
    print(antall_lop,"Antall lop Gunnar")
    with open('DNTodds.txt', 'a') as g:
        y=0   #vinner odds
        z = 1 #Plass odds
        a = 2 #Tvilling odds
        b = 3 #trippel odds
        c = 4 # vinner omsetning
        d = 5 # plass omsetning
        e = 6 # tvilling omsetning
        f = 7 # trippel omsetning   
        for x in range(0,antall_lop):    
            print(x,"x er det samme som antall lop")
            print(tabellinhold[y])
            vodds = tabellinhold[y]
            voddlen =len( vodds)
            voddsut = vodds[4:voddlen]
            y = y + 8
#            
            print(z,"z har verdien")
            print(tabellinhold[z])
            plassodds = tabellinhold[z]
            plasslen =len(plassodds)
            plassoddsut = plassodds[4:plasslen]
            z = z + 8 
#           Tvilling odds
            print(tabellinhold[a])
            tvillingodds = tabellinhold[a]
            tvillingoddslen =len(tvillingodds)
            tvillingoddsut =  tvillingodds[4:tvillingoddslen] 
            a = a + 8
            #Trippel odds
            print(tabellinhold[b])
            trippelodds = tabellinhold[b]
            trippeloddslen =len(trippelodds)
            trippeloddsut =  trippelodds[4:trippeloddslen] 
            b = b + 8
            #Vinner Omsetning
            print(tabellinhold[c])
            vomsetning = tabellinhold[c]
            vomsetninglen =len(vomsetning)
            vomsetningut =  vomsetning[4:vomsetninglen] 
            c = c + 8
            #Plass Omsetning
            print(tabellinhold[d])
            pomsetning = tabellinhold[d]
            pomsetninglen =len(pomsetning)
            pomsetningut =  pomsetning[4:pomsetninglen] 
            d = d + 8
            #Tvilling Omsetning
            print(tabellinhold[e])
            tvomsetning = tabellinhold[e]
            tvomsetninglen =len(tvomsetning)
            tvomsetningut =  tvomsetning[4:tvomsetninglen] 
            e = e + 8
            #Trippel Omsetning
            print(tabellinhold[f])
            tromsetning = tabellinhold[f]
            tromsetninglen =len(tromsetning)
            tromsetningut =  tromsetning[4:tromsetninglen] 
            f = f + 8
            
            lopnr = lopnr + 1
            g.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % \
            (utbanenavn,lopnr,Utdatoodds,voddsut, vomsetningut,plassoddsut,pomsetningut,tvillingoddsut,tvomsetningut, trippeloddsut,tromsetningut ))
            g.write('\n')
            x = x + 1
        

    return
