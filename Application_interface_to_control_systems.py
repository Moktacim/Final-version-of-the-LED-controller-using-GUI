import serial
from tkinter import *
import tkinter as tk
import time
import pyautogui
from PIL import Image
import numpy as np
from tkinter import Tk, Label
from tkinter.ttk import Scale, Style
import ctypes
from tkinter import messagebox
from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox
from serial.tools import list_ports

# Set up serial communication with Arduino Uno
ser = True

# Define LED strip parameters
NUM_LEDS = 33
screen_width = 1920
screen_height = 1080

# LED state
led_state = False

# Functions
def start_led():
    global led_state
    led_state = True
    ser.write(b'START')  # Send command to start LED

def stop_led():
    global led_state
    led_state = False
    ser.write(b'STOP')  # Send command to stop LED

    off_command = [0] * NUM_LEDS * 3
    off_command_str = ' '.join(str(c) for c in off_command)
    off_command_str1 = f'[{off_command_str}]\n'
    ser.write(off_command_str1.encode())

def on_closing():
    if messagebox.askyesno("Quit", "Do you want to QUIT the program?"):
        off_command = [0] * NUM_LEDS * 3
        off_command_str = ' '.join(str(c) for c in off_command)
        off_command_str1 = f'[{off_command_str}]\n'
        ser.write(off_command_str1.encode())
        ser.close()
        window.destroy()

def connect_serial():
    global ser
    port = port_combobox.get()
    baud_rate = 115200

    try:
        ser = serial.Serial(port, baud_rate)
        messagebox.showinfo("Success", "Serial connection established!")
    except serial.SerialException:
        messagebox.showerror("Error", "Failed to connect to the serial port.")


# Function to update the screen size
def update_screen_size():
    global screen_width, screen_height
    new_width = int(width_entry.get())
    new_height = int(height_entry.get())
    screen_width = new_width
    screen_height = new_height

    # Update the labels with the current values
    if (screen_width == 0):
        width_label.config(fg="red", text=f"Please select a valid Width: ")
    elif (screen_height == 0):
        height_label.config(fg="red", text=f"Please select a valid Height: ")
    else:
        width_label.config(fg="green", text=f"Selected Screen Width: {screen_width}")
        height_label.config(fg="green", text=f"Selected Screen Height: {screen_height}")

# Function to detect available serial ports and update the dropdown menu
def update_serial_ports():
    available_ports = [port.device for port in list_ports.comports()]
    port_combobox['values'] = available_ports

# Send brightness value to Arduino Uno
def send_brightness(brightness):
    # Send the brightness value to the Arduino
    if ser is None:
        ser.write(bytes([int(brightness)]))

# Create the GUI window
window = tk.Tk()
window.title("LED Control")
window.geometry("930x750")
window.configure(bg="light skyblue")

# icon = PhotoImage(file='Huawei-logo.png')
# window.iconphoto(True, icon)

# Serial port selection
port_label = Label(window, text="Select Serial Port: ")
port_label.pack()
port_combobox = Combobox(window)
port_combobox.pack(pady=5)

# Update the serial ports dropdown initially
update_serial_ports()

# Refresh button
refresh_button = Button(window, font="Cambria", text="Refresh", bg="white", fg="blue", command=update_serial_ports)
refresh_button.pack(pady=5)

# Connect button
connect_button = Button(window, font="Cambria", text="Connect", bg="white", fg="green", command=connect_serial)
connect_button.pack(pady=10)


# Start button
start_button = tk.Button(window, font="Cambria", text="START", bg="white", fg="green", command=start_led)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(window, font="Cambria", text="STOP", bg="white", fg="red", command=stop_led)
stop_button.pack(pady=30)

# Create labels and entry fields for width and height
width_label = Label(window, text="Screen Width: ")
width_label.pack()
width_entry = Entry(window)
width_entry.pack(pady=5)

height_label = Label(window, text="Screen Height: ")
height_label.pack()
height_entry = Entry(window)
height_entry.pack(pady=5)

# Create a button to update the screen size
update_button = Button(window,  font="Cambria", text="Update Screen Size", fg="blue", command=update_screen_size)
update_button.pack(pady=10)

# Brightness level
brightness_label = tk.Label(window, font="Cambria", text="BRIGHTNESS  LEVEL", bg="white", fg="black")
brightness_label.pack(pady=40)

brightness_scale = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, bg="white", fg="blue", length=350, command=send_brightness)
brightness_scale.set(50)
brightness_scale.pack(pady=2)


# Continuously send color matrix with brightness
while True:
    # Check LED state and send color matrix if LED is on
    if led_state:

        # Capture screen and resize to LED strip resolution
        screen = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
        screen = screen.resize((NUM_LEDS, 1), resample=Image.BILINEAR)

        # Convert image to RGB values
        screen_array = np.array(screen)
        screen_array = screen_array.reshape((NUM_LEDS, 3))
        screen_array = screen_array.tolist()

        # Send RGB values to Arduino Uno
        pixel_str = ' '.join([f'{p[0]} {p[1]} {p[2]}' for p in screen_array])
        matrix_str = f'[{pixel_str}]'

        # Update the color matrix with the selected brightness
        brightness = int(brightness_scale.get())
        color_matrix_with_brightness = [brightness] + [int(x) for x in matrix_str.strip("[]").split()]

        matrix_str = ' '.join(str(c) for c in color_matrix_with_brightness)
        matrix_str1 = f'[{matrix_str}]\n'

        # Send the matrix string to the Arduino
        ser.write(matrix_str1.encode())
        #print(matrix_str1)

    # Update the GUI window
    window.update()
    window.protocol("WM_DELETE_WINDOW", on_closing)

