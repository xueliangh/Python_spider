import requests
from bs4 import BeautifulSoup

def getWiki(term):
    res = requests.get('https://zh.wikipedia.org/wiki/{}'.format(term))
    soup = BeautifulSoup(res.text, 'lxml')
    article = soup.select_one('.mw-parser-output p').text
    print(article)

print(getWiki("search text"))


