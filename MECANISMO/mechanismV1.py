import serial
import time
import platform
print("\nTRABAJANDO CON PYTHON: ", platform.python_version())


def menu():
    while True:
        opcion = int(input("Seleccione el motor a utilizar 1 o 2: "))
        if(opcion == 1):
            moveOneStep(1)
        elif(opcion == 2):
            moveOneStep(2)
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")




def moveOneStep(motor):
    inputDireccion = input("\n Horario o Antihorario: H/A ")
    inputPasos = int(input("Cantidad de pasos: "))

    if(motor == 1):
        #MOTOR1
        if(inputPasos >= 1):
            if inputDireccion.upper() == "H":
                print(">")
                for i in range(inputPasos):               
                    time.sleep(0.1)
                    arduino.write(b'4')
                    menu()
            elif inputDireccion.upper() == "A":
                print("<")
                for i in range(inputPasos):                
                    time.sleep(0.1)
                    arduino.write(b'5')
                    menu()

            elif inputDireccion.upper() == "S":
                print("FINALIZADO")
                arduino.close()  # CERRANDO PUERTO
            else:
                print("WRONG")
                menu()
        else:
            print("CANTIDAD DE PASOS INVALIDA")
        
    elif(motor ==2):
        if(inputPasos >= 1):
            if inputDireccion.upper() == "H":
                print(">")
                for i in range(inputPasos):               
                    time.sleep(0.1)
                    arduino.write(b'8')
                    menu()
            elif inputDireccion.upper() == "A":
                print("<")
                for i in range(inputPasos):                
                    time.sleep(0.1)
                    arduino.write(b'9')
                    menu()

            elif inputDireccion.upper() == "S":
                print("FINALIZADO")
                arduino.close()  # CERRANDO PUERTO
            else:
                print("WRONG")
                menu()
        else:
            print("CANTIDAD DE PASOS INVALIDA")
    else:
        menu()




try:
    # Define the serial port and baud rate.
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)  # wait for the serial connection to initialize
    menu()
except:
    print("ERROR NO ARDUINO DETECTADO")
