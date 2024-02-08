These scripts make up my remote light switch, which consists of a raspberry-pi,
and a relay board connected through GPIO.
The relays are connected to one lamp, 6 outlets, and one is unused.

## Files

- `switch_service.py`: listens for commands over http; changes the state of a
  relay, using an arbitrary designated name, based on which relay it is on the
  relay board.
- `button.py`: this script is started on boot, and monitors a GPIO pin that has
  a button connected to it
- due to crap wires, this setup often detects false-positive triggers, so a
  "hold down to activate" mechanism was implemented, that fixed the issue.

## Remote trigger from android

Remote triggering from an android device is achieved using tasker, which
can send http get requests, and these commands can be assigned to a button in
the android quick settings pane
