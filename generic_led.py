__author__ = "Jieshu Wang & Bilal El Uneis"
__since__ = "November 2018"
__email__ = "foundwonder@gmail.com, bilaleluneis@gmail.com"

import time
import rainbowhat as rh


class GenericLed:
    def __init__(self, led_index: int, red_value: int, green_value: int, blue_value: int, sleep_time: float):
        self.__led_index = led_index
        self.__red_value = red_value
        self.__green_value = green_value
        self.__blue_value = blue_value
        self.__sleep_time = sleep_time

    def __led_on(self):
        rh.rainbow.set_pixel(self.__led_index, self.__red_value, self.__green_value, self.__blue_value)
        rh.rainbow.show()

    def __led_off(self):
        rh.rainbow.clear()

    def blink(self):
        self.__led_on()
        time.sleep(self.__sleep_time)
        self.__led_off()


class RedLed (GenericLed):

    def __init__(self, led_index: int, sleep_time: float):
        super().__init__(led_index, 255, 0, 0, sleep_time)


class RainbowShield:
    def __init__(self, sleep_time):
        self.__sleep_time = sleep_time

    def blink_left_right(self):
        for i in range(7):
            RedLed(led_index=i, sleep_time=self.__sleep_time).blink()

    def blink_right_left(self):
        for i in range(6, 0, -1):
            RedLed(led_index=i, sleep_time=self.__sleep_time).blink()


class RainBowShield:
    def __init__(self, sleep_time: int):
        self.__leds = []
        for index in range(7):
            self.__leds.append(RedLed(index, sleep_time))

    def run(self):
        while True:
            for led in range(7):
                self.__leds[led].blink()
            for led in range(6, 0, -1):
                self.__leds[led].blink()


def main():
    RainBowShield(0.5).run()


if __name__ == "__main__":
    main()
