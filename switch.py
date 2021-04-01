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

with open("wdir/state.json", "r") as stateFile:
    data = json.load(stateFile)
    print(data)


