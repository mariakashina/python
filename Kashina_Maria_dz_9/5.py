class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Пишет {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Чиркает {self.title}')


class Handle(Stationery):
    def draw(self):
         print(f'Скрипит {self.title}')


pen1 = Pen('Parker')
pen1.draw()
pencil1 = Pencil('KOH-I-NOOR')
pencil1.draw()
handle1 = Handle('centropen')
handle1.draw()
tassel = Stationery('Альбатрос')
tassel.draw()