import parser_function as pf
import pandas as pd
# import openpyxl


targets = ['rtx 3060', 'rtx 4060']
# targets = ['rtx 3060']
def main(targets):
    baseURL = 'https://megamarket.ru'
    targets = targets
    path = 'output.xlsx'

    # return pf.get_items(file_path='source-page-mm.html')
    # with open(path, mode="a+") as writer:

    # writer = open(path, 'a+')
    # try:
    #     for target in targets:
    #         targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')
    #         pf.get_source_html(url=targetURL)
    #         info = pf.get_items(file_path='source-page-mm.html')
    #         info.to_excel(path, sheet_name=f'{target}')
    # finally:
    #     writer.close()

    writer = pd.ExcelWriter(path)
    for target in targets:
        targetURL = baseURL + '/catalog/?q=' + target.replace(' ', '%20')
        pf.get_source_html(url=targetURL)
        info = pf.get_items(file_path='source-page-mm.html')
        info.to_excel(writer, sheet_name=f'{target}')
    writer.close()

if __name__ == '__main__':
    main(targets)
