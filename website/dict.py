from calendar import c
from cgi import print_exception
from cgitb import html
from itertools import combinations_with_replacement
from operator import attrgetter
from os import remove
from xml.dom.minidom import Attr
from flask import render_template
import re
from bs4 import BeautifulSoup
import requests
import time 
from datetime import datetime, timedelta
from threading import Timer


url = f"https://coinmarketcap.com/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

tbody = doc.tbody
trs = tbody.contents
#RAW DICTS  
crypto_coins = {}
ex_crypto = {}

#FIRST 10 COIN NAMES AND PRICES
for tr in trs[:10]: #only first 10 rows, rest are not under p tag thats why they dont show
    name, price = tr.contents[2:4]
    names = name.p.string
    prices = price.a.string
    crypto_coins[names] = prices


#REST OF NAMES AND PRICES 
for tr in trs[10:]:
    name_ext, price_ext = tr.contents[2:4]
    name_ex = name_ext.span.next.string 
    price_ex = str(price_ext.span).split("<")[-2].split(">")[1]
    ex_crypto[name_ex] = price_ex
    
for key in ex_crypto:
    ex_crypto[key] = '$' + ex_crypto[key]
    
    
def Merge(crypto_coins, ex_crypto):
    res = crypto_coins | ex_crypto
    return res

coin_dict = Merge(crypto_coins, ex_crypto)











