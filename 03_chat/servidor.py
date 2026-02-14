# Servidor
import socket
import threading

# Crear un socket TCP/IP
HOST = 'localhost' 
PORT = 9008

clientes = []

def atender_cliente(cliente, nombre):
    while True:
        try:
            mensaje = cliente.recv(1024) # Recibir datos del cliente (máximo 1024 bytes)
            if not mensaje:
                break
            print(f"{nombre}: {mensaje.decode()}") # Imprimir el mensaje recibido del cliente
            # Enviar el mensaje a todos los demás clientes conectados
            broadcast(mensaje.decode(), cliente)
        except ConnectionResetError:
            clientes.remove(cliente)
            cliente.close()
            print(f"{nombre} se ha desconectado.")
            break

def broadcast(mensaje, emisor):
    for cliente in clientes:
        if cliente != emisor:
            cliente.sendall(mensaje.encode()) # Enviar el mensaje a los demás clientes

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT)) # Asociar el socket a la dirección y puerto
servidor.listen() # Escuchar conexiones entrantes
print("El servidor 'chat' está esperando conexión...")

while True:

    # Aceptar una conexión
    cliente, direccion = servidor.accept()
    print(f'Conexión establecida desde {direccion}') # Imprimir la dirección del cliente
    nombre = cliente.recv(1024).decode() # Recibir el nombre del cliente
    clientes.append(cliente) # Agregar el cliente a la lista de clientes conectados
    broadcast(f"{nombre} se ha unido al chat.", cliente) # Informar a los demás clientes que alguien se ha unido
    hilo_cliente = threading.Thread(target=atender_cliente, args=(cliente, nombre)) # Crear un hilo para atender al cliente
    hilo_cliente.start() # Iniciar el hilo para atender al cliente

cliente.close()