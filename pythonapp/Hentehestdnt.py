from bs4 import BeautifulSoup
import requests
#from idlelib.replace import replace
r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=123599" )
#print('Hello Gunnar ')
r.content
#print(r.content,"Hello Gunnar")
soup = BeautifulSoup(r.content,"html.parser")
html_innhold = r.text
print(html_innhold)
Soup = BeautifulSoup(html_innhold,"html.parser")
for tr in soup.find_all('tr'):
    print(tr)
    for td in soup.find_all('td'):
         #td = [td[0] for td in tr]
         #print(td[0].text)
    