# Cliente
import socket
import threading

# Crear un socket TCP/IP
HOST = 'localhost'
PORT = 9008

def recibir_mensajes(cliente):
    while True:
        mensaje = cliente.recv(1024).decode() # Recibir mensajes del servidor (máximo 1024 bytes)
        print(mensaje)

nombre = input("Ingrese su nombre: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT)) # Conectar al servidor
cliente.sendall(nombre.encode()) # Enviar el nombre del cliente al servidor (debe ser binario "b")

hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,)) # Crear un hilo para recibir mensajes del servidor
hilo_recibir.start() # Iniciar el hilo para recibir mensajes del servidor

while True:
    mensaje = input("Mensaje: ")
    cliente.send(mensaje.encode()) # Enviar el mensaje al servidor
     
cliente.sendall(b"Mundo!") # Enviar datos al servidor
respuesta = cliente.recv(1024) # Recibir datos del servidor (máximo 1024 bytes)
print(f"Respuesta del servidor: {respuesta.decode()}") # Imprimir la respuesta del servidor

cliente.close() # Cerrar la conexión