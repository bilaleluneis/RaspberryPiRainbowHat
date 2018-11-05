__author__ = "Bilal El Uneis"
__since__ = "November 2018"
__email__ = "bilaleluneis@gmail.com"

import time
import rainbowhat as rh


def blink_from_right_to_left():
    for light in range(7):
        rh.rainbow.clear()
        rh.rainbow.set_pixel(light, 255, 0, 0)
        rh.rainbow.show()
        time.sleep(0.2)


def blink_from_left_right():
    for light in range(6, 0, -1):
        rh.rainbow.clear()
        rh.rainbow.set_pixel(light, 255, 0, 0)
        rh.rainbow.show()
        time.sleep(0.2)


def main():
    while True:
        blink_from_right_to_left()
        blink_from_left_right()


if __name__ == "__main__":
    main()
