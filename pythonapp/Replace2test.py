from nt import write

print('Hello what er som foregar')
x = 4 
if x < 6: 
    print(x,x*x*x) 
    
Hestenum = 123599
hesteid = 'Sokid='+ Hestenum.__str__()

print(hesteid,"Hesteid er")
from bs4 import BeautifulSoup
import requests
#r = requests.get('http://sportsearch.rikstoto.no/pages/hest_info.aspx?+ hesteid')
#r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=123599" )
r = requests.get("http://www.travsport.no/Sport/Startlister/Bjerke-Travbane/?date=20180110")

r.content
#print(r.content)
soup = BeautifulSoup(r.content,"html.parser")
print(r.content)
#Hesttabell = soup.find_all('table',class_ = 'dg')
Hesttabell = soup.find_all('table')
antalltabeller = len(Hesttabell)
print(antalltabeller,"Antall tabeller")

tabelltype =type(Hesttabell)
Hesttabell = Hesttabell[0]
print(tabelltype,"Tabell type")
with open("Hestedata2.txt","w") as r:
     for row in Hesttabell.find_all('tr'):
         for cell in row.find_all('td'):
             r.write(cell.text.ljust(22,';'))
             r.write('\n')    
        