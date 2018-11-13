#!/usr/bin/python
import RPi.GPIO as GPIO
import pinsetup

GPIO.setmode(GPIO.BCM)

def staton():
    pinsetup.statled()
    GPIO.output(7, GPIO.HIGH)
    print("Status LED is ON")

def main():
    staton()
    pinsetup.hotled()
    pinsetup.netstatled()
    pinsetup.setup_pin1()
    pinsetup.setup_pin2()
    pinsetup.setup_pin3()
    pinsetup.setup_pin4()
    pinsetup.setup_pin5()
    pinsetup.setup_pin6()
    pinsetup.setup_pin7()
    pinsetup.setup_pin8()
    pinsetup.setup_pin_B1()
    pinsetup.setup_pin_B2()

main()
