#!/usr/bin/env python3
"""
This file does thwe main switchong action
"""
try:
    import RPi.GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()