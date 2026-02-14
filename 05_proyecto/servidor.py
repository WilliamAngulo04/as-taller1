import socket
import urllib.parse

HOST = '127.0.0.1'
PORT = 9000
historial_chat = []

def generar_html_mensajes():
    if not historial_chat:
        return "<p style='color:#ccc; text-align:center;'>No hay mensajes aún...</p>"
    return "".join([f"<div class='msg'><b>{m['user']}:</b> {m['text']}</div>" for m in historial_chat])

def iniciar_insta_chat():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f">>> Insta Chat activo en http://{HOST}:{PORT}")

    while True:
        conn, addr = sock.accept()
        try:
            peticion = conn.recv(2048).decode('utf-8')
            if not peticion: continue
            
            linea = peticion.split('\n')[0]
            ruta = linea.split(' ')[1]
            url_p = urllib.parse.urlparse(ruta)
            params = urllib.parse.parse_qs(url_p.query)

            # 1. Manejo de actualización de mensajes (AJAX)
            if url_p.path == "/update":
                cuerpo = generar_html_mensajes()
                header = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
            
            # 2. Manejo de envío de nuevo mensaje
            elif 'msg' in params and 'user' in params:
                historial_chat.append({"user": params['user'][0], "text": params['msg'][0]})
                cuerpo = "OK"
                header = "HTTP/1.1 200 OK\r\n\r\n"

            # 3. Carga inicial de la página
            else:
                with open("index.html", "r", encoding="utf-8") as f:
                    html = f.read()
                
                usuario = params.get('user', [''])[0]
                # Si no hay usuario, forzamos vista de login
                if not usuario:
                    html = html.replace("{{SHOW_LOGIN}}", "flex").replace("{{SHOW_CHAT}}", "none")
                else:
                    html = html.replace("{{SHOW_LOGIN}}", "none").replace("{{SHOW_CHAT}}", "block")
                
                html = html.replace("{{USER_NAME}}", usuario)
                html = html.replace("{{MESSAGES}}", generar_html_mensajes())
                cuerpo = html
                header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

            conn.sendall((header + cuerpo).encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    iniciar_insta_chat()