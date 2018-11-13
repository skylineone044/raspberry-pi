#!/usr/bin/python
import RPi.GPIO as GPIO

print("\n  --- Relay toggle script started! ---   ")

##  Setting up GPIO  ##
print("Setting up GPIO...")
GPIO.setmode(GPIO.BCM)
print("Done.")

def relayswitch(relaynum):
	####RELAY_instance = RELAY.check, RELAY.switch, RELAY.write
    print("Defining pinlist...")
    pinlist = [None, 26, 19, 13, 6, 12, 16, 20, 21]
    print("Creating 'pin' variable...")
    pin = pinlist[relaynum]
    print("Setting up GPIO...")
    GPIO.setup(pin, GPIO.OUT)
    print("Creating 'path' variable...")
    path = "/ram/relays/r" + str(relaynum) + "stat"
    print("Retrieving 'state' variable...")
    state = RELAY.check(RELAY, relaynum, path)
    print("Switching relay...")
    RELAY.switch(RELAY, pin, state)
    print("Writing statefile...")
    RELAY.write(RELAY, state, path)
    print("     --- Done ---\n\n\n")

class RELAY():
    def check(self, relaynum, path):
        print("Reading current state of relay from file...")
        with open(path) as file:
            state = file.read()
        print("Done.")
        return state

    def write(self, state, path):
        print("Writing...")
        with open(path, "w") as file:
            if state == "1":
                file.write("0")
            elif state == "0":
                file.write("1")
            else:
                print("Error: 1")
            print("Done.")

    def switch(self, pin, state):
        if state == "0":
            print("Current state: OFF, turning ON...")
            GPIO.output(pin, GPIO.LOW)
            print("Relay on")

        elif state == "1":
            print("Current state: ON, turning OFF...")
            GPIO.output(pin, GPIO.HIGH)
            print("Relay off")
        else:
            print("Error: 2")

