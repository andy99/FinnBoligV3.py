from bs4 import BeautifulSoup
import requests 
# import os
coding='utf8'
r = requests.get("https://www.rikstoto.no/Min-side/Mine-favoritthester/?page=5")
#                       http://www.travsport.no/Sport/Resultater/Forus-Travbane/ 

r.content
print(r,"innhold") 
soup = BeautifulSoup(r.content,"html.parser")
print(soup,"innhold soup")
# lopdato=soup.find_all("tbody")[1].get_text()
Hesttabell = soup.find_all('td')
antalltabeller = len(Hesttabell)
print(Hesttabell,"Lopsdato")
# for i in lopdato:
#     print(lopdato,"Lopsdato")
# print(lopdato,"Lopsdato")