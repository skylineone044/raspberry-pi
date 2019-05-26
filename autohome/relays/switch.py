#!/usr/bin/python3
'''
this module interfaces with the rest,
and calls relay switch with the right argument
'''

print("\n  --- Relay toggle script started! ---   ")
#import RPi.GPIO as GPIO
import sys
import relaylist

relaylist.relayswitch(int(sys.argv[1]))
