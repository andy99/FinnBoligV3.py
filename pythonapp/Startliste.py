from bs4 import BeautifulSoup
import requests
num = 4280
while num == 4280:
#     num = 9
    print(num)         
    #r = requests.get("http://www.alltidhest.org/Drivers/Page/{}".format(num) )
    #r = requests.get("http://www.alltidhest.org/RaceInfo/Details/{}".format(num) )
    r = requests.get("http://www.alltidhest.org/RaceInfo/Details/4280/")
    #                  http://www.alltidhest.org/RaceInfo/Details/4280
    #print(r,"Innhold i r")
    num = num + 1
    r.content
    #print(r,"innhold r content")
    soup = BeautifulSoup(r.content,"html.parser")
    #print(soup,"Innhold soup")
    with open('AlltidStartlisteTest0.txt', 'a') as f:
        for tr in soup.find_all('tr')[0:]:
            #print  data.has_key("rowspan")
            tds = tr.find_all('td')
            #print(tds[2].text,"Innhold tds")
            f.write("%s" % \
                ( tds[0].text.strip()))
            f.write('\n')