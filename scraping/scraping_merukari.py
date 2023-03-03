from bs4 import BeautifulSoup as bs
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER = "/Users/kyota/git_repository/googlechrome.dmg"


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = Service(executable_path=CHROMEDRIVER)
    driver = webdriver.Chrome(options=options)
    return driver


def get_source_from_page(driver, page):
    try:
        driver.get(page)
        driver.implicitly_wait(10)
        page_source = driver.page_source
        return page_source

    except Exception as e:
        print("Exception\n" + traceback.format_exc())
        return None


def get_data_from_source(src):
    soup = bs(src, features='lxml')
    print(soup)
    try:
        info = []
        elems = soup.findAll(class_="mer-list-item")
        print(elems)
        for elem in elems:
            a_tag = elem.find("a")

            if a_tag:
                href = a_tag.attrs['href']
                category_id = href.replace("/jp/category/", "")
                info.append(category_id)

        return info
    except Exception as e:
        print("Exception\n" + traceback.format_exc())
        return None



