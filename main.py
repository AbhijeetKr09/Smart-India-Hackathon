import pandas as pd
import requests
from bs4 import BeautifulSoup
# for i in range(2,10):
url="https://www.flipkart.com/search?q=shoes+under+500&sid=osp%2Ccil&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=shoes+under+500%7CMen%27s+Footwear&requestId=e5665efe-6ab5-4ccd-9438-288fe51cd25b&as-backfill=on&page="+str(i)
# r=(requests.get(url))
# print(r)
# soup=BeautifulSoup(r.text,"lxml")
# # print(soup)
# np=soup.find("a",class_="_1LKTO3").get("href")
# print(np)
print(url)