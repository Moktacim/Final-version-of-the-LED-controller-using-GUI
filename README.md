# Final-version-of-the-LED-controller-using-GUI

### Required Hardware ###

- Arduino UNO (or any model of Arduino board)
- LED Stripe
- Power source (5V)
- Connecting wires

### Required Software ###

- Python (Updated version)
- Arduino IDE 

##############
Arduino Setup
##############

- File named "Set_brightness_level_using_GUI.ino" is need to be uploaded to the Arduino UNO.
  (If new arduino board need to be used then, select the correct board and port name from the
   drop down menu in the Arduino IDE)
- Connect the Vcc and Gnd pin of the LED stripe to the Arduino Vcc and Gnd.
- Every PWM pin is defied in the arduino script so that user can connect data pin of the LED stripe any of the PWM 
  pin and ready to go.

###############
Python Setup
###############

- File named "Application_interface_to_control_systems.py" is delivered with the full project 
- COM port will be automatically detected by the system and appeares to the GUI window. User need to select the 
  correct COM port. If the port does not appears then there is a "Refresh" button to refresh the system.
- There is a unique button to start and stop the system.
- System is created for the (32x1) LED in the LED stripe. Depending on the requirements it can be changed.
- Screen size can adjust from the GUI window. There are seperate window for the screen width and height. User can select the
  customised window size by giving the width and height.(Width and Height needs to be valid number otherwise error message will pop up)
- Brightness level can adjust from GUI window.
- Application is made (myapp) to run the system easily.
- When user will try to quit the Apps, there will be a pop up window for the confirmation of closing.

#########
Apps command
########

pyinstaller --onefile -n myapp file_name.py
