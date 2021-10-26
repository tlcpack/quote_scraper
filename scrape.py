import requests
from bs4 import BeautifulSoup

quotes = []

URL = "https://imsdb.com/scripts/Big-Lebowski,-The.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

record_el = soup('body')[0]
b_el = record_el.find_all('b')

# print(b_el[0].get_text().strip())

for b in b_el:
  if b.get_text().strip() == 'DUDE':
    line = str(b.next_sibling).strip()
    quotes.append(line)


print(quotes) 
