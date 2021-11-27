class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_full_salary(self):
        print(self._income['wage'] + self._income['bonus'])


worker1 = Position('Name', 'Surname', 'boss', 100, 20000000)
worker1.get_full_salary()
worker1.get_full_name()
print(worker1.name)
print(worker1.surname)
print(worker1.position)
print(worker1._income)
