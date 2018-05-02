#cwiid is used for wii controller
import cwiid
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7,50)

#start servo at 7.5
p.start(7.5)

print("Press 1 + 2 to pair Wiimote")
sleep(1)

#pairing the wii controller with raspberry pi via bluetooth
try:
        wii=cwiid.Wiimote()
except RuntimeError:
        print("Cannot connect to your Wiimote")
        quit()

#sets wii mode
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

#this while loop checks the wii controller location forever and updates servo location based on coordinates
while True:
        location = wii.state['acc'][0]
        if location < 110:
                p.ChangeDutyCycle(2.5)
        elif location < 115:
                p.ChangeDutyCycle(3.5)
        elif location < 120:
                p.ChangeDutyCycle(4.5)
        elif location < 125:
                p.ChangeDutyCycle(5.5)
        elif location < 130:
                p.ChangeDutyCycle(6.5)
        elif location < 135:
                p.ChangeDutyCycle(7.5)
        elif location < 140:
                p.ChangeDutyCycle(8.5)
        elif location < 145:
                p.ChangeDutyCycle(9.5)
        elif location < 150:
                p.ChangeDutyCycle(10.5)
        elif location < 155:
                p.ChangeDutyCycle(11.5)
        elif location < 160:
                p.ChangeDutyCycle(12.5)
        else:
                p.ChangeDutyCycle(12.5)
        sleep(0.01)
