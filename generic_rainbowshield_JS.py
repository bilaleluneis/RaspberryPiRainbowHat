from __future__ import annotations

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
}


class Color(object):
    def __init__(self, color_name: str= None, color_rgb: Tuple[int, int, int]= None):
        if color_name is None and color_rgb is None:
            raise Exception("must at least pass one value for either name or rgb")
        elif color_name is not None:
            self.__color_name = color_name
        elif color_rgb is not None:
            self.__rgb_value: Tuple[int, int, int] = color_rgb

    @property
    # @abstractmethod
    def rgb(self) -> Tuple[int, int, int]:
        if self.__color_name in colors_dic:  # todo: the way you checked for key in the Dict is so cool, keep it!
            return colors_dic[self.__color_name]
        elif self.__rgb_value is None and self.__color_name == "random":
            return rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)
        elif self.__color_name is None and self.__rgb_value is not None:
            return self.__rgb_value
        else:
            raise Exception("unknown color!")

    def set_rgb(self, new_rgb: Tuple[int, int, int]):
        if new_rgb in colors_dic.values():
            self.__color_name = list(colors_dic.keys())[list(colors_dic.values()).index(new_rgb)]
        else:
            raise Exception("unknown rgb!")

    def get_name(self):
        return self.__color_name

    def __iadd__(self, new_color: str) -> Color:  # colorA += colorB
        r1, g1, b1 = self.rgb
        r2, g2, b2 = colors_dic[new_color]
        r3 = int((r2 - r1) / 10)
        g3 = int((g2 - g1) / 10)
        b3 = int((b2 - b1) / 10)
        self.__rgb_value = (r1 + r3), (g1 + g3), (b1 + b3)
        self.__color_name = None
        return self


class Timer(ABC):
    def __init__(self, delay_time: float):
        self.__delay_time = delay_time

    def get_delay(self) -> float:
        return self.__delay_time


class Led(Color, Timer):

    @property
    def rgb(self) -> Tuple[int, int, int]:
        r, g, b = super().rgb
        print("calling the overridden get_rgb in Led class with values R={} G={} B={} !".format(r, g, b))
        return r, g, b

    def __init__(self, led_index: int, led_timer: float, led_color: str=None, led_rgb: Tuple[int, int, int]=None):
        Color.__init__(self, color_name=led_color, color_rgb=led_rgb)
        Timer.__init__(self, led_timer)
        self.__led_index = led_index

    def on(self):
        r, g, b = self.rgb
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
            self.__leds.append(Led(i, self.__time_pattern, self.__color_pattern))

    def rainbow_run(self):
        for i in range(7):
            order_list = orders_dic[self.__order]
            order_index = order_list[i]
            self.__leds[order_index].blink()


def main():
    # Led(1, "red", 1.0).on()
    # Color("red")
    # while True:
    # RainbowShield("random", "random", 0.3).rainbow_run()
    # Led(1, "green", 2).set_rgb((255, 0, 0))
    led1 = Led(1, 0.2, "blue", None)
    while True:
        led1.blink()
        rgb = led1.rgb
        led_color = Color(color_name=None, color_rgb=rgb)
        led_color += "red"
        led_rgb = led_color.rgb
        led2 = Led(1, 0.2, None, led_rgb)
        led2.blink()


if __name__ == "__main__":
    main()
