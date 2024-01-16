import bs4
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

# функция сбора информации с сайта и записи в файл
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

# функция обработки собранной информации
def get_items(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    items_divs = soup.find_all('div', 'catalog-item-desktop')

    df = pd.DataFrame({'наименование': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Купон': [], 'Стоимость с плюшками': [], 'Ссылка': []})

    # функция определения купона по стоимости товара
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

    # перебор блоков с товарами
    for item in items_divs:
        item_block = item.find('div', class_='item-block')
        item_price_block = item_block.find('div', class_='inner catalog-item__prices-container')
        item_money = item_price_block.find('div', class_='item-money')
        item_price = item_money.find('div', class_='item-price')
        item_price_result = item_price.find('span').get_text()

        # извлечение наименования и ссылки на товар
        item_link = item_block.find('a', class_='ddl_product_link')
        name = item_link.get('title')
        link = 'https://megamarket.ru' + item_link.get('href')

        item_bonus = item_money.find('div', class_='item-bonus')
        if isinstance(item_bonus, bs4.element.Tag):
            item_bonus_percent = item_bonus.find('span', class_='bonus-percent').get_text()
            item_bonus_amount = item_bonus.find('span', class_='bonus-amount').get_text()
        else:
            continue
        # получение кэшбека в цифрах
        bonus_percent = int(item_bonus_percent.replace('%', ''))

        # получение цены в цифрах
        price = int(item_price_result[0:-1].replace(' ', ''))

        # расчет цены с учетом купона и кэшбека
        best_price = (price - cupon(price)) * (1 - bonus_percent / 100)

        # составление строки с данными и добавление к датафрейму
        df_item = pd.DataFrame({'наименование': [name], 'Полная цена': [price], 'Кэшбек': [item_bonus_amount], 'Процент Кэшбека': [item_bonus_percent],'Купон': [cupon(price)], 'Стоимость с плюшками': [best_price], 'Ссылка': [link]})
        df = df._append(df_item)

    return df.sort_values(by=['Стоимость с плюшками'])

# функция сбора информации с определенной страницы ММ
def get_items_page(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    # поиск блоков
    items_divs = soup.find_all('div', 'product-offer product-offer_with-payment-method')
    # подготовка пустого датафреймас именованными колонками
    df = pd.DataFrame({'наименование': [], 'Магазин': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Купон': [],
                       'Стоимость с плюшками': [], 'Ссылка': []})

    # функция определения купона по стоимости товара
    def cupon(price):
        if 11000 < price < 30000:
            cupon_finish = 2000
        elif 30000 < price < 50000:
            cupon_finish = 5000
        elif 50000 < price < 75000:
            cupon_finish = 9000
        elif price > 75000:
            cupon_finish = 12000
        else:
            cupon_finish = 0
        return cupon_finish

    # перебор блоков с товарами
    for item in items_divs:
        product_offer_price = item.find('div', class_='product-offer-price')

        # получение полной цены
        price = product_offer_price.find('span').get_text()
        price = int(price.replace(' ', ''))

        # получение наименования товар
        header = soup.find('h1', class_='pdp-header__title pdp-header__title_only-title')
        name = header.get_text()

        # получение бонусов
        item_bonus_block = product_offer_price.find('div', class_='product-offer-price-bonus product-offer-price-bonus_with-money-bonus')
        item_bonus = item_bonus_block.find('div', class_='money-bonus xs money-bonus_loyalty')
        if isinstance(item_bonus, bs4.element.Tag):
            bonus_percent = int(item_bonus.find('span', class_='bonus-percent').get_text().replace('%', ''))
            bonus_amount = int(item_bonus.find('span', class_='bonus-amount').get_text().replace(' ', ''))
        else:
            continue
        # получение названия магазина
        product_offer_name = item.find('div', class_='product-offer-name')
        market_name = product_offer_name.find('span', class_='pdp-merchant-rating-block__merchant-name').get_text()

        # расчет цены с учетом купона и кэшбека
        best_price = (price - cupon(price)) * (1 - bonus_percent / 100)

        # составление строки с данными и добавление к датафрейму
        df_item = pd.DataFrame({'наименование': [name], 'Магазин': [market_name], 'Полная цена': [price], 'Кэшбек': [bonus_amount],
                                'Процент Кэшбека': [bonus_percent], 'Купон': [cupon(price)],
                                'Стоимость с плюшками': [best_price], 'Ссылка': [link]})
        df = df._append(df_item)

    return df.sort_values(by=['Стоимость с плюшками'])