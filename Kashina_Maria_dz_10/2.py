from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def area_full(self):
        return f'Потрачено ткани: {(self.v / 6.5 + 0.5) + (2 * self.h + 0.3):.2f}'

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):

    def area_for_thing(self):
        return f'Для пальто нужно: {self.v / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Пальто'


class Suit(Clothes):

    def area_for_thing(self):
        return f'Для костюма нужно: {2 * self.h + 0.3 :.2f} ткани'

    def abstract(self):
        return 'Костюм'


coat1 = Coat(6.5, 0.35)
suit1 = Suit(6.5, 0.35)
print(coat1.area_for_thing())
print(suit1.area_for_thing())
print(coat1.area_full)
print(coat1.abstract())
