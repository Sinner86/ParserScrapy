import bs4
from bs4 import BeautifulSoup
<<<<<<< HEAD

=======
>>>>>>> origin/master
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
<<<<<<< HEAD

from webdriver_manager.chrome import ChromeDriverManager

=======
from webdriver_manager.chrome import ChromeDriverManager
>>>>>>> origin/master
import pandas as pd

baseURL = 'https://megamarket.ru'
# target = input('Ввести искомый товар')
target = 'sun-m27bg130'
targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')

def get_items(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', 'catalog-item-desktop')

<<<<<<< HEAD
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
=======
    df = pd.DataFrame({'наименование': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Стоимость с плюшками': []})

>>>>>>> origin/master

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
<<<<<<< HEAD
        promo = 2000


        bonus = int(item_bonus_amount.replace(' ', ''))
        bonus_percent = int(item_bonus_percent.replace('%', ''))
        price = int(item_price_result[0:-1].replace(' ', ''))
=======
        df_item = pd.DataFrame()
        df.append(df_item)

        # bonus = int(item_bonus_amount.replace(' ', ''))
        # price = int(item_price_result[0:-1].replace(' ', ''))
>>>>>>> origin/master
        # k = price / bonus
        # item_url = item.find('a')
        #
        # link = baseURL + item_url.replace(' ', '%20')
        # items[k] = {'price': item_price_result[0:-2], 'bonus amount': item_bonus_amount,
        #             'bonus percent': item_bonus_percent, 'link': link}
<<<<<<< HEAD
        best_price = (price - promo) * (1 - bonus_percent / 100)
        df_item = pd.DataFrame([target, price, item_bonus_amount, item_bonus_percent, cupon(price), best_price])
        df.append(df_item)

    return df
def main():
    # get_source_html(url=targetURL)
    # get_items(file_path='source-page-mm.html')
    print(get_items(file_path='source-page-mm.html'))
=======


def main():
    # get_source_html(url=targetURL)
    get_items(file_path='source-page-mm.html')
>>>>>>> origin/master

if __name__ == '__main__':
    main()