#!/usr/bin/env python3

import time
import datetime
import os

path = "/ram/internet/istherenet"

def w1():
    with open(path, "w") as file:
        file.write("1")

def w0():
    with open(path, "w") as file:
        file.write("0")

time.sleep(2)

def is_connected():
    now = datetime.datetime.now()
    if response == 0:
        print( now.hour, ":", now.minute, ":", now.second, "success")
        w1()
        time.sleep(5)
    else:
        print( now.hour, ":", now.minute, ":", now.second, "fail")
        w0()
        time.sleep(2)
        

while True:
    response = os.system("fping -b 1 -t 51 google.com")
    is_connected()
