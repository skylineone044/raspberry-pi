#!/usr/bin/python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def statled():
    GPIO.setup(7, GPIO.OUT)
    print("Pin 7 (statled) Set: OUT")

def netstatled():
    GPIO.setup(25, GPIO.OUT)
    print("Pin 25 (netstatled) Set: OUT")

def hotled():
    GPIO.setup(24, GPIO.OUT)
    print("Pin 24 (hotled) Set: OUT")

def setup_pin1():
    GPIO.setup(26, GPIO.OUT)
    print("Pin 26 (1) Set: OUT")

def setup_pin2():
    GPIO.setup(19, GPIO.OUT)
    print("Pin 19 (2) Set: OUT")

def setup_pin3():
    GPIO.setup(13, GPIO.OUT)
    print("Pin 13 (3) Set: OUT")
    GPIO.output(13, GPIO.HIGH)
    print("Pin 13 has been turned ON!")

def setup_pin4():
    GPIO.setup(6, GPIO.OUT)
    print("Pin 6 (4) Set: OUT")

def setup_pin5():
    GPIO.setup(12, GPIO.OUT)
    print("Pin 12 (5) Set: OUT")

def setup_pin6():
    GPIO.setup(16, GPIO.OUT)
    print("Pin 16 (6) Set: OUT")
    GPIO.output(16, GPIO.HIGH)
    print("Pin 16 has been turned ON!   Note:When pin is on = relay is off")

def setup_pin7():
    GPIO.setup(20, GPIO.OUT)
    print("Pin 20 (7) Set: OUT")

def setup_pin8():
    GPIO.setup(21, GPIO.OUT)
    print("Pin 21 (8) Set: OUT")

def setup_pin_B1():
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("Pin 5 (9) Set: IN, Pulled UP")

def setup_pin_B2():
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("Pin 8 (netstatled) Set: IN, Pulled UP")
