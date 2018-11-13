#!/usr/bin/python

print("\n  --- Relay 4 toggle script started! ---   ")
import RPi.GPIO as GPIO
import relaylist

relaylist.relayswitch(4)
