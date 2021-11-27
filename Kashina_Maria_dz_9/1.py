from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self.__color.items():
            sleep(value)
            print(key)


traffic_light1 = TrafficLight(color={'Красный': 3, 'Желтый': 2, 'Зеленый': 4})
traffic_light1.running()
