from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'жёлтый', 'зеленый']
        self.__time = [7, 2, 7]

    # def running(self):
    #     for i in cycle(self.__color):
    #         print(i)
    #         if i == 'красный':
    #             time.sleep(7)
    #         elif i == 'жёлтый':
    #             time.sleep(2)
    #         else:
    #             time.sleep(7)

    def running(self):
        for i in cycle(zip(self.__color, self.__time)):
            print(i[0])
            time.sleep(i[1])


light = TrafficLight()
light.running()
