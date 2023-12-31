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
a.speed = 30
a.drive()
