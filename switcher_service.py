#!/usr/bin/env python3
"""
Runs a webserver that listens to switch commands, and switcher the relays
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import sys

try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    print("USING DUMMY GPIO LIB")
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi  # Fake RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO  # Fake GPIO
    import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
PINS = {
    "button": {"pin_number": 5, "direction": "IN", "state": "LOW"},
    "relay1": {"pin_number": 26, "direction": "OUT", "state": "HIGH"},
    "realy2": {"pin_number": 19, "direction": "OUT", "state": "LOW"},
    "relay3": {"pin_number": 6, "direction": "OUT", "state": "LOW"},
    "relay4": {"pin_number": 13, "direction": "OUT", "state": "HIGH"},
    "relay5": {"pin_number": 12, "direction": "OUT", "state": "LOW"},
    "relay6": {"pin_number": 16, "direction": "OUT", "state": "LOW"},
    "relay7": {"pin_number": 20, "direction": "OUT", "state": "HIGH"},
    "relay8": {"pin_number": 21, "direction": "OUT", "state": "LOW"},
    "satus_led": {"pin_number": 7, "direction": "OUT", "state": "HIGH"},
}

HOSTNAME = "192.168.31.120"
PORT = 8091


def init_realys():
    print("Setting up pin data directions...")
    for name, pindata in PINS.items():
        print(f"Setting up pin for {name}... ", end="")

        if pindata["direction"] == "IN":
            GPIO.setup(pindata["pin_number"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
            print("IN PUD_UP")
        elif pindata["direction"] == "OUT":
            GPIO.setup(pindata["pin_number"], GPIO.OUT)
            print("OUT ", end="")
            if pindata["state"] == "LOW":
                GPIO.output(pindata["pin_number"], GPIO.LOW)
                print("LOW")
            elif pindata["state"] == "HIGH":
                GPIO.output(pindata["pin_number"], GPIO.HIGH)
                print("HIGH")


def switch(new_states):
    mutated_relays = []
    for relay, action in new_states.items():
        if relay not in [
            "relay1",
            "realy2",
            "relay3",
            "relay4",
            "relay5",
            "relay6",
            "relay7",
            "relay8",
        ]:
            continue
        try:
            if action == "toggle":
                new_state = GPIO.HIGH if PINS[relay]["state"] == "LOW" else GPIO.LOW
            elif action in ["on", "high"]:
                new_state = GPIO.HIGH
            elif action in ["off", "low"]:
                new_state = GPIO.LOW
            else:
                print(f"Unknown action: {action}")
                continue
            GPIO.output(PINS[relay]["pin_number"], new_state)
            PINS[relay]["state"] = "HIGH" if new_state == GPIO.HIGH else "LOW"
            mutated_relays.append(relay)
        except KeyError:
            print(f"Relay not found: {relay}")
    return mutated_relays


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path.lower()).query
        query_components = dict(
            (qc.split("=") if "=" in qc else [qc, "toggle"]) for qc in query.split("?")
        )
        # print(f"query_components: {query_components}")
        mutated_relays = switch(query_components)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("ok\n", "utf-8"))
        for relay in mutated_relays:
            self.wfile.write(
                bytes(
                    f"{relay}\t{'on' if PINS[relay]['state'] == 'LOW' else 'off'}\n",
                    "utf-8",
                )
            )



if __name__ == "__main__":
    init_realys()

    webServer = HTTPServer((HOSTNAME, PORT), Server)
    print(f"Server started http://{HOSTNAME}:{PORT}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server closed")
