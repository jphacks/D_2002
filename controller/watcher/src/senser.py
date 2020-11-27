import time
import RPi.GPIO as GPIO

# インターバル
INTERVAL = 0.03
# スリープタイム
SLEEPTIME = 0.03
# 使用するGPIO
GPIO_PIN_RIGHT = 18
GPIO_PIN_LEFT = 17

GPIO_PIN_LIST = [GPIO_PIN_RIGHT, GPIO_PIN_LEFT]
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_LIST, GPIO.IN)


def get_data():
    # センサー感知
    try:
        if (GPIO.input(GPIO_PIN_RIGHT) == GPIO.HIGH or GPIO.input(GPIO_PIN_LEFT) == GPIO.HIGH):
            return True
        else:
            print(f'LIGHT{GPIO.input(GPIO_PIN_RIGHT)}')
            print(f'LEFT{GPIO.input(GPIO_PIN_LEFT)}')
            return False
    except Exception as e:
        print(e)


def main():
    while True:
        get_data()
        time.sleep(SLEEPTIME)


if __name__ == '__main__':
    main()
