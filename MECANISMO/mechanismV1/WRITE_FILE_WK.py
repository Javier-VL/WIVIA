import time
import socket
import threading
import platform
import os

#1280v X 720h
#1280folders con 720 archivos cada uno |2764800 archivos 3mls por cada uno, para un total de 46min

cont_hrz = 0 #<=720
cont_vtl = 0 #<=1280

print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

directorio = "VERTICAL_V_"
directorio_padre ="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/DATA1/"
file_name ="test2.txt"

path = os.path.join(directorio_padre,directorio)#DEFINIENDO LA RUTA

try:
    os.mkdir(path)#CREANDO LA RUTA
except:
    print("FILE ERROR, DIRECTORY ALREADY EXISTS")
    pass
ruta = directorio_padre+file_name


with open(ruta,'w') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
    f.write("testaaaaa")


with open(ruta,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
    f.write("2")
