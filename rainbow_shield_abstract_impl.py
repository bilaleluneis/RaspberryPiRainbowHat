
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

    def __init__(self, index: int):
        self.__index = index

    @property
    def index(self) -> int:
        return self.__index

    @abstractmethod
    def blink(self):
        pass


"""
Initially I overrode __new__() in Color to prevent the creation
of instance, but then I realized that I need to create a dictionary
our of Color, so it made sense to allow instance creation of this class.
"""


class Color(object):

    def __init__(self, red: int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def color(self) -> Tuple[int, int, int]:
        return self.__red, self.__green, self.__blue


"""
overrode __new__() in Timer to prevent direct creation of instance.
but shouldn't prevent subclassing and calling __init_() from subclass.
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
This class uses inheritance of multiple classes to define what
a RainbowLed is and its capabilities.
"""


class RainbowLed(Led, Color, Timer):

    def __init__(self, index_id: int, clr: str, delay: float):
        Led.__init__(self, index_id)
        Timer.__init__(self, delay)
        (red, green, blue) = colors[clr].color
        Color.__init__(self, red, green, blue)

    def on(self):
        (red, green, blue) = self.color
        rainbow.set_pixel(self.index, red, green, blue)
        rainbow.show()

    def off(self):
        rainbow.set_pixel(self.index, 0, 0, 0)
        rainbow.show()

    def blink(self):
        self.on()
        sleep(self.delay)
        self.off()


# TODO: still need to implement
class RainbowShield:
    pass


def main():
    led_0: RainbowLed = RainbowLed(0, "green", 0.5)
    while True:
        led_0.blink()


if __name__ == "__main__":
    main()
