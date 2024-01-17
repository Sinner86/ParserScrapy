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

df = pd.DataFrame()
df1 = pd.DataFrame({'наименование': [], 'Полная цена': [], 'Кэшбек': [], 'Процент Кэшбека': [], 'Стоимость с плюшками': []})
df2 = pd.DataFrame({'наименование': ['sun'], 'Полная цена': [17690], 'Кэшбек': [6000], 'Процент кэшбека': [30], 'Стоимость с плюшками': [10000]})
df = df1._append(df2)
print(df)