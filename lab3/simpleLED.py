import time
import RPi.GPIO as GPIO

LedPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def blink():
    while True:
        GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LedPin, GPIO.LOW)
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()
