from bs4 import BeautifulSoup
import requests
num = 418
while num < 421:
#     num = 9
    print(num)
    r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    
    with open('AlltidHest.txt', 'a') as f:
        for tr in soup.find_all('tr')[2:]:
            tds = tr.find_all('td')
            f.write("Regnr: %s, Navn: %s, Regnr: %s, Alder :%s, Kjonn:%s, Farge: %s, Land: %s" % \
                ( tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(),tds[7].text.strip()))
            f.write('\n')     
                