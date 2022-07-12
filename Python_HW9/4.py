class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self._speed = 0
        self.direction = None
        self.is_police = False

    def go(self):
        print('Введите скорость:')
        self._speed = int(input())
        self.direction = 'прямо'
        print(f'Машина едет {self.direction}.')

    def stop(self):
        print('Машина остановилась.')
        self._speed = 0

    def turn(self):
        print('Введите направление поворота:')
        self.direction = input()
        print(f'Машина повернула {self.direction}.')

    def show_speed(self):
        print(f'Скорость машины: {self._speed}.')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.__speed = 0

    def show_speed(self):
        while self.__speed > 60:
            print(f'Скорость машины: {self._speed} - превышение!')
            print('Задайте скорость заново')
            TownCar.go(self)
        print(f'Скорость машины: {self._speed}.')


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        while self._speed > 40:
            print(f'Скорость машины: {self._speed} - превышение!')
            print('Задайте скорость заново')
            WorkCar.go(self)
        print(f'Скорость машины: {self._speed}.')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


town_car = TownCar('красная', 'Лада')
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.turn()
print(f'Цвет машины: {town_car.color}, марка машины: {town_car.name}, машина полицейская: {town_car.is_police}')
town_car.show_speed()
town_car.stop()
town_car.show_speed()
print()


sport_car = SportCar('жёлтая', 'Феррари')
sport_car.show_speed()
sport_car.go()
sport_car.show_speed()
sport_car.turn()
print(f'Цвет машины: {sport_car.color}, марка машины: {sport_car.name}, машина полицейская: {sport_car.is_police}')
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()
print()


work_car = WorkCar('белый', 'Форд')
work_car.show_speed()
work_car.go()
work_car.show_speed()
work_car.turn()
print(f'Цвет машины: {work_car.color}, марка машины: {work_car.name}, машина полицейская: {work_car.is_police}')
work_car.show_speed()
work_car.stop()
work_car.show_speed()
print()

police_car = PoliceCar('синий', 'Хёндэ')
police_car.show_speed()
police_car.go()
police_car.show_speed()
police_car.turn()
print(f'Цвет машины: {police_car.color}, марка машины: {police_car.name}, машина полицейская: {police_car.is_police}')
police_car.show_speed()
police_car.stop()
police_car.show_speed()
print()
