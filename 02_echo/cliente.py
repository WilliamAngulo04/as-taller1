#Cliente
import socket

# Crear un socket TCP/IP
HOST = 'localhost'
PORT = 9008

mensaje = input("Ingrese un mensaje para enviar al servidor: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT)) # Conectar al servidor

cliente.sendall(mensaje.encode()) # Enviar datos al servidor (debe ser binario "b")
print(f"Mensaje enviado: '{mensaje}'")

respuesta = cliente.recv(1024) # Recibir datos del servidor (máximo 1024 bytes)
print(f"Respuesta del 'Echo': {respuesta.decode()}") # Imprimir la respuesta del servidor

cliente.close() # Cerrar la conexión