import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re

#目標頁面

res = requests.get('https://www.ptt.cc/bbs/Beauty/index2109.html')
soup = BeautifulSoup(res.text, 'lxml')

#使用迴圈進入到目標頁面中的每個主題頁面

for article in soup.select('.r-ent a'):
    url = 'https://www.ptt.cc' + article['href']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    
    #判斷網址中有沒有圖片，如果有就開始下載

    if len(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})) > 0:
        for index, img_url in enumerate(soup.findAll('a', {'href':re.compile('http:\/\/i\.imgur\.com\/.*')})):
            try:
                    #記得更改想要下載到的位置

                urlretrieve(img_url['href'], 'D:\{}_{}.jpg'.format(article.text, index))
            except:
                print('{} {}_{}.jpg 下載失敗!'.format(img_url['href'], article.text, index))