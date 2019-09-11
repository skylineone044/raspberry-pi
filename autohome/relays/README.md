#This is used to switch GPIO relays, easily with a single command

##Files:
* pinsetup.py:  Sets up the GPIO pins for the correct In-Out modes  
* relay_init.py:Initialises the list of default states in a json file  
* relaylist.py: This it where the magic happens  
* switch.py:    This one interfaces with the rest, passes in the correct args. (You have to call this one to make it go)  
* button.py:    This manages a button connected to a pin, and switches relay 1 when activated  


