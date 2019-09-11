printf "\n\n\n"
printf "--------------------------------"
printf "--Started Autohome init script--"
printf "--------------------------------"

printf "\n-Setting up GPIO Pins..."
python3 /home/pi/cmd/auto/pinsetup.py

printf "\n-Setting relay defaults..."
python3 /home/pi/cmd/auto/relay_init.py

printf "\n-Starting button script..."
python3 /home/pi/cmd/auto/button.py

printf "--All done!\n"

#Notes:
#Place the simlinks of the scripts to /home/pi/cmd/auto for automatic execution
