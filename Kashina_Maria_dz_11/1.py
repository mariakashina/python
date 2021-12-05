from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('.')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('.')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Incorrect data'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('.')
            date(int(year), int(month), int(day))
            return 'Correct data!'
        except ValueError:
            return 'Incorrect data!'


print(Data.valid('05.13.2021'))
print(Data.valid('05.12.2021'))
print(Data.type('05.12'))
print(Data.type('05.12.2021'))
