#!/usr/bin/env python3
"""
This module sets up the GPIO pins after startup, and sets their valuues
"""
import os
import json

try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils

    fake_rpigpio.utils.install()

