import tkinter
from tkinter import *
from tkinter import ttk


# def clicked():
#     res = "Привет {}".format(txt.get())                 #запись в переменную текста форматированного с учетом полученных данных из переменной txt
#     lbl.configure(text=res)                             #вставка в переленную lbl данных из переменной res в формате текста
#
#
# window = Tk()                                           #создание окна
# window.title("Добро пожаловать в приложение PythonRu")  #текст шапки окна
# window.geometry('400x250')                              #размер окна в пикселях
# lbl = Label(window, text="Привет")                      #объект в окне, текстовый
# lbl.grid(column=0, row=0)                               #положение объекта в окне (колонка, ряд)
# txt = Entry(window, width=10)                           #объект в окне, строка ввода
# txt.grid(column=1, row=0)                               #положение объекта в окне (колонка, ряд)
# btn = Button(window, text="Клик!", command=clicked)     #обект в окне, кнопка
# btn.grid(column=2, row=0)                               #положение объекта в окне (колонка, ряд)
# window.mainloop()                                       #функция постоянного показа окна


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
# links = [x27g, g24, rtx3060]
# links = {'x27g':x27g, 'g24':g24, 'rtx3060':rtx3060}
links = [1, 2, 3]
def click_btn(var):
    res = var.get()
    current_var = res
    return current_var
    # lbl.configure(text=res)

window = Tk()                                           #создание окна
window.configure(bg='#696565')                          #цвет фона окна
window.title("MM parser")                               #текст шапки окна
window.geometry('400x350')                              #размер окна в пикселях

current_var = StringVar()

lbl = Label(window, textvariable=current_var)                          #объект в окне, текстовый
lbl.pack()

combobox = ttk.Combobox(values=links, textvariable=current_var)
combobox.pack()

btn = Button(window, text='ok', command=click_btn(combobox), activebackground='red')
btn.pack()

window.mainloop()                                       #функция постоянного показа окна