#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

print(" --- Netsignal script started --- ")
print("Setting up...")
pinnum = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinnum, GPIO.OUT)
print("Done.")

def checkstat():
    print("Reading internet state from file...")
    with open("/ram/internet/istherenet") as file:
        netstat = file.read()
    print("Read data:", netstat)
    print("Done.")
    global netstat

print("Defining blink() function")
def blink():
    while netstat == "0":
        print("netstat = 0")
        GPIO.output(pinnum, GPIO.LOW)
        print("pin LOW")
        time.sleep(0.5)
        GPIO.output(pinnum, GPIO.HIGH)
        print("pin HIGH")
        print("rechecking status...")
        checkstat()
        print("Done.")
        time.sleep(0.5)
print("Done")

print("Starting main loop...")
while True:
    checkstat()
    print("Checking data...")
    if netstat == "1":
        print("netstat = 1")
        GPIO.output(pinnum, GPIO.HIGH)
        print("Pin ON")
    elif netstat == "0":
        print("netstat = 0")
        print("Starting blink() function...")
        blink()
    else:
        print("Error")
    time.sleep(1)
