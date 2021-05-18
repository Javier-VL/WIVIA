import time
import socket
import threading
import platform
import os
import numpy as np

#SE CONECTA POR UDP Y OBTIENE UN VALOR DE SEÑAL CADA 250mls

print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

#DILE DEPENDENCIES
directorio_padre ="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/DATA1/"
file_name ="ONESTEP.txt"
#-------------------------------

#UDP DEPENDENCIES
FORMAT ='utf-8'
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.29"
ADDRESS =(SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER,PORT))
print(SERVER)
#-------------------------

TIMEOUT = 0.25

pixel_list = []
pixel =255

#------------------------

def getRGBfromlist(pixel_list):
    templist= np.array_split(pixel_list,3)

    pixel_R =[]
    pixel_G =[]
    pixel_B =[]
    rgb = []

    for x in range (0,3,1):
        if(x==0):
            pixel_R = templist[0]
        elif (x==1):
            pixel_G = templist[1]
        elif (x==2):
            pixel_B = templist[2]
    
    rgb.append(promedio(pixel_R))        

    rgb.append(promedio(pixel_G))       

    rgb.append(promedio(pixel_B))           
            
    return rgb

    

def writeFreq(data):
    ruta = directorio_padre+file_name
    with open(ruta,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write(str(data)+"|")

def promedio(lista):
    average = sum(lista)/len(lista)
    average = round(average,0)
    return int(average)


def getFreq(conn,addr,timeout):#esta funcion toma alrededor de 3milisegundos
    cont=1
    lista = []

    time_start = time.time()#Comenzando contador
    while time.time() < time_start + timeout:#Recibir data por los 250milisigundos
        databyte = conn.recv(1024)
        datalist = list(databyte)
        #print(datalist)
        pixel_list.append(promedio(datalist))
        lista.append(promedio(datalist))


        cont+=1

    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    pixel = promedio(pixel_list)
    rgb = getRGBfromlist(pixel_list)
    print(f"VALOR EN RGB {rgb}")
    print("---------------------")



start_time = time.time()


for x in range(0,5,1):
    getFreq(sock,ADDRESS,TIMEOUT)
    pass

#getFreq(sock,ADDRESS,TIMEOUT)

print("finalizo...")
print("--- %s seconds ---" % (time.time() - start_time))
print(len(pixel_list))
