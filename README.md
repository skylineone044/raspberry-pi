These scripts make up my remote light switch, which consists of a raspberry-pi, and a relay board connected through GPIO.
The relays are connected to one lamp, 6 outlets, and one is unused.

## Files

- `BootState.json`: this stored the default state of the realys
- `relay_init.py`: this script initializes the relyas after bootup, based on the `BootState.json`
- `switch.py`: this changes the state of a relay, using either its GPIO pin number, or an arbitrary designated number, based on which relay it is on the realy board.
  - This script is activated through `ssh` for remote operation
- `button.py`: this script is started on boot, and monitrs a GPIO pin that has a button connected to its
  - due to crap wires, this setup often detect false-positive triggers, so a "hold down to activae" mechanism was implemented, that fixed the issue.

The current state is stored in a json file located in a ram disk, to reduce the number of writes to the raspberry-pi's sd card

## Remote trigger from android

Remote triggering from an android device is acheived using openssh through termux (A powerful terminal emulator for android)

- `Tasker` is used to create a button in the android quick setting pane
- `Termux: Tasker` plugin is used to execute termux shell scripts from tasker
- `Termux` executes a shell scrit, that runs `switch.py R1` over ssh
- for ssh, keyfile autchentication is used
