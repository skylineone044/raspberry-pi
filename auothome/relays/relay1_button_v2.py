#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import pinsetup
import datetime

now = datetime.datetime.now()
path_lockstate = "/ram/relays/buttonlockstate"
def lockcheck():
    print("checking lock position...")
    with open("/home/pi/python/1/GPIO/buttonlockstate") as file:
        global lock
        lock = file.read()
    print("Done.")

def timecheck():
    if lock == "0":
        print("Checking the time...")
        if ( now.hour >= 6 ) and ( now.hour <= 19 ):
            print("Allowed, Proceeding...")
            os.system("relay1")
            print("Relay Toggled")
        else:
            print("Cannot turn on, button pressed outside of allowed timeframe.")
    elif lock == "1":
        print("Cannot toggle, deisabled by lock.")

##  Setting up GPIO  ##
print("Setting up GPIO...")
pinnum = 5
pinsetup.setup_pin_B1()
print("Done.")

##  MAIN  ## 
while True:
    try:
        print("Vaiting for buttonpress...")
        GPIO.wait_for_edge(pinnum, GPIO.RISING)
        print("BUtton1 pressed!")
        lockcheck()
        timecheck()
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
        print("Exited")
        break
