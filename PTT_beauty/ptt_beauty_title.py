# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:57:19 2018

@author: simon
"""
import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.ptt.cc/bbs/Beauty/index.html')
soup = BeautifulSoup(res.text,'html.parser')
tag_name = 'div.title a'
articles = soup.select(tag_name)
for art in articles:
    print(art.text)
    print(art['href'])
    
