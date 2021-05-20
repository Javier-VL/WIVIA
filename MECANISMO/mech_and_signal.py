import time
import socket
import threading
import platform
import os
import os.path
from os import path
from pathlib import Path

print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

#|FILE HANDLER

directorio = "f"
directorio_padre ="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/"
file_name ="scan-argb-values.txt"

path = os.path.join(directorio_padre,directorio)#DEFINIENDO LA RUTA

ruta = directorio_padre+file_name


try:
    os.mkdir(path)#CREANDO LA RUTA
except:
    print("this ROUTE ALREADY EXIST")
    pass

#VERIFICANDO QUE EL ARCHIVO EXISTA Y NO SOBRE ESCRIBA
my_file = Path(ruta)

for x in range(5):
    if my_file.is_file():
        with open(ruta,'a+') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
            f.write("255,255\n")
    else:
        with open(ruta,'w') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
            f.write("720\n")
            f.write("480\n")
    


    



