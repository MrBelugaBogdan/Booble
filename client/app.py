import tkinter as tk
from tkinter import messagebox

class BoobleAuth:
    def __init__(self, root):
        self.root = root
        self.root.title("Booble v1.0 - Авторизація")
        self.root.geometry("300x400")
        self.root.configure(bg="#0a0a0a")

        # Логотип
        tk.Label(root, text="B", fg="#00ffcc", bg="#0a0a0a", font=("Arial", 60, "bold")).pack(pady=30)
        tk.Label(root, text="Введіть ваш ключ Booble", fg="white", bg="#0a0a0a").pack()

        # Поле для пароля (ключа)
        self.key_entry = tk.Entry(root, show="*", bg="#1a1a1a", fg="#00ffcc", borderwidth=0, insertbackground="white")
        self.key_entry.pack(pady=10, ipady=5)

        # Кнопка входу
        tk.Button(root, text="УВІЙТИ", command=self.check_auth, bg="#00ffcc", fg="black", width=15).pack(pady=20)

    def check_auth(self):
        # Наш секретний ключ (можеш змінити на свій)
        if self.key_entry.get() == "1234":
            self.root.destroy() # Закриваємо вікно входу
            self.open_main_chat() # Відкриваємо чат
        else:
            messagebox.showerror("Помилка", "Невірний ключ доступу!")

    def open_main_chat(self):
        main_root = tk.Tk()
        # Тут буде код нашого головного чату, який ми писали раніше
        print("Вхід дозволено!")
        main_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = BoobleAuth(root)
    root.mainloop()
