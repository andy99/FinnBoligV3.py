from bs4 import BeautifulSoup
import requests
#r = requests.get('http://sportsearch.rikstoto.no/pages/hest_info.aspx?+ hesteid')
r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=30095680" )
#http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=30095680 
#soup = BeautifulSoup
#table = r.text
soup = BeautifulSoup(r.content,"html.parser")
Hestedata = soup.find_all('table', class_="fixedTable")
anttabeller = len(Hestedata)
print(anttabeller,"Antall tabeller")

#Hestdata[1] inneholder de data vi skal ha
print(Hestedata[0],"Innhold Hestedata 0")
Hestinfo = []
Hestinfo = Hestedata[0]

for tr in soup.find_all('tr')[0:]:
            tds = tr.find_all('span')
#             print("tds")

for tr in soup.find_all('tr')[0:]:
            span = tr.find_all('span')
            print(span,"Innhold span")

#Finner Hestenavn
Hestenavn = soup.find('span',class_ ="infoHeader")
Hesteinfo = soup.find('span',class_= "infoLinje")
Hestenavn = Hestenavn.text
print(Hestenavn,"Innhold heste navn")
print(Hesteinfo.text,"Innhold heste navn")
#     