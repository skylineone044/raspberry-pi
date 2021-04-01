#!/usr/bin/env python3
"""
This module handles the button, for manual control
"""
import os
import json
import sys
import time
import datetime

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO

from tendo import singleton
me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

import switch


SLEEP_TIME = 5
BLINK_TIME = 0.2
TIME_CHECK = False

BUTTON_PIN = 5
LED_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)


def isUnlocked() -> bool:
    if TIME_CHECK:
        if (datetime.datetime.now().hour >= 7) and (
            datetime.datetime.now().hour <= 22
        ):
            return True
        else:
            return False
    else:
        return True


def blinkStatusLED():
    on = True
    timeout_end = time.time() + SLEEP_TIME
    while time.time() < timeout_end:
        if on:
            GPIO.output(LED_PIN, GPIO.LOW)
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)
        on = not on
        time.sleep(BLINK_TIME)
    GPIO.output(LED_PIN, GPIO.HIGH)


try:
    while True:
        print("Waiting for buttonpress...")
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
        print("Button pressed!")
        if isUnlocked():
            switch.switch("26", "SWITCH")
        blinkStatusLED()
except KeyboardInterrupt:  # if ctrl+c pressed exit cleanly
    GPIO.cleanup()

except:  # this catches ALL other exceptions including errors.
    GPIO.cleanup()

finally:  # cleanup GPIO on normal exit
    GPIO.cleanup()
