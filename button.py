#!/usr/bin/env python3
"""
This module handles the button, for manual control
"""
import sys
import time

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO

import switcher_service

SLEEP_TIME = 5
BLINK_TIME = 0.2
TIME_CHECK = False

LONG_PRESS_TIME_SECONDS = 0.15

BUTTON_PIN = 5
LED_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

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


def wait_for_long_press():
    while True:
        print("Wainting...")
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
        print("Pressed")
        start = time.time()
        # time.sleep(0.05)

        while GPIO.input(BUTTON_PIN) == GPIO.LOW:
            time.sleep(0.01)
            length = time.time() - start
            print(length)

            if length > LONG_PRESS_TIME_SECONDS:
                print("Long Press")
                return True
            else:
                print("Short Press")


try:
    while True:
        print("Waiting for buttonpress...")
        if wait_for_long_press():
            print("Button pressed!")
            switcher_service.switch({"relay1": "toggle"})
        blinkStatusLED()

except KeyboardInterrupt:  # if ctrl+c pressed exit cleanly
    GPIO.cleanup()
finally:  # cleanup GPIO on normal exit
    GPIO.cleanup()
