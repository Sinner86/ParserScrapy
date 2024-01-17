# создание класса и интерфейса объекта

class Machine():
    def __init__(self, color='red', speed=20):
        """Constructor"""
        self.__color = color
        self.__speed = speed
        print('создан класс Machine')

# инкапсуляция с помощью свойства
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, speed):
        if 0 <= speed:
            self.__speed = speed
        else:
            print ("Недопустимое значение")

# инкапсуляция с помощью геттер и сеттрет для цвета
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



class Figure:
    def __init__(self, color = 'red'):
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, c):
        self.__color = c
class Rectangle(Figure):
    def __init__(self, width, height):
        Figure.__init__(self)
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError
    def area(self):
        return self.__width * self.__height

a = Rectangle(10, 20)
print(a.color)
a.color = 'green'
print(a.color)