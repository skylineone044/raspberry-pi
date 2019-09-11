#!/usr/bin/env python3
'''
This module converts and writest the default values in json format
to PATH
'''
import os
import json

PATH = "/ram/relays/"

print("Making folder in /ram...")
try:
    os.system("mkdir {}".format(PATH))
except:
    print("Oops! seems you do not have the /ram directory!\n Please creathe it, and mount it in the ram")
print("creating path...")

## Deafults -------------
print("Reading defaults...")
DEFAULT_STATES = [0, 0, 1, 0, 1, 1, 1, 1, 1]
# The 1st item is the buttonlock state, the rest are the relays

## creating the files
print("Creating files...")
DATAFILE = "{}STATES.json".format(PATH)
os.system("touch {}".format(DATAFILE))
os.system("sudo chmod 777 {}".format(DATAFILE))

## Setting the values in the files
print("Setting values...")
DATA_JSON = json.dumps(DEFAULT_STATES)
with open(DATAFILE, "w") as DATAFILE_JSON:
    DATAFILE_JSON.write(DATA_JSON)
print("All done!")
