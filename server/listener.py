import socket

def booble_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999)) # Порт нашого месенджера
    server.listen(10)
    print("--- BOOBLE NETWORK ONLINE ---")

    while True:
        conn, addr = server.accept()
        print(f"Нове з'єднання: {addr}")
        
        # Відправляємо вітання від Booble
        conn.send(b"BOOBLE_V1_READY")
        conn.close()

if __name__ == "__main__":
    booble_server()
