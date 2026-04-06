import tkinter as tk
from tkinter import messagebox

class BoobleClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Booble Messenger v1.0")
        self.root.geometry("400x500")
        self.root.configure(bg="#1a1a1a") # Темний хай-тек фон

        # Заголовок
        self.label = tk.Label(root, text="BOOBLE", fg="#00ffcc", bg="#1a1a1a", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Поле для вводу тексту
        self.entry = tk.Entry(root, bg="#333333", fg="white", insertbackground="white", width=30)
        self.entry.pack(pady=10)

        # Кнопка відправки
        self.send_btn = tk.Button(root, text="ВІДПРАВИТИ", command=self.send_msg, bg="#00ffcc", fg="black")
        self.send_btn.pack(pady=10)

    def send_msg(self):
        msg = self.entry.get()
        if msg:
            messagebox.showinfo("Booble", f"Повідомлення '{msg}' зашифровано та готове до відправки!")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BoobleClient(root)
    root.mainloop()
