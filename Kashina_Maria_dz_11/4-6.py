class Storage:
    storage = {}

    def add_equipment(self, equipment, count):
        equipment_type = equipment.__class__.__name__
        try:
            self.storage[equipment_type][equipment.name] += count
        except KeyError:
            if equipment_type not in self.storage:
                self.storage[equipment_type] = {}
                self.storage[equipment_type][equipment.name] = count
            elif equipment.name not in self.storage[equipment_type]:
                self.storage[equipment_type][equipment.name] = count

    def __str__(self):
        output = ''
        for key, equipment in self.storage.items():
            output += f'{key}:\n'
            print(equipment)
            for el, count in equipment.items():
                output += f'\t{el} {count}\n'
        return output


class OfficeEquipment:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except ValueError:
            print(f'price {price} is not a number')
            self.__price = 'None'

    def __str__(self):
        return f'{self.name} {self.price}'


class Printer(OfficeEquipment):
    format = ['A2', 'A3', 'A4', 'A5']
    mode = ['black&white', 'colored']

    def __init__(self, name, price, formats, mode):
        super(Printer, self).__init__(name, price)
        self.formats = formats
        self.mode = mode

    def __str__(self):
        return f'{self.name} {self.formats} {self.mode} {self.price}руб'


class Scanner(OfficeEquipment):
    formats = ['A4', 'A5']
    mode = ['black&white', 'colored']

    def __init__(self, name, price, formats, mode):
        super(Scanner, self).__init__(name, price)
        self.formats = formats
        self.mode = mode

    def __str__(self):
        return f'{self.name} {self.formats} {self.mode} {self.price}руб'


class Xerox(OfficeEquipment):
    formats = ['A4', 'A5']
    mode = 'black&white'

    def __init__(self, name, price, formats):
        super(Xerox, self).__init__(name, price)
        self.formats = formats

    def __str__(self):
        return f'{self.name} {self.formats} {self.mode} {self.price}руб'


scanner = Scanner("Brother", "5500", "A5", 'black&white')
printer = Printer("Epson", "13000", "A2", 'colored')
xerox = Xerox("Xerox", "str", "A4")
printer2 = Printer("HP", "7000", "A4", 'black&white')
storage = Storage()
storage.add_equipment(scanner, 2)
storage.add_equipment(printer, 5)
storage.add_equipment(xerox, 10)
storage.add_equipment(printer2, 4)
print(storage)
print(xerox)
