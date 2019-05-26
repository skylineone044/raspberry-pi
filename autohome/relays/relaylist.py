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

    print("Cheching current state...")
    state, data = check_current_pin_state(relaynum, path)

    print("Switching relay...")
    switch_current_pin(pin, state)

    print("Writing statefile...")
    write_new_pin_state(data, path, relaynum)

    print("     --- Done ---\n\n\n")

def check_current_pin_state(relaynum, path):
    '''
    This function checks the current state of a relay that
    is stored in the path as a json file
    '''
    print("Retrieving 'state' variable...")
    with open(path) as datafile_json:
        data_json = datafile_json.read()
        data = json.loads(data_json)
        state = data[relaynum]
    return state, data

def write_new_pin_state(data, path, relaynum):
    '''
    This function writes the new state of the relay to the json file
    '''
    print("Writing...")
    with open(path, "w") as datafile_json:
        if data[relaynum] == 0:
            data[relaynum] = 1
        elif data[relaynum] == 1:
            data[relaynum] = 0
        data_json = json.dumps(data)
        datafile_json.write(data_json)
    print("Done.")

def switch_current_pin(pin, state):
    '''
    This function switches the relay
    '''
    GPIO.setup(pin, GPIO.OUT)
    if state == 0:
        print("Current state: OFF, turning ON...")
        GPIO.output(pin, GPIO.LOW)
        print("Relay on")

    elif state == 1:
        print("Current state: ON, turning OFF...")
        GPIO.output(pin, GPIO.HIGH)
        print("Relay off")
    else:
        print("Error: Cant swtich relay")
