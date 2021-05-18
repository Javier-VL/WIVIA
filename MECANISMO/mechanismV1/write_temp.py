import time
import socket
import threading
import platform
import os

#1280v X 720h
#1280folders con 720 archivos cada uno |2764800 archivos 3mls por cada uno, para un total de 46min

#CREAR RUTA>CREAR ARCHIVOS

cont_hrz = 0 #<=720
cont_vtl = 0 #<=1280

print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

directorio = "VERTICAL_V_"
directorio_padre ="C:/Users/Javier/Documents/INCO\MODULAR/MECANISMO/CODIGO/WIVIA/FILES/DATA2/"


def createColumn(cont_vtl):#CREA FOLDER DONDE SERAN ALMACENADOS LOS ARCHIVOS DE ESE VECTOR
    
    while True:        
        if(cont_vtl<=5):#SERA 1289
            path = os.path.join(directorio_padre,directorio+str(cont_vtl))#DEFINIENDO LA RUTA        
            try:
                os.mkdir(path)
                time.sleep(1)
                while True:
                    global cont_hrz 
                    cont_hrz= createFile(cont_hrz,directorio+str(cont_vtl))#CREANDO LOS ARCHIVOS
                   
                    if(cont_hrz==10):
                        print(f"valor{cont_hrz}")
                        break         
                cont_vtl+=1
            except:
                print("ERROR,PATH ALREADY EXISTS")
               
        elif(cont_vtl>=5):
            print(f"valor{cont_vtl}")
            break
        print(f"valor{cont_vtl}")
        return cont_vtl

def createFile(cont_hrz,folder):
    file_name = "/freq_"+str(cont_hrz)+".txt"
    ruta = directorio_padre+folder+file_name

    with open(ruta,'w') as f:#SOLO ESTA ABIERTO DENTRO DE LA FUNCION
        f.write("testaaaaa")
    cont_hrz+=1
    return cont_hrz

cont_vtl = createColumn(cont_vtl)

print(f"Terminado, creadas {cont_vtl} carpetas, y {cont_hrz} archivos")



#notes
#accidentalmente cree 53mil archivos