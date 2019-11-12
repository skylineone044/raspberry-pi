#!/usr/bin/python

path = "/ram/relays/buttonlockstate"

print("Reading current state....")
with open(path) as file:
    currstate = file.read()
print( currstate )
print("Done.")
dojgn bsrh
rangezhre
hasattr(rwh
        )
print("Checking current state")
if currstate == "0":
    print("It's 0")
    with open(path, "w") as file:
        print("Changing to 1...")
        file.write("1")
    pri