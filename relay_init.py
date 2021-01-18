#!/usr/bin/env python3
"""
This module sets up the GPIO pins after startup, and sets their valuues
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


print("Starting relay setkup...")
GPIO.setmode(GPIO.BCM)
# Set up directory srructure in the ram directory
try:
    if sys.argv[1] in ("--Write-config", "-Wc"):
        print("Writing config...")
        with open("state.json", "w") as jsonFile:
            data = {
                "Working_dir": "wdir",
                "pins": [5, 26, 19, 13, 6, 12, 16, 20, 21, 7],  # pin numbers
                "pin_directions": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 in 1 out
                "pin_states": [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],  # 0 off 1 on
            }
            # 0. item is the button, the next 8 are relay pins,
            # the last in the pins group is the status LED
            json.dump(data, jsonFile)
except IndexError:
    pass

print("Reading config...")
with open("state.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)

print("Creating storage structure...")
os.system(f"mkdir {data['Working_dir']}")
with open(f"{data['Working_dir']}/state.json", "w") as statefile:
    json.dump(data, statefile)

print("Setting up pin data directions...")
for i, pin in enumerate(data["pins"]):
    print(f"Setting up pin {pin}... ", end="")
    if data["pin_directions"][i] == 0:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("IN PUD_UP")
    elif data["pin_directions"][i] == 1:
        GPIO.setup(pin, GPIO.OUT)
        print("OUT ", end="")
        if data["pin_states"][i] == 0:
            GPIO.output(pin, GPIO.LOW)
            print("LOW")
        elif data["pin_states"][i] == 1:
            GPIO.output(pin, GPIO.HIGH)
            print("HIGH")

print("Done!")
