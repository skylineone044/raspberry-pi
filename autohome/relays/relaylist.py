#!/usr/bin/python3
'''
This is the main switching module for the GPIO pins
'''
import RPi.GPIO as GPIO
import json

print("\n  --- Relay toggle script started! ---   ")

##  Setting up GPIO  ##
print("Setting up GPIO...")
GPIO.setmode(GPIO.BCM)
print("Done.")

def relayswitch(relaynum):
    '''
    This is the main switching function
    '''
    ####RELAY_instance = RELAY.check, RELAY.switch, RELAY.write
    print("Defining pinlist...")
    pinlist = [None, 26, 19, 13, 6, 12, 16, 20, 21]

    print("Creating 'pin' variable...")
    pin = pinlist[relaynum]

    #print("Setting up GPIO...")
    #GPIO.setup(pin, GPIO.OUT)

    print("Creating 'path' variable...")
    path = "/ram/relays/STATES.json"

    print("Retrieving 'state' variable...")
    with open(path) as datafile_json:
        data_json = datafile_json.read()
        data = json.loads(data_json)
        state = data[relaynum]

    print("Switching relay...")
    switch(pin, state)

    print("Writing statefile...")
    write(state, path)

    print("     --- Done ---\n\n\n")

def check(relaynum, path):
    print("Reading current state of relay from file...")
    with open(path) as file:
        state = file.read()
    print("Done.")
    return state

def write(state, path):
    print("Writing...")
    with open(path, "w") as file:
        if state == "1":
            file.write("0")
        elif state == "0":
            file.write("1")
        else:
            print("Error: 1")
    print("Done.")

def switch(pin, state):
    if state == "0":
        print("Current state: OFF, turning ON...")
        GPIO.output(pin, GPIO.LOW)
        print("Relay on")

    elif state == "1":
        print("Current state: ON, turning OFF...")
        GPIO.output(pin, GPIO.HIGH)
        print("Relay off")
    else:
        print("Error: 2")
