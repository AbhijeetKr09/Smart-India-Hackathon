# imports
import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
description=[]
reviews=[]
for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobiles+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+5g%7CMobiles&requestId=958ab9f1-2f35-4bd8-94e1-4065b1139a89&as-backfill=on&page="+str(i)
    r=requests.get(url)
    # print(r)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")
    for i in names:
        name=i.text
        Product_name.append(name)
    # print(Product_name)
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices:
        name=i.text
        Prices.append(name)
    # print(len(Prices))
    # np=soup.find("a",class_="_1LKTO3").get("href")
    # print(np)
    # print(url)

df=pd.DataFrame({"product name":Product_name,"Prices":Prices})
# print(df)

df.to_csv("flipkart_mobies.csv")
