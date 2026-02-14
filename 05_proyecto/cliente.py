import socket

HOST = '127.0.0.1'
PORT = 9000

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("[CONECTADO] Conexión establecida con Fix Manager Server.")
        
        while True:
            msg = input("Mensaje (o 'salir' para terminar): ")
            if msg.lower() == 'salir':
                break
            
            client.send(msg.encode('utf-8'))
            
            # Recibir respuesta del servidor
            respuesta = client.recv(1024).decode('utf-8')
            print(f"Servidor: {respuesta}")
            
    except ConnectionRefusedError:
        print("[ERROR] No se pudo conectar. ¿Está el servidor encendido?")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()