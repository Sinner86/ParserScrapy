import parser_function as pf
import pandas as pd
# import openpyxl

# список наименований товаров для поиска
# targets = ['rtx 3060', 'rtx 4060', 'Xiaomi X27G', 'sun-m27bg130']
targets = ['rtx 3060', 'rtx 4060']
links = ['https://megamarket.ru/catalog/details/monitor-xiaomi-x27g-g27-165hz-1920x1080-ips-600013078509/#?details_block=prices']

def main(targets):
    baseURL = 'https://megamarket.ru'
    targets = targets
    path = 'output.xlsx'

    # подготовка файла для экспорта данных
    writer = pd.ExcelWriter(path)
    try:
        for target in targets:
            # подготовка ссылки
            targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')
            # запуск драйвера браузера и получение данных
            pf.get_source_html(url=targetURL)
            # переработка полученных данных в таблицу
            info = pf.get_items(file_path='source-page-mm.html')
            # запись в файл
            info.to_excel(writer, sheet_name=f'{target}')
    finally:
        writer.close()

def main2(link):
    path = 'output_page.xlsx'
    writer = pd.ExcelWriter(path)
    try:
        for link in links:
            # запуск драйвера браузера и получение данных
            # pf.get_source_html(url=link)
            # переработка полученных данных в таблицу
            info = pf.get_items_page(file_path='source-page-mm.html')
            # запись в файл
            info.to_excel(writer)
    finally:
        writer.close()
if __name__ == '__main__':
    # main(targets)
    main2(links)
