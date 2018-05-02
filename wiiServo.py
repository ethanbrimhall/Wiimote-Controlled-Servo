import cwiid
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(2.5)

button_delay = 1.0

cycle = 0

print("Press 1 + 2 to pair Wiimote")
sleep(1)

try:
        wii=cwiid.Wiimote()
except RuntimeError:
        print("Cannot connect to your Wiimote")
        quit()

print("connected")
wii.rpt_mode = cwiid.RPT_BTN

ledMode = 1


try:
        while True:
                buttons = wii.state['buttons']
                if (buttons & cwiid.BTN_A):
                        if cycle == 0:
                                p.ChangeDutyCycle(12.5)
                                cycle = 1
                        else:
                                p.ChangeDutyCycle(2.5)
                                cycle = 0
                        sleep(button_delay)
except:
        p.stop()
        GPIO.cleanup()

