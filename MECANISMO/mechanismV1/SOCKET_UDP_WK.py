import time
import socket
import threading
import platform


print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

#UDP DEPENDENCIES
FORMAT ='utf-8'
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.29"
ADDRESS =(SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER,PORT))
#--

TIMEOUT = 0.25


def getFreq(conn,addr,timeout):#esta funcion toma alrededor de 3milisegundos
    cont = 1
    time_start = time.time()
    while time.time() <= time_start + timeout:#Repitiendo 250mls
        data = conn.recv(1024)
        print(type(data))
        print(f"{cont} || [{addr}] | {type(data)}")
        a =list(data)
        for x in range(len(a)):
            print (a[x],"|", end = ''),
            pass
        print (f"{cont} | Paquete")
            
        cont+=1
        

    print(f"{cont}|FINALIZO EN: ")
    print("--- %s seconds ---" % (time.time() - time_start))
    print("---------------------")


start_time = time.time()


for x in range(0,30,1):
    getFreq(sock,ADDRESS,TIMEOUT)
#   pass

#getFreq(sock,ADDRESS,TIMEOUT)

print("finalizo...")
print("--- %s seconds ---" % (time.time() - start_time))