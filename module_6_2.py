class Vehicle:
    __COLOR_VARIANTS = {'red', 'pink', 'blue', 'violet'}

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f"Модель: {self.__model}\n"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}\n"

    def get_color(self):
        return f"Цвет: {self.__color}\n"

    # распечатывает результаты методов (в том же порядке):get_model, get_horsepower, get_color, владельца
    def print_info(self):
        out_str = str(self.get_model())
        print(self.get_model() + self.get_horsepower() + self.get_color() +
              f'Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if str(new_color).lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __COLOR_VARIANTS = 5 # в седан может поместиться только 5 пассажиров


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
