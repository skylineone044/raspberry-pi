#!/usr/bin/env python3
import os

print("Making folder in /ram...")
try:
    os.system("mkdir /ram/relays")
except:
    print("Oops! seems you do not have the /ram directory!\n Please creathe it, and mount it in the ram")
print("creating path...")
path = "/ram/relays/"

## Deafults -------------
print("Reading defaults...")
default_buttonlockstate = "0"
default_r1stat = "1"
default_r2stat = "1"
default_r3stat = "0"
default_r4stat = "1"
default_r5stat = "1"
default_r6stat = "1"
default_r7stat = "1"
default_r8stat = "1"

## creating the files
print("Creating files...")
os.system("touch {}buttonlockstate".format(path))
os.system("touch {}r1stat".format(path))
os.system("touch {}r2stat".format(path))
os.system("touch {}r3stat".format(path))
os.system("touch {}r4stat".format(path))
os.system("touch {}r5stat".format(path))
os.system("touch {}r6stat".format(path))
os.system("touch {}r7stat".format(path))
os.system("touch {}r8stat".format(path))

## Setting the values in the files
print("Setting values...")
with open("/ram/relays/buttonlockstate", "w") as f_bls:
    f_bls.write(default_buttonlockstate)

with open("/ram/relays/r1stat", "w") as f_r1s:
    f_r1s.write(default_r1stat)

with open("/ram/relays/r2stat", "w") as f_r2s:
    f_r2s.write(default_r2stat)

with open("/ram/relays/r3stat", "w") as f_r3s:
    f_r3s.write(default_r3stat)

with open("/ram/relays/r4stat", "w") as f_r4s:
    f_r4s.write(default_r4stat)

with open("/ram/relays/r5stat", "w") as f_r5s:
    f_r5s.write(default_r5stat)

with open("/ram/relays/r6stat", "w") as f_r6s:
    f_r6s.write(default_r6stat)

with open("/ram/relays/r7stat", "w") as f_r7s:
    f_r7s.write(default_r7stat)

with open("/ram/relays/r8stat", "w") as f_r8s:
    f_r8s.write(default_r8stat)
print("All done!")

