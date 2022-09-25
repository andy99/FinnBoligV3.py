from bs4 import BeautifulSoup
import requests 
r = requests.get("https://www.finn.no/realestate/homes/search.html?filters=&lifecycle=2")
r.content
soup = BeautifulSoup(r.content,"html.parser")
overskrift=soup.find_all("h2")[1].get_text()
print(overskrift,"Overskrift")
overskrift2=soup.find_all("h2")
print(overskrift2,"Overskrift2")
overskrift3=soup.find("h2").text
print(overskrift3,"Overskrift3")
# Starttabell = soup.find_all('table')
# print(Starttabell,"Lopsdato")
# for tr in  Starttabell.find_all('tr')[0]:
#             tds =  tr.find_all('td')
#             antkol = len(tds)
#             print(tr,"Innhold tr")