#!/usr/bin/env python3
"""
This file does thwe main switchong action
"""

import os
import json
import sys
import time
import pathlib

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# The realys pin numbers in order, for relay 1 is the [0] indexed item
PIN_LIST = ["26", "19", "13", "6", "12", "16", "20", "21"]
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + "/wdir"
WORKING_STATUS_FILE = WORKING_DIRECTORY + "/state.json"
LOCKFILE = WORKING_DIRECTORY + "/LOCK"


def unlock():
    try:
        os.remove(LOCKFILE)
    except FileNotFoundError:
        print("was not locked")


def switch(relayPin, toState):
    if os.path.isfile(LOCKFILE):
        print("locked, cannot switch")
        return -1
    open(LOCKFILE, 'a').close()

    try:
        toState = toState.upper()
        if toState not in ("SWITCH", "HIGH", "LOW", "ON", "OFF"):
            print("Invalid desired state given, aborting...")
            exit(2)

        # Read in current state of the relays

        with open(WORKING_STATUS_FILE, "r") as stateFile:
            data = json.load(stateFile)
            # print(data)

        if toState == "ON":
            toState = "HIGH"
        if toState == "OFF":
            toState = "LOW"

        try:
            if toState == data["pins"][relayPin]["state"]:
                print("Relay is in the desired state, done")
                exit(0)
        except KeyError:
            print(
                "This relay pin number [{}] is not configured to be switched!".format(relayPin)
            )
            exit(3)

        # if we got this far they we need to switch the realy

        # switching it
        current_state = data["pins"][relayPin]["state"]
        if data["pins"][relayPin]["direction"] == "OUT":
            GPIO.setup(int(relayPin), GPIO.OUT)
            if current_state == "HIGH":
                print("Switching pin {} to LOW...".format(relayPin))
                GPIO.output(int(relayPin), GPIO.LOW)
                data["pins"][relayPin]["state"] = "LOW"
            elif current_state == "LOW":
                print("Switching pin {} to HIGH...".format(relayPin))
                GPIO.output(int(relayPin), GPIO.HIGH)
                data["pins"][relayPin]["state"] = "HIGH"
        else:
            print("This pin is configured as an input!")
            exit(4)

        # writing out changed data

        with open(WORKING_STATUS_FILE, "w") as stateFile:
            print("Writing out state...")
            json.dump(data, stateFile, indent=4)

    finally:
        time.sleep(0.2)
        print("Done")
        unlock()


def relayLookup(relayPin):
    """
    picks the right realy number
    if the input number is bare, it returns it,
    as it is the default GPIO numbering mode

    if the first character of the relayPin is an "R", then we are int the
    realtive realy numbering mode, in this case relay numbers have to be between
    1-8, as that is how many relays are connected to the pi. based on the number,
    we pick the correct GPIO pin number from the PIN_LIST
    """
    if relayPin[0] in ("R", "r"):
        try:
            return PIN_LIST[int(relayPin[1])-1]
        except IndexError:
            print("no such relay configured")
            exit(5)
    else:
        return relayPin


if __name__ == "__main__":
    try:
        relayPin = sys.argv[1]
    except IndexError:
        print("No relay number given, abording...")
        exit(1)

    relayPin = relayLookup(relayPin)

    try:
        toState = sys.argv[2]
    except IndexError:
        print("No desired state given, defaulting to switching")
        toState = "SWITCH"

    try:
        switch(relayPin, toState)
    finally:
        unlock()
