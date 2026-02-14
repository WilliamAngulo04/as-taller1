# Servidor
import socket

# Crear un socket TCP/IP
HOST = 'localhost' 
PORT = 9008

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT)) # Asociar el socket a la dirección y puerto
servidor.listen() # Escuchar conexiones entrantes

while True:

    print('Esperando conexión...')

    # Aceptar una conexión
    cliente, direccion = servidor.accept()
    print(f'Conexión establecida desde {direccion}') # Imprimir la dirección del cliente

    # los datos que se envían y reciben a través de sockets deben ser binarios, no strings
    datos = cliente.recv(1024) # Recibir datos del cliente (máximo 1024 bytes)

    if not datos:
        break

    print(f"Datos recibidos: ", datos) # Imprimir los datos recibidos del cliente
    cliente.sendall(datos) # debe ser binario "b", no string
    cliente.close()