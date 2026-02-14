# Cliente
import socket

# Crear un socket TCP/IP
HOST = 'localhost'
PORT = 9000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT)) # Conectar al servidor

cliente.sendall(b"Mundo!") # Enviar datos al servidor (debe ser binario "b")
respuesta = cliente.recv(1024) # Recibir datos del servidor (máximo 1024 bytes)
print(f"Respuesta del servidor: {respuesta.decode()}") # Imprimir la respuesta del servidor


cliente.close() # Cerrar la conexión