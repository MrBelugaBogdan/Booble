import tkinter as tk

class BooblePro:
    def __init__(self, root):
        self.root = root
        self.root.title("Booble v1.0 - High Tech Messenger")
        self.root.geometry("800x500")
        self.root.configure(bg="#0f0f0f") # Глибокий чорний колір

        # ЛІВА ПАНЕЛЬ (Список чатів)
        self.side_bar = tk.Frame(root, bg="#1a1a1a", width=250)
        self.side_bar.pack(side="left", fill="y")
        
        tk.Label(self.side_bar, text="ЧАТИ", fg="#00ffcc", bg="#1a1a1a", font=("Segoe UI", 12, "bold")).pack(pady=10)
        
        # Заглушки під чати (для вигляду)
        for name in ["Брат Артем", "Проєкт DoNet", "Адмін Booble"]:
            btn = tk.Button(self.side_bar, text=name, bg="#252525", fg="white", relief="flat", anchor="w")
            btn.pack(fill="x", padx=5, pady=2)

        # ПРАВА ПАНЕЛЬ (Вікно переписки)
        self.main_chat = tk.Frame(root, bg="#0f0f0f")
        self.main_chat.pack(side="right", expand=True, fill="both")

        # Поле з повідомленнями
        self.chat_display = tk.Text(self.main_chat, bg="#0f0f0f", fg="#e0e0e0", state="disabled", borderwidth=0)
        self.chat_display.pack(expand=True, fill="both", padx=10, pady=10)

        # ПОЛЕ ВВОДУ (Внизу)
        self.input_area = tk.Frame(self.main_chat, bg="#1a1a1a", height=60)
        self.input_area.pack(side="bottom", fill="x")

        self.msg_entry = tk.Entry(self.input_area, bg="#333333", fg="white", borderwidth=0)
        self.msg_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        self.send_btn = tk.Button(self.input_area, text="➤", bg="#00ffcc", fg="black", width=5)
        self.send_btn.pack(side="right", padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BooblePro(root)
    root.mainloop()
