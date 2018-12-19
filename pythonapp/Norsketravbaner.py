from bs4 import BeautifulSoup
import requests
r = requests.get("http://www.travsport.no/Sport/Norske-baner/")
soup = BeautifulSoup(r.content,"html.parser")

for i in soup.find_all('a'):
    with open('Norsketravbaner.txt', 'a') as f:
            f.write("%s;" % \
                ( i.text))
            f.write('\n')     
    print( "Found the URL:", i.text)
#tabell = soup.find("div class="mainBody")

# for b in soup.find_all("div",{"class": "mainbody"}):
#     with open('Norsketravbaner.txt', 'a') as f:
#             f.write("%s;" % \
#                 ( i.text))
#             f.write('\n')     
#     print("hva er verdien av B",b)
# travbaner = []
# travbaner = soup.findALL("div", {"class": "mainBody"})
# print(travbaner)
# print(soup.get_text())
# Travbane = soup.find(True, class= "ctl00_MainRegion_horseInfo_lblNavn")
# for i in travbaner[-1]:
#     print(travbaner)
# with open('Norsketravbaner.txt', 'a') as f:
#             f.write("%s;" % \
#                 ( i.text))
#             f.write('\n')     
#              