from bs4 import BeautifulSoup
import requests
num = 0
while num < 521:
    
#     num = 9
    print(num)
    r = requests.get("http://www.alltidhest.org/Horses/Page/{}".format(num) )
    num = num + 1
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    
    with open('AlltidHestTest2.txt', 'a') as f:
        for tr in soup.find_all('tr')[2:]:
            tds = tr.find_all('td')
            f.write("%s,%s,%s,%s,%s,%s,%s" % \
                ( tds[1].text.strip(), tds[2].text.strip(), tds[3].text.strip(), tds[4].text.strip(), tds[5].text.strip(), tds[6].text.strip(),tds[7].text.strip()))
            f.write('\n')     
                
                