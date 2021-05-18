import serial
import time
import sys
 
# Define the serial port and baud rate.
#git pull origin main

arduino = serial.Serial('COM3', 9600)


print("TRABAJANDO EN PYTHON: ",sys.version)
time.sleep(2)


def moveOneStep():
    user_input = input("\n Derecha o Izquierda: ")
    
    if user_input =="D":
        print(">")
        time.sleep(0.1) 
        arduino.write(b'D') 
        moveOneStep()
    elif user_input =="I":
        print("<")
        time.sleep(0.1) 
        arduino.write(b'I') 
        moveOneStep()
    elif user_input =="S":
        print("FINALIZADO")
        arduino.close()#CERRANDO PUERTO
    else:
        print("WRONG")
        moveOneStep()

time.sleep(2) # wait for the serial connection to initialize
moveOneStep()

