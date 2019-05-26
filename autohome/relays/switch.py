#!/usr/bin/python3

print("\n  --- Relay toggle script started! ---   ")
#import RPi.GPIO as GPIO
import sys
import relaylist

relaylist.relayswitch(sys.argv[1])
