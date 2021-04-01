#!/usr/bin/env python3
"""
This file does thwe main switchong action
"""

import os
import json
import sys

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO

WORKING_STATUS_FILE = "wdir/state.json"

try:
    RELAY_TO_BE_SWITCHED = sys.argv[1]
except IndexError:
    print("No relay number given, abording...")
    exit(1)

try:
    DESIRED_STATE = sys.argv[2]
except IndexError:
    print("No desired state given, defaulting to switching")
    DESIRED_STATE = "SWITCH"

if DESIRED_STATE.upper() not in ("SWITCH", "HIGH", "LOW", "ON", "OFF"):
    print("Invalid desired state given, aborting...")
    exit(2)

# Read in current state of the relays

with open(WORKING_STATUS_FILE, "r") as stateFile:
    data = json.load(stateFile)
    print(data)


if DESIRED_STATE == "ON":
    DESIRED_STATE = "HIGH"
if DESIRED_STATE == "OFF":
    DESIRED_STATE = "LOW"

try:
    if DESIRED_STATE == data["pins"][RELAY_TO_BE_SWITCHED]["state"]:
        print("Relay is in the desired state, done")
        exit(0)
except KeyError:
    print(
        f"This relay pin number [{RELAY_TO_BE_SWITCHED}] is not configured to be switched!"
    )
    exit(3)

# if we got this far they we need to switch the realy

## switching it
current_state = data["pins"][RELAY_TO_BE_SWITCHED]["state"]
if data["pins"][RELAY_TO_BE_SWITCHED]["direction"] == "OUT":
    if current_state == "HIGH":
        print(f"Switching pin {RELAY_TO_BE_SWITCHED} to LOW...")
        GPIO.output(int(RELAY_TO_BE_SWITCHED), GPIO.LOW)
        data["pins"][RELAY_TO_BE_SWITCHED]["state"] = "LOW"
    elif current_state == "LOW":
        print(f"Switching pin {RELAY_TO_BE_SWITCHED} to HIGH...")
        GPIO.output(int(RELAY_TO_BE_SWITCHED), GPIO.HIGH)
        data["pins"][RELAY_TO_BE_SWITCHED]["state"] = "HIGH"
else:
    print("This pin is configured as an input!")
    exit(4)

## writing out changed data

with open(WORKING_STATUS_FILE, "w") as stateFile:
    print("Writing out state...")
    json.dump(data, stateFile, indent=4)

print("Done")
