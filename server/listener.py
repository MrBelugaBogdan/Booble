import socket

def start_booble_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("--- BOOBLE SERVER RUNNING ---")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024)
        
        # Перевіряємо, чи це наш протокол
        if data.startswith(b"BOOB"):
            content = data[4:].decode('utf-8') # Відрізаємо заголовок "BOOB"
            print(f"[{addr}] Каже: {content}")
        
        conn.close()

if __name__ == "__main__":
    start_booble_server()
