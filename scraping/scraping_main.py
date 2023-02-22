from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas
import re
import requests
import time


ua = UserAgent()
useragent = ua.random


def get_html(url):
    headers = {"User-Agent": useragent}
    res = requests.get(url, headers=headers)
    return res


url = "https://auctions.yahoo.co.jp/search/search?p=pt+デニム&va=pt+デニム&exflg=1&b=1&n=100"
url_list = []

# get products' url in 5 pages
for _ in range(5):
    res = get_html(url)
    soup = bs(res.content, "html.parser")
    items = soup.findAll(class_="Product")
    url_list += [item.find(class_="Product__titleLink").get("href") for item in items]

    url = soup.find(class_="Pager__list Pager__list--next").find("a").get("href")
    time.sleep(5)
    print(url)
    print("*"*100)

print(len(url_list))
