from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://no.unibet.com/betting/sports/filter/trotting"
print("a")
driver = webdriver.Chrome('C:/Users/XNikolai-360NoscopeX/Downloads/chromedriver_win32/chromedriver.exe')
print("b")
driver.get(url)
print("c")
soup = BeautifulSoup(driver.page_source, 'html.parser')
print("d")
containers = soup.findAll("table")
print(soup)
print()
print(containers)