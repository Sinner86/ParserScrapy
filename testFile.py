# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self, color, doors, tires, vtype):
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
#         self.vtype = vtype
#
#     def brake(self):
#         """
#         Stop the car
#         """
#         return "%s braking" % self.vtype
#
#     def drive(self):
#         """
#         Drive the car
#         """
#         return "I'm driving a %s %s!" % (self.color, self.vtype)
#
#
# if __name__ == "__main__":
#     car = Vehicle("blue", 5, 4, "car")
#     print(car.brake())
#     print(car.drive())
#
#     truck = Vehicle("red", 3, 6, "truck")
#     print(truck.drive())
#     print(truck.brake())

import pandas as pd
class ItemMM():
    def __init__(self, product_name, fullprice, bonus_percent, link = 'None', cupon = 0, market ='noName'):
        self.product_name = product_name
        self.fullprice = fullprice
        self.market = market
        self.bonus_percent = bonus_percent
        self.bonus_amount = self.fullprice * ((100 - self.bonus_percent) / 100)
        self.cupon = cupon
        self.bestprice = self.fullprice - self.cupon - self.bonus_amount
        self.link = link

    def to_df(self):
        df = pd.DataFrame({'наименование': [self.product_name], 'Магазин': [self.market], 'Полная цена': [self.fullprice],
                               'Кэшбек': [self.bonus_amount], 'Процент Кэшбека': [self.bonus_percent], 'Купон': [self.cupon],
                               'Стоимость с плюшками': [self.bestprice], 'Ссылка': [self.link]})

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

item = ItemMM('rtx3060', 31000, 36)
item.product_name = 'rtx4060'
print(item.product_name)