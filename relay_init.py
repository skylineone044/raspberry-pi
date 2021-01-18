#!/usr/bin/env python3
"""
This module sets up the GPIO pins after startup, and sets their valuues
"""
import os
import json

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpigpio.utils

    fake_rpigpio.utils.install()

print("Starting relay setkup...")
# Set up directory srructure in the ram directory

# with open("state.json", "w") as jsonFile:
#     data = {"Working_dir": "wdir", "relay_states": [0, 0, 1, 0, 1, 1, 1, 1, 1]}
#     json.dump(data, jsonFile)

print("Reading config...")
with open("state.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)

print("Creating storage structure...")
os.system(f"mkdir {data['Working_dir']}")
with open(f"{data['Working_dir']}/state.json", "w") as statefile:
    json.dump(data, statefile)

print("Done!")
