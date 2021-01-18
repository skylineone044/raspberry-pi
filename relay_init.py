#!/usr/bin/env python3
"""
This module sets up the GPIO pins after startup, and sets their values
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

BOOT_CONFIG_FILE = "BootState.json"

print("Starting relay setup...")
GPIO.setmode(GPIO.BCM)
# Set up directory srructure in the ram directory
try:
    if sys.argv[1] in ("--Write-config", "-Wc"):
        print("Writing config...")
        with open(BOOT_CONFIG_FILE, "w") as jsonFile:
            data = {
                "Working_dir": "wdir",
                "pins": [
                    {"number": 5, "direction": "IN", "state": "LOW"},
                    {"number": 26, "direction": "OUT", "state": "LOW"},
                    {"number": 19, "direction": "OUT", "state": "HIGH"},
                    {"number": 13, "direction": "OUT", "state": "LOW"},
                    {"number": 6, "direction": "OUT", "state": "HIGH"},
                    {"number": 12, "direction": "OUT", "state": "HIGH"},
                    {"number": 16, "direction": "OUT", "state": "HIGH"},
                    {"number": 20, "direction": "OUT", "state": "HIGH"},
                    {"number": 21, "direction": "OUT", "state": "HIGH"},
                    {"number": 7, "direction": "OUT", "state": "HIGH"},
                ],
            }
            # 0. item is the button, the next 8 are relay pins,
            # the last in the pins group is the status LED
            json.dump(data, jsonFile, indent=4)
except IndexError:
    pass

print("Reading config...")
with open(BOOT_CONFIG_FILE, "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)

print("Creating storage structure...")
os.system(f"mkdir {data['Working_dir']}")
with open(f"{data['Working_dir']}/state.json", "w") as statefile:
    json.dump(data, statefile)

print("Setting up pin data directions...")
for i, pin in enumerate(data["pins"]):
    print(f"Setting up pin {pin['number']}... ", end="")
    if pin["direction"] == "IN":
        GPIO.setup(pin["number"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("IN PUD_UP")
    elif pin["direction"] == "OUT":
        GPIO.setup(pin["number"], GPIO.OUT)
        print("OUT ", end="")
        if pin["state"] == "LOW":
            GPIO.output(pin["number"], GPIO.LOW)
            print("LOW")
        elif pin["state"] == "HIGH":
            GPIO.output(pin["number"], GPIO.HIGH)
            print("HIGH")

print("Done!")
