from abc import ABC, abstractmethod


class AbstractClothes (ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, *diff_clothes):
        self.clothes = diff_clothes
        self.number = len(diff_clothes)

    @property
    def cost(self):
        cost_sum = 0
        for cloth in range(self.number):
            cost_sum += self.clothes[cloth].cost
        return cost_sum


class Coat(AbstractClothes):
    def __init__(self, param):
        self.size = param

    @property
    def cost(self):
        return self.size / 6.5 + 0.5


class Suit(AbstractClothes):
    def __init__(self, param):
        self.height = param

    @property
    def cost(self):
        return 2 * self.height + 0.3


coat = Coat(39)
suit = Suit(15)
suit2 = Suit(30)
clothes = Clothes(coat, suit, suit2)
print(coat.cost)
print(suit.cost)
print(suit2.cost)
print(clothes.cost)
