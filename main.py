import pandas as pd
import requests
import bs4 as BeautifulSoup

url="https://www.flipkart.com/search?q=shoes+under+500&sid=osp%2Ccil&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=shoes+under+500%7CMen%27s+Footwear&requestId=e5665efe-6ab5-4ccd-9438-288fe51cd25b&as-backfill=on&page=2"
r=(requests.get(url))
print(r)
soup=BeautifulSoup(r.text,"lxml")
print(soup)