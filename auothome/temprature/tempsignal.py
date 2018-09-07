#!/usr/bin/env python3
import relaylist
import os
import time
import RPi.GPIO as GPIO

switch_relay = relaylist.relayswitch

##  Setting up GPIO  ##
print("Setting up GPIO...")
pinnum = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnum, GPIO.OUT)
print("Done.")

is_fan_on = False

def checktemp():
    with open("/sys/class/thermal/thermal_zone0/temp") as file:
        rawtemp = file.read(3)   #Read the file
        celsius = float(rawtemp) / 10   #Converting, dividing
        print(celsius)   #Print the number
        return celsius


def main(is_fan_on, celsius = checktemp()):
        while True:
            celsius = checktemp()		
                while celsius > 55:
                    print("HOT:  " + str(celsius))
                    GPIO.output(pinnum, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinnum, GPIO.LOW)
                    time.sleep(0.5)
                    celsius = checktemp()
                GPIO.output(pinnum, GPIO.LOW)
                if celsius >= 60:
                    switch_relay(6)
                    is_fan_on = True
                elif celsius < 40 and is_fan_on == True:
                    switch_relay(6)
                    is_fan_on = False
                    time.sleep(0.5)

main(is_fan_on, celsius = checktemp())

