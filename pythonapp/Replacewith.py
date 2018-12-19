from bs4 import BeautifulSoup
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
#markup = '</td><td align="center" nowrap="nowrap">&nbsp;'
soup = BeautifulSoup(markup,"html.parser")
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "Gunnar.net"
a_tag.i.replace_with(new_tag)

a_tag
print(a_tag)
# <a href="http://example.com/">I linked to <b>example.net</b></a>