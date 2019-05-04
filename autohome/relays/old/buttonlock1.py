#!/usr/bin/python

path = "/ram/relays/buttonlockstate"

print("Reading current state....")
with open(path) as file:
    currstate = file.read()
print( currstate )
print("Done.")

print("Checking current state")
if currstate == "0":
    print("It's 0")
    with open(path, "w") as file:
        print("Changing to 1...")
        file.write("1")
    print("Done.")

elif currstate == "1":
    print("It's 1")
    with open(path, "w") as file:
        print("Changing to 0...")
        file.write("0")
    print("Done.")
else:
    print("error")
