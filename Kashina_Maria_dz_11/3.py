class ListOfNumbers:
    def __init__(self):
        self.my_list = []

    def elements(self):
        while True:
            try:
                val = int(input('Введите значение: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list}')
                answer = input(f'Если хотите закончить, введите "stop": ').lower()
                if answer == 'stop':
                    print(f'Вы вышли')
                    break
            except ValueError:
                print(f"Введено не число")
                print(f'Текущий список - {self.my_list}')
                answer = input(f'Если хотите закончить, введите "Stop": ').lower
                if answer == 'stop':
                    print(f'Вы вышли')
                    break


list1 = ListOfNumbers()
print(list1.elements())
