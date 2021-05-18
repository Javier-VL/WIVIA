import time
import socket
import threading
import platform


print("\nTRABAJANDO CON PYTHON: ", platform.python_version())

FORMAT ='utf-8'
PORT = 9000
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.0.29"
server_address = (SERVER, PORT)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)



print(f"starting up on {SERVER} port {PORT}")

def handle_client(conn,addr):
    #print(f"[NUEVA CONEXION] {addr} CONECTADA.")
    
    connected = True

    while connected:
        data = conn.recv(1024)
        print(f"{data}")
        time.sleep(1000)

    conn.close()


try:
    print(f"[ESCUCHANDO] Server esta escuchando en... {SERVER}")
    while True:
        #print('\nwaiting to receive message')
        #data, address = sock.recvfrom(1024)   

        #print(f"received {len(data)} bytes from {address}")
        #print(type(data))
        #msg = data.decode(FORMAT)
        #print(msg)
        #time.sleep(4)

        #conn, addr = sock.accept()#Espera a una conexion nueva en el server
        hilo = threading.Thread(target=handle_client, args=(sock,server_address))
        hilo.start()
        print(f"[CONEXIONES ACTIVAS] {threading.activeCount() -1}")

except KeyboardInterrupt:
    print("CTRL+C EXIT")
    pass



