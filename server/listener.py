import socket

def start_server():
    # Створюємо "вухо" сервера
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080)) # Порт 8080 для Booble
    server.listen(5)
    
    print("--- BOOBLE SERVER ONLINE ---")
    print("Очікування підключень...")

    while True:
        client, address = server.accept()
        print(f"Підключено: {address}")
        data = client.recv(1024)
        if data:
            print(f"Отримано пакет BBP: {data}")
        client.close()

if __name__ == "__main__":
    start_server()
