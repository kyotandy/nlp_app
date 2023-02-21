import pandas
import requests
from bs4 import BeautifulSoup as bs
import re
from fake_useragent import UserAgent


ua = UserAgent()
useragent = ua.random


def get_html(url):
    headers = {"User-Agent": useragent}
    res = requests.get(url, headers=headers)
    return res


url = "https://auctions.yahoo.co.jp/search/search?p=pt+デニム&va=pt+デニム&exflg=1&b=1&n=100"

res = get_html(url)

soup = bs(res.content, "html.parser")

items = soup.findAll(class_="Product")

url_list = [item.find(class_="Product__titleLink").get("href") for item in items]

print(url_list)
