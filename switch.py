#!/usr/bin/env python3
"""
This file does thwe main switchong action
"""

import os
import json
import sys

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
WORKING_STATUS_FILE = "wdir/state.json"


def switch(relayPin, toState):
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

    ## switching it
    current_state = data["pins"][relayPin]["state"]
    if data["pins"][relayPin]["direction"] == "OUT":
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

    ## writing out changed data

    with open(WORKING_STATUS_FILE, "w") as stateFile:
        print("Writing out state...")
        json.dump(data, stateFile, indent=4)

    print("Done")


if __name__ == "__main__":
    try:
        relayPin = sys.argv[1]
    except IndexError:
        print("No relay number given, abording...")
        exit(1)

    try:
        toState = sys.argv[2]
    except IndexError:
        print("No desired state given, defaulting to switching")
        toState = "SWITCH"

    switch(relayPin, toState)
