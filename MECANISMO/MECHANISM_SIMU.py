import serial
import time
import platform
print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

def menuSup():
    while True:
        print("1| ARRIBA")
        print("2| ABAJO")
        opcion = int(input("Seleccione : "))
        if(opcion == 1):
            motorSuperior(1,"A")
        elif(opcion == 2):
            motorSuperior(1,"H")
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")

def menuInf():
    while True:
        print("1| IZQUIERDA")
        print("2| DERECHA")
        opcion = int(input("Seleccione : "))
        if(opcion == 1):
            motorInferior(1,"H")
        elif(opcion == 2):
            motorSuperior(1,"A")
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")


def menu():
    while True:
        print("1 |COMENZAR ESCANEO 10X10")
        print("2 |MOVER MOTOR SUPERIOR")
        print("3 |MOVER MOTOR INFERIOR")
        opcion = int(input("Selecciona: "))
        if(opcion == 1):
            pass
            
        elif(opcion == 2):
            menuSup()
        elif(opcion == 3):
            menuInf()               
        elif(opcion == 0):
            break
        else:
            print("INVALID OPTION")


def motorSuperior(inputPasos,inputDireccion):
    if(inputPasos >= 1):
        if inputDireccion.upper() == "H":
            print(">")
            for i in range(inputPasos):               
                time.sleep(0.1)
                arduino.write(b'4')              
        elif inputDireccion.upper() == "A":
            print("<")
            for i in range(inputPasos):                
                time.sleep(0.1)
                arduino.write(b'5')
        elif inputDireccion.upper() == "S":
            #print("FINALIZADO")
            arduino.close()  # CERRANDO PUERTO
        else:
            print("WRONG")
            #menu()
    else:
        print("CANTIDAD DE PASOS INVALIDA")

def motorInferior(inputPasos,inputDireccion):
    if(inputPasos >= 1):
        if inputDireccion.upper() == "H":
            print(">")
            for i in range(inputPasos):               
                time.sleep(0.1)
                arduino.write(b'4')
        elif inputDireccion.upper() == "A":
            print("<")
            for i in range(inputPasos):                
                time.sleep(0.1)
                arduino.write(b'5')
        elif inputDireccion.upper() == "S":
            #print("FINALIZADO")
            arduino.close()  # CERRANDO PUERTO
        else:
            print("WRONG")
            #menu()
    else:
        print("CANTIDAD DE PASOS INVALIDA")
        


try:
    # Define the serial port and baud rate.
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)  # wait for the serial connection to initialize
    print("CONEXION AL ARDUINO EXITOSA")
    menu()
except:
    print("ERROR NO ARDUINO DETECTADO")
