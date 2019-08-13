#!/usr/bin/env python3
'''
This module manages the button
'''

import time
import datetime
import json
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PINNUM = 5
GPIO.setup(PINNUM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
SKIP_TIME_CHECK = True
NOW = datetime.datetime.now()
PATH = "/ram/relays/STATES.json"
SLEEP_TIME = 5
def lockcheck():
    '''
    This function check wether on not the button-lock
    is on.
    '''
    print("checking lock position...")
    with open(PATH) as datafile_json:
        data_json = datafile_json.read()
        data = json.loads(data_json)
        state = data[0] # the 1st item in the list is
                        #the value that stores the button-lock state
    print("Done.")
    return state

def timecheck(lock_state):
    '''
    This function checks the timeframe for switching the relay
    '''

    if lock_state == "0":
        print("Checking the time...")
        if (NOW.hour >= 6) and (NOW.hour <= 19) or (SKIP_TIME_CHECK == True):
            print("Allowed, Proceeding...")
            switch()
        else:
            print("Cannot turn on, button pressed outside of allowed timeframe.")
    elif lock_state == "1":
        print("Cannot toggle, deisabled by lock.")

def switch():
    '''
    This function switches the relay corresponding to the button
    '''
    os.system("python3 /home/pi/cmd/switch.py 1")

##  MAIN  ##
while True:
    try:
        print("Vaiting for buttonpress...")
        GPIO.wait_for_edge(PINNUM, GPIO.RISING)
        print("BUtton1 pressed!")
        timecheck(lockcheck())
        print("Sleeping...")
        time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
        print("Exited")
        break
