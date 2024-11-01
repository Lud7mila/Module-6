import math

class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__color = [0, 0, 0]  # список цветов в формате RGB
        self.filled = False  # закрашенный
        self.set_color(list(color)[0], list(color)[1], list(color)[2])
        self.__sides = []  # список сторон(целые числа)
        self.set_sides(*args)
        self.filled = True

    # Служебный метод __is_valid_color - принимает параметры r, g, b.
    # Метод проверяет корректность переданных значений перед установкой нового цвета.
    # Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    # Метод set_color - принимает параметры r, g, b - числа и изменяет атрибут__color на соответствующие
    # значения, предварительно проверив их на корректность. Если введены
    # некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Метод get_color - возвращает список RGB цветов.
    def get_color(self):
        return self.__color

    # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает:
    # True, если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
    # False - во всех остальных случаях.
    def __is_valid_sides(self, new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side < 0:
                return False
        return True

    # Метод set_sides(self, *new_sides) должен принимать новые стороны,
    # если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        elif not self.filled:
            self.__sides = [1] * self.sides_count

    # Метод get_sides должен возвращать значения атрибута __sides.
    def get_sides(self):
        return self.__sides

    # Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color, *args)
        # __radius - рассчитывается, исходя из длины окружности (одной единственной стороны).
        self.__radius = args[0] / (2 * math.pi)

    # Метод get_square - возвращает площадь круга
    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    # Метод get_square - возвращает площадь треугольника
    def get_square(self):
        perimeter = self.__len__()
        sides = self.get_sides()
        result = perimeter
        for side in sides:
            result *= perimeter - side
        return math.sqrt(result)

class Cube (Figure):
    sides_count = 12

    def __init__(self, color, *args):
        if len(args) == 1 and isinstance(args[0], int) and args[0] > 0:
            self.__sides = [args[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

        self.set_color(list(color)[0], list(color)[1], list(color)[2])
        self.filled = True

    # Переопределенный метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает:
    # True, если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
    # False - во всех остальных случаях.
    def __is_valid_sides(self, new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side < 0:
                return False
        return True

    # Переопределенный метод set_sides(self, *new_sides) должен принимать новые стороны,
    # если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    # Переопределенный метод get_sides должен возвращать значения атрибута __sides.
    def get_sides(self):
        return self.__sides

    # Переопределенный метод get_volume - возвращает объём куба.
    def get_volume(self):
        return self.__sides[0] ** 3

    # Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())

# triangle = Triangle((41, 51, 61), 1, 3, 9)
# print(triangle.get_square())
