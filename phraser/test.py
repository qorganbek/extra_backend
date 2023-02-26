import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.nur.kz/society/')
html = BS(r.content, 'html.parser')
url = html.select('.block-infinite__item-content > a')[0].attrs['href']

print(url)


# for el in html.select('.block-infinite__item-content'):
#     title = el.select('.article-preview-mixed__content > h3')
#     date = el.select('a')[0].text
#     url = el.select('a')[0].attrs['href']
#     print(url)