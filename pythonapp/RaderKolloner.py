from bs4 import BeautifulSoup
import requests
#!/usr/bin/python
# -*- coding: ascii -*-
import csv
from nt import replace
from _overlapped import NULL
from pip._vendor.pyparsing import empty
from itertools import count
from idlelib.rpc import response_queue
#from Replace2test import hestetabell
#-*- coding: UTF-8 -*-
#soup = BeautifulSoup
#r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=123599" )
r = requests.get("http://www.alltidhest.org/Horses/Page/1" )

html_innhold =r.text
soup = BeautifulSoup(r.content,"html.parser")
tabell = soup.find('table')
tabell_rader = tabell.find_all('tr')

for tr in tabell_rader:
    td = tr.find_all_next('td')
    rad = [i.text for i in td]
    #testtekst = rad
    print(rad,"Utskift RAD")
# print(testtekst,"Skriver test tekst")

#rad_tekst = soup.findAll('td')
rad_list = []
#rad_list = rad
# print(j,"Lengde j list antall rader i Html siden")
# print(i,"Lengde rad list antall rader i Html siden")
for i, value in enumerate(rad):
    #rad_list = rad_list.remove("Olav Mikkelborg")
    #print(i,rad_list,"Utskrift fra tabell")
    with open("Bravehunter.csv","w") as bravehunterfile:
         writer = csv.writer(bravehunterfile)
         writer.writerow(rad)
         bravehunterfile.close()
    
    
    
   
    
    
# with open("Bravehunter.csv","w") as bravehunterfile:
#      writer = csv.writer(bravehunterfile)
#      writer.writerow([rad_list[0],rad_list[1]])
#      bravehunterfile.close()
