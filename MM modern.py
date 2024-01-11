import bs4
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

baseURL = 'https://megamarket.ru'
# target = input('Ввести искомый товар')
# target = 'sun-m27bg130'
target = 'rtx 3060'
targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')

def get_source_html(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get(url=url)
        WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.TAG_NAME, "html")))
        with open('source-page-mm.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def get_items(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', 'catalog-item-desktop')

    df = pd.DataFrame({'наименование': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Купон': [], 'Стоимость с плюшками': []})

    def cupon(price):
        if 11000 < price < 30000:
            cupon1 = 2000
        elif 30000 < price < 50000:
            cupon1 = 5000
        elif 50000 < price < 75000:
            cupon1 = 9000
        elif price > 75000:
            cupon1 = 12000
        else: cupon1 = 0
        return cupon1
    df = pd.DataFrame({'наименование': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Купон': [], 'Стоимость с плюшками': []})

    for item in items_divs:
        item_block = item.find('div', class_='item-block')
        item_price_block = item_block.find('div', class_='inner catalog-item__prices-container')
        item_money = item_price_block.find('div', class_='item-money')
        item_price = item_money.find('div', class_='item-price')
        item_price_result = item_price.find('span').get_text()

        item_bonus = item_money.find('div', class_='item-bonus')
        if isinstance(item_bonus, bs4.element.Tag):
            item_bonus_percent = item_bonus.find('span', class_='bonus-percent').get_text()
            item_bonus_amount = item_bonus.find('span', class_='bonus-amount').get_text()
        else:
            continue

        bonus_percent = int(item_bonus_percent.replace('%', ''))
        price = int(item_price_result[0:-1].replace(' ', ''))

        best_price = (price - cupon(price)) * (1 - bonus_percent / 100)
        df_item = pd.DataFrame({'наименование': [target], 'Полная цена': [price], 'Кэшбек': [item_bonus_amount], 'Процент Кэшбека': [item_bonus_percent],'Купон': [cupon(price)], 'Стоимость с плюшками': [best_price]})
        df = df._append(df_item)

    return print(df)
def main():
    get_source_html(url=targetURL)
    get_items(file_path='source-page-mm.html')


def main():
    # get_source_html(url=targetURL)
    get_items(file_path='source-page-mm.html')

if __name__ == '__main__':
    main()