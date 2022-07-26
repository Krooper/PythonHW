import datetime
import re


class WareHouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__free_space = capacity

    def acceptance(self, item):
        self.__free_space -= item.__volume


class Office_Equipment:
    def __init__(self, name, weight, cost, need_repair):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.need_repair = need_repair

    @property
    def volume(self):
        return None


class Printer(Office_Equipment):
    def __init__(self, name, weight, cost, need_repair, has_ink):
        super().__init__(name, weight, cost, need_repair)
        self.has_ink = has_ink
        self._coef = 0.7

    @property
    def volume(self):
        if self.has_ink:
            volume = self._coef + 0.1
        else:
            volume = self._coef
        return volume


class Scanner(Office_Equipment):
    __year = None
    __month = None
    __day = None

    def __init__(self, name, weight, cost, need_repair, production_date):
        super().__init__(name, weight, cost, need_repair)
        assert re.compile(r"^(\d{2}-){2}\d{4}$").match(production_date), f'wrong date {production_date}'
        self.production_date = production_date

    @property
    def volume(self):
        volume = 0.5
        return volume

    @classmethod
    def is_valid(cls, date):
        date_lst = date.split('-')
        cls.__day = int(date_lst[0])
        cls.__month = int(date_lst[1])
        cls.__year = int(date_lst[2])
        if cls.__year < 2017:
            return False
        return True

    @staticmethod
    def validator():
        # Проверка только для примера, по факту должна быть сложнее (меньшее кол-во дней в феврале и т.д.):
        if 0 < Scanner.__day < 32 and 0 < Scanner.__month < 13 and datetime.MINYEAR < Scanner.__year < datetime.MAXYEAR:
            return True
        return False


class Xerox(Office_Equipment):
    def __init__(self, name, weight, cost, need_repair, generation):
        super().__init__(name, weight, cost, need_repair)
        self.generation = generation
        if self.generation == 1:
            self.__speed = 50
        elif self.generation == 2:
            self.__speed = 75
        elif self.generation == 3:
            self.__speed = 100

    @property
    def volume(self):
        volume = 1.2
        return volume
