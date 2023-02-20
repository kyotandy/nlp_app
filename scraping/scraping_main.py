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

