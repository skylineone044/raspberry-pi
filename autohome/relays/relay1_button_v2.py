#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import pinsetup
import datetime
import time

skiptimecheck = True
now = datetime.datetime.now()
path_lockstate = "/ram/relays/buttonlockstate"
def lockcheck():
    print("checking lock position...")
    with open("/ram/relays/buttonlockstate") as file:
        global lock
        lock = file.read()
    print("Done.")

def timecheck():
    if lock == "0":
        print("Checking the time...")
        if ( now.hour >= 6 ) and ( now.hour <= 19 ) or (skiptimecheck == True):
            print("Allowed, Proceeding...")
            #os.system("python3 relay1.py")
            import relaylist
            relaylist.relayswitch(1)
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
        print("Sleeping...")
        time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
        print("Exited")
        break
