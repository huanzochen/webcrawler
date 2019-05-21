# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:42:11 2019

@author: huang
"""
import os
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
s = requests.Session()
res = s.get('https://www.buy123.com.tw/')
soup = BeautifulSoup(res.text, 'html.parser')
"""print(soup.prettify())"""

print('======================')
print(soup.find_all('a'))