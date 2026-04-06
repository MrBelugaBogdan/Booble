class BoobleCipher:
    def __init__(self, key=123):
        self.key = key  # Твій секретний цифровий ключ

    def encrypt(self, text):
        """Шифрує текст через XOR (швидко і надійно для слабкого заліза)"""
        return "".join(chr(ord(c) ^ self.key) for c in text)

    def decrypt(self, encrypted_text):
        """Розшифровує повідомлення назад"""
        return self.encrypt(encrypted_text) # В XOR ключ працює в обидва боки
