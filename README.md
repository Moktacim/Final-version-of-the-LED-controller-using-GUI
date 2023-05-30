# Final-version-of-the-LED-controller-using-GUI
LED stripe color controlling using GUI Apps

##############
Arduino Setup
##############

- File named "Set_brightness_level_using_GUI.ino" is already uploaded to the Arduino UNO.
  (If new arduino board need to be used then, select the correct board and port name from the
   drop down menu in the Arduino IDE)

- Every PWM pin is defied in the arduino script so that user can connect LED stripe any PWM 
  pin and ready to go.

###############
Python Setup
###############

- File named "Application_interface_to_control_systems.py" is delivered with the full project
- COM port will be automatically detected by the system and appeares to the GUI window.
- System is created for the (32x1) LED in the LED stripe. Depending on the requirements it can be changed.
- Screen size can adjust from the GUI window.
- Brightness level can adjust from GUI window.
- Application is made to run the whole system easily.


#########
Apps command
########

pyinstaller --onefile -n myapp file_name.py
