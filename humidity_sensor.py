from Adafruit_DHT import read_retry, DHT11
from time import sleep


def main():
    while True:
        humidity, temp = read_retry(DHT11, 18)
        if humidity is not None:
            print("Current Humidity={}% and temp={}".format(humidity, temp))
        sleep(2)


if __name__ == "__main__":
    main()
