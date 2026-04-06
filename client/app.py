import socket

def send_to_server(message):
    try:
        # Створюємо з'єднання з твоїм сервером
        # 'localhost' - це твій комп'ютер, але потім тут буде IP твого сервера
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 9999)) 
        
        # Пакуємо в Booble Binary Protocol (BBP)
        # HEADER "BOOB" + MESSAGE
        packet = b"BOOB" + message.encode('utf-8')
        
        client.send(packet)
        client.close()
        return True
    except:
        print("Помилка з'єднання!")
        return False
