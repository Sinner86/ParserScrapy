import parser_function as pf
import pandas as pd
import openpyxl
import time

# список наименований товаров для поиска
# targets = ['rtx 3060', 'rtx 4060', 'Xiaomi X27G', 'sun-m27bg130', 'jbl boombox 3']
# targets = ['rtx 3060', 'rtx 4060','Xiaomi X27G', 'DTM50Z', 'DBO180Z']
targets = ['Honor Pad X9 128']

# x27g до 9000
x27g = ['https://megamarket.ru/catalog/details/monitor-xiaomi-x27g-g27-165hz-1920x1080-ips-600013078509/#?details_block=prices']
# g24 до 7000
g24 = ['https://megamarket.ru/catalog/details/monitor-xiaomi-23165-238-chernyy-23165-600009835519/#?details_block=prices&related_search=xiaomi%20redmi%20g24']
# sunwind130 до 11000
sunwind130 = ['https://megamarket.ru/catalog/details/monitor-sunwind-chernyy-sun-m27bg130-100045194336_11440/']
# rt0700c до 6800
rt0700c = ['https://megamarket.ru/catalog/details/frezer-makita-rt0700c-100022771469/#?details_block=prices']
# dbo180z до 6800
dbo180z = ['https://megamarket.ru/catalog/details/akkumulyatornaya-ekscentrikovaya-shlifovalnaya-mashina-makita-dbo180z-100000379620/']
# rtx3060 до 18000
rtx3060 = ['https://megamarket.ru/catalog/details/videokarta-msi-nvidia-geforce-rtx-3060-ventus-2x-12g-oc-100028286028/']
# Makita2012NB до 43000
Makita2012NB = ['https://megamarket.ru/catalog/details/stanok-reysmusovyy-makita-2012nb-123670-100022771140/#?related_search=%D1%80%D0%B5%D0%B9%D1%81%D0%BC%D1%83%D1%81%20makita']
JBL3 = ['https://megamarket.ru/catalog/details/portativnaya-kolonka-jbl-boombox-3-hacks-467020-600009488256/#?related_search=jbl%20boombox%203']
# x27gq до 13000
x27gq = ['https://megamarket.ru/catalog/details/27-monitor-xiaomi-p27qba-rx-chernyy-165hz-2560h1440-ips-600014023315_11428/']
# Реноватор Makita DTM50Z
DTM50 = ['https://megamarket.ru/catalog/details/akkumulyatornyy-renovator-makita-dtm50z-100000379664/#?related_search=dtm50z']
# Планшет TabA9plus
TabA9plus = ['https://megamarket.ru/catalog/details/planshet-samsung-galaxy-tab-a9-sm-x210-4-64gb-silver-eac-600014860296/']
# Планшет HPadX9
HPadX9 = ['https://megamarket.ru/catalog/details/planshet-honor-pad-x9-lte-115-2023-4-64gb-seryy-5301agtm-wi-fi-cellular-600013937719/']
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
            info.to_excel(writer, sheet_name=str(target))
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
    # main(targets)
    # main2(Makita2012NB)
    main2(HPadX9)
