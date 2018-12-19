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
    tabell = soup.find_all('table')[2]
    #print(tabell,"Innhold tabell")
    tmp = tabell.find_all('tr')
    
    first = tmp[0]
    allRows = tmp[0:-1]
    #print(allRows,"Innhold allrows")
    reslutat = [[data.get_text() for data in row.find_all('td')] for row in allRows]


    rowspan =[]
    for no, tr in enumerate(allRows):
        print(allRows,"Allrows i for loop")
        tmp = []
        for td_no, gunnar in enumerate(tr.find_all('td)')):
            print(td_no,"Innhold data i for loop")
            print (data.has_key("rowspan"))
            if data.has_key("rowspan"):
                print("Har rowspan HURRA")
                rowspan.append((no,td_no, int(data["rowspan"],data.get_text)))
                
    if rowspan:
        for i in rowspan:
            for j in range(1, i[2]):
                reslutat[i[0]+j.insert(i[1, i[3]])]
                print(reslutat,"Resultst etter rowspan")        
    #print(soup,"Innhold soup")
#     with open('AlltidStartlisteTest0.txt', 'a') as f:
#         for tr in soup.find_all('tr')[0:]:
#             #print  data.has_key("rowspan")
#             tds = tr.find_all('td')
#             #print(tds[2].text,"Innhold tds")
#             f.write("%s" % \
#                 ( tds[0].text.strip()))
#             f.write('\n')