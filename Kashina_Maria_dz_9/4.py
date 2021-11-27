class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed > 0:
            print(f'{self.name} едет')

    def stop(self):
        if self.speed == 0:
            print(f'{self.name} остановилась')

    def turn(self, direction):
        if direction:
            print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    pass


taxi = TownCar(70, 'white', 'Volkswagen Polo', False)
taxi.go()
taxi.stop()
taxi.turn('налево')
taxi.show_speed()
print(taxi.name, taxi.speed, taxi.color, taxi.is_police)

balid = SportCar(200, 'red', 'Mazda RX7', False)
balid.go()
balid.stop()
balid.turn('направо')
balid.show_speed()
print(balid.name, balid.speed, balid.color, balid.is_police)

truck = WorkCar(40, 'black', 'MAN', False)
truck.go()
truck.stop()
truck.turn('')
truck.show_speed()
print(truck.name, truck.speed, truck.color, truck.is_police)

police = PoliceCar(0, 'whitlish blue', 'UAZ', True)
police.go()
police.stop()
police.turn('')
police.show_speed()
print(police.name, police.speed, police.color, police.is_police)
