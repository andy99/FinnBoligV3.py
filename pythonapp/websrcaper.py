from bs4 import BeautifulSoup
import requests
#from builder._html5lib import Element
#coding: utf-8
#from idlelib.replace import replace
#r = requests.get("http://sportsearch.rikstoto.no/pages/hest_info.aspx?sokid=30095680" )
#Henter informasjon om super talisman sokid=30095680
class Element(object):
    def __init__(self, row, col, text, rowspan=1, colspan=1):
        self.row = row
        self.col = col
        self.text = text
        self.rowspan = rowspan
        self.colspan = colspan

    def __repr__(self):
        return f'''{{"row": {self.row}, "col":  {self.col}, "text": {self.text}, "rowspan": {self.rowspan}, "colspan": {self.colspan}}'''

    def isRowspan(self):
        return self.rowspan > 1

    def isColspan(self):
        return self.colspan > 1


r = requests.get("http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=30095680")
doc = BeautifulSoup(r.content,"html.parser")

#Henter alle datarader
trs = doc.select('tr')

#print (trs,"skriver datarader")
#sjekker antall rader
antrader =len(trs)
#print(antrader,"Antall rader")

#Henter rad for rad
m = []
with open('ResulttatHest0.txt', 'a') as f:
    for rad, tr in enumerate(trs):
        it = []
        ts =tr.find_all('td')
#         print(ts,"Skriver ts ")
        for kol, tx in enumerate(ts):
            print(rad,"Dette er raden")
            print(kol,"Dette er kol")
            felt = Element(rad, kol, tx.text.strip())
            print(felt.text,"Innhold felt")
            it.append(felt)
            #print(it,"Innhold it")
            m.append(it)
#     print(m,"Innhold en rad")
    f.write("%s" % \
    m)
                 



