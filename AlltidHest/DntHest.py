from bs4 import BeautifulSoup
import requests
# f = open("D:\workplace_python\TravAnalyse\Galoppprosentmangleridnr.txt", "r")
# print(f.read()) 
# inndata = f.read()
#r = requests.get("http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?search=Firstneverfollows" )
f = open("D:\workplace_python\TravAnalyse\Galoppprosentmangleridnr.txt", "r")
for x in f:
    print(x) 
    innnavn = x
    lengdenavn = len(innnavn)
#     print(lengdenavn,"Lengde hestenavn")
    hestenavn=x[5:lengdenavn-1]
    print(hestenavn,"Hestenavn for oppslag")
    r = requests.get("http://www.travsport.no/Andre-elementer/Sok-etter-hestkusklop/Sok-etter-hest/?search=" + hestenavn )
    r.content
    soup = BeautifulSoup(r.content,"html.parser")
    myspan = soup.find("span", {"class": "infoLinje"})
    myspan2 = soup.find_all("title")
    myspan3=soup.select("span")
    myspan4=soup.find("span", id="ctl00_MainRegion_horseInfo_lblInfo")
    test5 = myspan3[1].text.strip()
    regnr = test5[0:15]
    test = myspan
# test1=test.find('578001020165462')
# print(StartHestregnr,"startpunkt hest regnr")
    print(test5,"Test5 ")
#     x = myspan.get("id")
#     y = test.get("class")
#     print(x,"skriver x ")
#     print(y,"skriver y ")
# print(len(test)) 
  
    with open('DntHestRegnr.txt', 'a') as f:
        print("Skiver fil")
        f.write("%s;%s" % \
        ( regnr,hestenavn))
        f.write('\n')
