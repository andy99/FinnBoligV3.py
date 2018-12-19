from bs4 import BeautifulSoup
import requests
import urllib
from basic import soup
from test.pystone import Record

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata
soup = make_soup("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=123599")
#print("Hellai gunnar")
hestedata =""
hestedatalagret = ""
data = []
tabell = soup.find('table')
Record = tabell.find_all('tr')
print(Record,"Record Hurra")
data = Record.find_all('td')
print(data,"Data Hurra")
hestedata = hestedata + "," + data.text + "Ny linje"
hestedatalagret = hestedatalagret + "\n" + hestedata[1:]
#print(hestedatalagret) 
print(hestedatalagret.text,"Skriver ut hestedatalagret ")