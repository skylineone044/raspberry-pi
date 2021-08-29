#!/usr/bin/env python3
"""
This module sets up the GPIO pins after startup, and sets their values
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


BOOT_CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + "/BootState.json"

print("Starting relay setup...")
GPIO.setmode(GPIO.BCM)
# Set up directory srructure in the ram directory
try:
    if sys.argv[1] in ("--Write-config", "-Wc"):
        print("Writing config...")
        with open(BOOT_CONFIG_FILE, "w") as jsonFile:
            data = {
                "Working_dir": os.path.dirname(os.path.abspath(__file__)) + "/wdir",
                "pins": {
                    "5": {"direction": "IN", "state": "LOW"},
                    "26": {"direction": "OUT", "state": "LOW"},
                    "19": {"direction": "OUT", "state": "HIGH"},
                    "13": {"direction": "OUT", "state": "LOW"},
                    "6": {"direction": "OUT", "state": "HIGH"},
                    "12": {"direction": "OUT", "state": "HIGH"},
                    "16": {"direction": "OUT", "state": "HIGH"},
                    "20": {"direction": "OUT", "state": "HIGH"},
                    "21": {"direction": "OUT", "state": "HIGH"},
                    "7": {"direction": "OUT", "state": "HIGH"},
                },
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
os.system("mkdir {}".format(data['Working_dir']))
with open("{}/state.json".format(data['Working_dir']), "w") as statefile:
    json.dump(data, statefile)

print("Setting up pin data directions...")
for pin, pindata in data["pins"].items():
    print("Setting up pin {}... ".format(pin), end="")

    if pindata["direction"] == "IN":
        GPIO.setup(int(pin), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print("IN PUD_UP")
    elif pindata["direction"] == "OUT":

        GPIO.setup(int(pin), GPIO.OUT)
        print("OUT ", end="")
        if pindata["state"] == "LOW":
            GPIO.output(int(pin), GPIO.LOW)
            print("LOW")
        elif pindata["state"] == "HIGH":
            GPIO.output(int(pin), GPIO.HIGH)
            print("HIGH")

print("Done!")
