from scraping_merukari import *


if __name__ == "__main__":
    page = "https://www.mercari.com/jp/category"

    driver = get_driver()

    source = get_source_from_page(driver, page)

    info = get_data_from_source(source)

