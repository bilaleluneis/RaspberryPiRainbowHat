__author__ = "Jieshu Wang"
__since__ = "November 2018"
__email__ = "foundwonder@gmail.com"

import time
import rainbowhat as rh
from abc import ABC
from typing import Dict, Tuple, List
import random as rd

colors_dic: Dict[str, Tuple[int, int, int]] = {
    "red": (255, 0, 0),
    "orange": (255, 127, 0),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "violet": (139, 0, 255),
    "white": (255, 255, 255),
    "none": (0, 0, 0)
    # "random": (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
}


class Color(ABC):
    def __init__(self, color_name: str):
        self.__color_name = color_name

    # fixme: you can make the bellow a function at top level of file and remove the need for the Color class
    def get_rgb(self) -> Tuple[int, int, int]:
        if self.__color_name in colors_dic:  # todo: the way you checked for key in the Dict is so cool, keep it!
            return colors_dic[self.__color_name]
        elif self.__color_name == "random":
            return rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)
        else:
            raise Exception("unknown color name!")


class Timer(ABC):
    def __init__(self, delay_time: float):
        self.__delay_time = delay_time

    def get_delay(self) -> float:
        return self.__delay_time


class Led(Color, Timer):
    def __init__(self, led_index: int, led_color: str, led_timer: float):
        Color.__init__(self, led_color)  # fixme: do you really need Color class? you are using Tuple in the dict
        Timer.__init__(self, led_timer)
        self.__led_index = led_index

    def on(self):
        r, g, b = self.get_rgb()
        rh.rainbow.set_pixel(self.__led_index, r, g, b)
        rh.rainbow.show()

    def off(self):
        rh.rainbow.set_pixel(self.__led_index, 0, 0, 0)
        rh.rainbow.show()

    def blink(self):
        self.on()
        a_delay: float = self.get_delay()
        time.sleep(a_delay)
        self.off()


orders_dic: Dict[str, list] = {
    "right to left": [0, 1, 2, 3, 4, 5, 6],
    "left to right": [6, 5, 4, 3, 2, 1, 0],
    "random": [rd.randint(0, 6), rd.randint(0, 6), rd.randint(0, 6), rd.randint(0, 6),
               rd.randint(0, 6), rd.randint(0, 6), rd.randint(0, 6)],
    "none": [-1, -1, -1, -1, -1, -1, -1]
}


class Order:
    def __init__(self, order_name: str):
        self.__order_name = order_name

    def get_order(self):
        if self.__order_name in orders_dic:
            return orders_dic[self.__order_name]
        else:
            raise Exception("unknown order!")


class RainbowShield:
    def __init__(self, order: str, color_pattern: str, time_pattern: float):
        self.__order = order
        self.__color_pattern = color_pattern
        self.__time_pattern = time_pattern
        self.__leds: List[Led] = []  # always initialize before use even to empty
        for i in range(7):
            self.__leds.append(Led(i, self.__color_pattern, self.__time_pattern))

    def rainbow_run(self):
        for i in range(7):
            order_list = orders_dic[self.__order]
            order_index = order_list[i]
            self.__leds[order_index].blink()


def main():
    # Led(1, "red", 1.0).on()
    while True:
        RainbowShield("random", "random", 0.3).rainbow_run()


if __name__ == "__main__":
    main()
