from bs4 import BeautifulSoup
import requests



r = requests.get("https://www.finn.no/realestate/homes/search.html?filters=&is_new_property=false&location=0.20061")
r.content
soup = BeautifulSoup(r.content,"html.parser")

with open('FinnBolig.txt', 'a') as g:
    Address_divs = soup.findAll("div", {"class": "ads__unit__content__details"})
    Price_divs = soup.findAll("div", {"class": "ads__unit__content__keys"})

    if not len(Address_divs) == len(Price_divs):
        print("Address_divs has not the same length as Price_divs: ERROR ")

    for i in range(len(Address_divs)):
        pos_m = Price_divs[i].text.find("m")
        kvadrat_meter = Price_divs[i].text[0:pos_m-1]
        if len(kvadrat_meter) > 5:
            kvadrat_meter = 1
        print(kvadrat_meter,"Kvadarat meter")
        total_pris = Price_divs[i].text[pos_m + 2: -2]
        total_pris = total_pris.replace(" ", "").replace(" ", "")
        
        
        if total_pris == "Sol":
            continue
        if (74364 * float(int(kvadrat_meter))) > float(int(total_pris)):
            g.write("%s;%s;%s;%s;%s" % \
                    (Address_divs[i].text, kvadrat_meter, total_pris, (74364 * int(kvadrat_meter)), ((74364 * int(kvadrat_meter)) - int(total_pris))))
            g.write('\n')







                