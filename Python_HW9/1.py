import time


class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        color_lst = ('красный', 'жёлтый', 'зелёный')
        while True:
            for color in color_lst:
                self.__color = color
                print(self.__color)
                if color == 'красный':
                    time.sleep(7)
                elif color == 'желтый':
                    time.sleep(2)
                else:
                    time.sleep(10)


traffic_light = TrafficLight()
traffic_light.running()
