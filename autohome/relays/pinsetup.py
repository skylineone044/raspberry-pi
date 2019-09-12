#!/usr/bin/env python3
'''
This module initialises the pist to be
ready to accept signal, and in the correct direction (IN / OUT)
'''

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PINLIST = [7, 26, 19, 13, 6, 12, 16, 20, 21, 5]
# 1. item is the stat led, last item is a button

for i in range(len(PINLIST)):
    '''
    This loops through all the select pins in PINLIST
    and sets their direction (IN / OUT) accodingly

    IT also set special pins
    '''
    if i < 9:
        GPIO.setup(PINLIST[i], GPIO.OUT)
        print("Pin {0} Set: OUT".format(PINLIST[i]))
    if PINLIST[i] == 5:
        GPIO.setup(PINLIST[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("Pin 5 (9) Set: IN, Pulled UP")
    if PINLIST[i] == 13:
        GPIO.setup(13, GPIO.OUT)
        print("Pin 13 (3) Set: OUT")
        GPIO.output(13, GPIO.HIGH)
        print("Pin 13 has been turned ON!")
    if PINLIST[i] == 7:
        GPIO.output(PINLIST[i], GPIO.HIGH)
