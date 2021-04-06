import serial
import time
import sys
 
# Define the serial port and baud rate.
ser = serial.Serial('COM3', 9600)

print("TRABAJANDO EN PYTHON: ",sys.version)