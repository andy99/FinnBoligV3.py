from bs4 import BeautifulSoup
import requests
id_nr = '885'
# Hestsok = requests.get("http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=30104845")
# Hestsok = requests.get('http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=' + '30104844')
#id_nr =  30133760
id_nr =  30139753
teller = 0
while id_nr < 30139959:
    id_nrtxt = str(id_nr)
    Hestsok = requests.get('http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?id=116&sokId=' + id_nrtxt)
    Hestsok.content
    soup = BeautifulSoup(Hestsok.content,"html.parser")
    Hestenavn = soup.find('span', class_="infoHeader")
    print(Hestenavn,"Hestenavn er ?") 
    teller = teller + 1
    id_nr = id_nr + 1
    if teller > 100:
        print(id_nr,"Idnr int har verdien")
        teller = 0
        
    with open('DNTHestidnr.txt', 'a') as f:
        f.write("%s,%s" % \
            (id_nrtxt,Hestenavn.text.strip()))
        f.write('\n')
