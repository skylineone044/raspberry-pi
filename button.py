#!/usr/bin/env python3
"""
This module handles the button, for manual control
"""
try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()
