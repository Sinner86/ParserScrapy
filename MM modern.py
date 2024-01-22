import parser_function as pf
import pandas as pd
import openpyxl

# список наименований товаров для поиска
targets = ['rtx 3060', 'rtx 4060', 'Xiaomi X27G', 'sun-m27bg130']
# targets = ['rtx 3060']

x27g = ['https://megamarket.ru/catalog/details/monitor-xiaomi-x27g-g27-165hz-1920x1080-ips-600013078509/#?details_block=prices']
sunwind130 = ['https://megamarket.ru/catalog/details/monitor-sunwind-chernyy-sun-m27bg130-100045194336_11440/']
rt0700c = ['https://megamarket.ru/catalog/details/frezer-makita-rt0700c-100022771469/#?details_block=prices']
dbo180z = ['https://megamarket.ru/catalog/details/akkumulyatornaya-ekscentrikovaya-shlifovalnaya-mashina-makita-dbo180z-100000379620/']
rtx3060 = ['https://megamarket.ru/catalog/details/videokarta-msi-nvidia-geforce-rtx-3060-ventus-2x-12g-oc-100028286028/']
Makita2012NB = ['https://megamarket.ru/catalog/details/stanok-reysmusovyy-makita-2012nb-123670-100022771140/#?related_search=%D1%80%D0%B5%D0%B9%D1%81%D0%BC%D1%83%D1%81%20makita']

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
            info.to_excel(writer, sheet_name=str(targeet))
    finally:
        writer.close()

def main2(links):
    links = links
    path = 'output_page.xlsx'
    writer = pd.ExcelWriter(path)
    try:
        for link in links:
            # запуск драйвера браузера и получение данных
            pf.get_source_html(url=link)
            # переработка полученных данных в таблицу
            info = pf.get_items_page(file_path='source-page-mm.html')
            # запись в файл
            info.to_excel(writer)
    finally:
        writer.close()
if __name__ == '__main__':
    main(targets)
    # main2(rtx3060)
