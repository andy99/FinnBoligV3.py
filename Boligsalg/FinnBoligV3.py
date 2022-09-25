from bs4 import BeautifulSoup
import requests



r = requests.get("https://www.finn.no/realestate/homes/search.html?filters=&is_new_property=false&location=0.20061")
r.content
soup = BeautifulSoup(r.content, "html.parser")
#print(soup, "InnHold Soup")

with open('FinnBolig.txt', 'a') as g:
    Address_divs = soup.findAll("div", {"class": "text-14 text-gray-500"})
    print(Address_divs, "Innhold adresse div")
    print(len(Address_divs), "Lengde Adresse")
    Price_divs = soup.findAll("div", {"class": "ads__unit__content__keys"})

   # if not len(Address_divs) == len(Price_divs):
   #     print("Address_divs has not the same length as Price_divs: ERROR ")

    for i in range(len(Address_divs)):
        print(Address_divs[i].text)

        
        # if total_pris == "Sol":
        #     continue
        # if (74364 * float(int(kvadrat_meter))) > float(int(total_pris)):
        #     g.write("%s;%s;%s;%s;%s" % \
        #             (Address_divs[i].text, kvadrat_meter, total_pris, (74364 * int(kvadrat_meter)), ((74364 * int(kvadrat_meter)) - int(total_pris))))
        #     g.write('\n')







                