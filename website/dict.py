from flask import render_template
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# RAW DICTS
crypto_coins = {}
ex_crypto = {}

# FIRST 10 COIN NAMES AND PRICES
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    names = name.p.string
    prices = price.a.string
    crypto_coins[names] = prices

# REST OF NAMES AND PRICES 
for tr in trs[10:]:
    name_ext, price_ext = tr.contents[2:4]

    # Check if span exists in price_ext
    if price_ext.span:
        # Extract the price if the span exists
        name_ex = name_ext.span.next.string 
        price_ex = str(price_ext.span).split("<")[-2].split(">")[1]
    else:
        # Handle the case where span does not exist
        name_ex = "N/A"
        price_ex = "N/A"

    ex_crypto[name_ex] = price_ex

for key in ex_crypto:
    ex_crypto[key] = '$' + ex_crypto[key]

def merge(crypto_coins, ex_crypto):
    res = crypto_coins | ex_crypto
    return res

coin_dict = merge(crypto_coins, ex_crypto)

# Rest of your code...
