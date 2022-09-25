from bs4 import BeautifulSoup
import requests
from time import sleep
# import lxml.html
print("Hallo hvem der")
r = requests.get("https://no.unibet.com/betting/sports/filter/trotting").text
# print(r,"Innhold r").encode("utf-8")
# soup = BeautifulSoup(requests.get("https://no.unibet.com/betting/sports/filter/trotting").text)
# r.content
# print("Sjekker status")
# if r.status_code == 200:
#     print('Success!')
# elif r.status_code == 404:
#     print('Not Found.')
# overskrift =r.headers
# overskifttype = r.headers['Content-Type']
# print(r,"innhold r")
# print(overskifttype ,"innhold r")
soup = BeautifulSoup(r,"lxml").encode("utf-8")
print("Hallo")
sleep(5)
print(soup.prettyfi(),"Innhold soup")
# print(soup,"Innhold Soup")