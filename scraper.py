import requests
from bs4 import BeautifulSoup 


req_main = requests.get("https://www.ebay.com")

src_main = req_main.content

#print(src_main)

soup_main = BeautifulSoup(src_main,'lxml')

#print(soup_main)

link = soup_main.find('li', class_ = 'hl-cat-nav__js-tab')

hreff = link.find_all('a')
for x in hreff:
    print(x.attrs['href'])

for x in hreff:
    print(x.text)
