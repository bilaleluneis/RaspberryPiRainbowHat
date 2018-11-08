
__author__ = "Bilal El Uneis"
__since__ = "November 2018"
__email__ = "bilaleluneis@gmail.com"

from abc import ABC, abstractmethod
from typing import Tuple, Dict
from rainbowhat import rainbow
from time import sleep

"""
Led is abstract class, so it can't be instantiated. 
added abstract method blink() that will require and override
from sub classes.
"""


class Led(ABC):

    def __init__(self, identifier: int):
        self.__id = identifier

    @property
    def identifier(self) -> int:
        return self.__id

    @abstractmethod
    def blink(self):
        pass


"""
Initially I overrode __new__() in Color to prevent the creation
of instance, but then I realized that I need to create a dictionary
our of Color, so it made sense to allow instance creation of this class.
I also overloaded the == operator to allow testing 2 colors for equality.
"""


class Color(object):

    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def rgb_value(self) -> Tuple[int, int, int]:
        return self.__red, self.__green, self.__blue

    def __eq__(self, color):  # overload the == operator
        (r1, g1, b1) = self.rgb_value
        (r2, g2, b2) = color.rgb_value
        if r1 == r2 and g1 == g2 and b1 == b2:
            return True
        else:
            return False


"""
overrode __new__() in Timer to prevent direct creation of instance.
but shouldn't prevent subclassing and calling __init__() from subclass.
"""


class Timer(object):

    def __init__(self, delay: float):
        self.__delay = delay

    def __new__(cls, *args, **kwargs):
        if cls is Timer:
            raise TypeError("Timer is abstracts class!")
        return object.__new__(cls)

    @property
    def delay(self) -> float:
        return self.__delay

    @delay.setter
    def delay(self, value: float):
        self.__delay = value


"""
Simple Map / Dictionary of basic colors.
"""


colors: Dict[str, Color] = {
    "red": Color(255, 0, 0),
    "orange": Color(255, 127, 0),
    "yellow": Color(255, 255, 0),
    "green": Color(0, 255, 0),
    "blue": Color(0, 0, 255),
    "violet": Color(139, 0, 255),
    "white": Color(255, 255, 255)
}


"""
RainbowLed is class that represents a LED on a RainbowShield.
This class uses inheritance of multiple classes (Led and Timer)
and composition of Color class to define what a RainbowLed is and its capabilities. 
"""


class RainbowLed(Led, Timer):

    def __init__(self, index_id: int, clr: str, delay: float):
        Led.__init__(self, index_id)
        Timer.__init__(self, delay)
        self.__color: Color = colors[clr]

    @property
    def color(self) -> str:
        for color_name, a_color in colors.items():
            if self.__color == a_color:
                return color_name
        raise Exception("Unknown Color!")

    @color.setter
    def color(self, new_color: str):
        self.__color = colors.get(new_color, Color(-1, -1, -1))
        if self.__color == Color(-1, -1, -1):
            raise Exception("Invalid Color been assigned!")

    def on(self):
        (red, green, blue) = self.__color.rgb_value
        rainbow.set_pixel(self.identifier, red, green, blue)
        rainbow.show()

    def off(self):
        rainbow.set_pixel(self.identifier, 0, 0, 0)
        rainbow.show()

    def blink(self):
        self.on()
        sleep(self.delay)
        self.off()


# TODO: still need to implement
class RainbowShield:
    pass


def main():
    led_0: RainbowLed = RainbowLed(0, "white", 1)
    for color_name, color in colors.items():
        led_0.color = color_name
        led_0.blink()


if __name__ == "__main__":
    main()
