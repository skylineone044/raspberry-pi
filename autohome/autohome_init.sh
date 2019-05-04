echo "\n\n\n"
echo "--------------------------------"
echo "--Started Autohome init script--"
echo "--------------------------------"

echo "\n-Setting up GPIO Pins..."
python3 /home/pi/cmd/auto/pinsetup_onboot.py

echo "\n-Setting relay defaults..."
python3 /home/pi/cmd/auto/relay_init.py

echo "\n-Starting button script..."
python3 /home/pi/cmd/auto/relay1_button_v2.py

echo "--All done!\n"

#Notes:
#Place the simlinks of the scripts to /home/pi/cmd/auto for automatic execution
