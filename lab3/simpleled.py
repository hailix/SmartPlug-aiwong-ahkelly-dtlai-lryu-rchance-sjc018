import RPi.GPIO as GPIO
import time
import SmartSound

ledpin = 27
ledstate = 0
env_th = 80

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)

SS = SmartSound.SmartSound()


while True:
    envelopeVal = SS.get_envelope()
    print envelopeVal

    if (envelopeVal > env_th and ledstate == 1):
        print "LED off"
        GPIO.output(ledpin, GPIO.LOW)
        ledstate = 0
        time.sleep(0.2)
    elif (envelopeVal > env_th and ledstate == 0):
        print "LED on"
        GPIO.output(ledpin, GPIO.HIGH)
        ledstate = 1
        time.sleep(0.2)
    time.sleep(0.1)


    


