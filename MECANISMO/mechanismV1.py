import serial
import time
import platform
print("\nTRABAJANDO CON PYTHON: ", platform.python_version())


def moveOneStep():
    inputDireccion = input("\n Horario o Antihorario: H/A ")
    inputPasos = int(input("Cantidad de pasos: "))

    if(inputPasos >= 1):
        if inputDireccion.upper() == "H":
            print(">")
            for i in range(inputPasos):               
                time.sleep(0.1)
                arduino.write(b'H')
                moveOneStep()
                

        elif inputDireccion.upper() == "A":
            print("<")
            for i in range(inputPasos):                
                time.sleep(0.1)
                arduino.write(b'A')
                moveOneStep()

        elif inputDireccion.upper() == "S":
            print("FINALIZADO")
            arduino.close()  # CERRANDO PUERTO
        else:
            print("WRONG")
            moveOneStep()

    else:
        print("CANTIDAD DE PASOS INVALIDA")


try:
    # Define the serial port and baud rate.
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)  # wait for the serial connection to initialize
    moveOneStep()
except:
    print("ERROR NO ARDUINO DETECTADO")
