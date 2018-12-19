from bs4 import BeautifulSoup
#import bs4 as bs
import requests
#r = requests.get('http://sportsearch.rikstoto.no/pages/hest_info.aspx?+ hesteid')
url = ("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=30095680" )
r =requests.get(url)
html_content = r.text
# r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=30095680" )
#http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=30095680 
#soup = BeautifulSoup
#table = r.text
soup = BeautifulSoup(r.text,"html.parser")

for tr in soup.find_all('tr')[0:-1]:
    print(tr,"innhold tr")
    tds = tr.find_all('td') 
    print(tds,"Innhold tds")
    

