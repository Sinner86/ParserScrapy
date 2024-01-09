# создание класса и интерфейса объекта

class Machine():
    def __init__(self, color='red', speed=20):
        """Constructor"""
        self.__color = color
        self.__speed = speed
        print('создан класс Machine')

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, speed):
        if 0 <= speed:
            self.__speed = speed
        else:
            print ("Недопустимое значение")

# геттер и сеттрет для цвета
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color

    def drive(self):
        print(f"driving, speed = {self.__speed}")

    def stop(self):

        print(f"stop, speed = 0")

class Auto(Machine):
    def __init__(self):
        pass

a = Machine()
a.drive()
a.stop()
a.drive()
a.set_color('green')
print(a.get_color())

