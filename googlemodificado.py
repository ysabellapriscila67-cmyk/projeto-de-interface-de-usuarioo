import tkinter as tk
from tkinter import ttk

class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lil Peep Search")
        self.geometry("800x600")
        self.configure(bg="#1a001f")
        self.minsize(400, 300)

        title_font = ("Segoe Script", 56, "bold")
        entry_font = ("Consolas", 14)
        button_font = ("Montserrat", 11, "bold")
        footer_font = ("Georgia", 12, "italic")

        # Container principal
        main_frame = tk.Frame(self, bg="#1a001f")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_frame = tk.Frame(main_frame, bg="#1a001f")
        title_frame.pack(pady=(0, 30))

        # Cores estética Lil Peep
        colors = [
            "#ff66c4",
            "#d291ff",
            "#ff99cc",
            "#c77dff",
            "#ff4fa3",
            "#b5179e",
            "#ff66c4",
            "#d291ff"
        ]

        text = "Lil Peep"

        for i, char in enumerate(text):
            tk.Label(
                title_frame,
                text=char,
                font=title_font,
                fg=colors[i % len(colors)],
                bg="#1a001f"
            ).pack(side="left")

        search_frame = tk.Frame(
            main_frame,
            bg="#2b0a3d",
            bd=0,
            highlightbackground="#ff66c4",
            highlightthickness=2
        )
        search_frame.pack(ipadx=10, ipady=6, fill="x")

        # Ícone esquerda
        search_icon = tk.Label(
            search_frame,
            text="🖤",
            bg="#2b0a3d",
            font=("Segoe UI Emoji", 16),
            fg="#ff99cc"
        )
        search_icon.pack(side="left", padx=(10, 5))

        # Placeholder
        self.placeholder_text = "search your sadness..."
        self.search_var = tk.StringVar()

        # Entrada
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=entry_font,
            width=50,
            bd=0,
            bg="#2b0a3d",
            fg="#aaaaaa",
            insertbackground="#ffffff",
            highlightthickness=0
        )

        self.search_entry.pack(side="left", padx=5, pady=8)
        self.search_entry.insert(0, self.placeholder_text)

        # Ícone direita
        mic_icon = tk.Label(
            search_frame,
            text="☁",
            bg="#2b0a3d",
            font=("Segoe UI Emoji", 16),
            fg="#ff66c4"
        )
        mic_icon.pack(side="right", padx=(5, 10))

        # Eventos
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        buttons_frame = tk.Frame(main_frame, bg="#1a001f")
        buttons_frame.pack(pady=30)

        search_button = tk.Button(
            buttons_frame,
            text="Cry Search",
            font=button_font,
            bg="#ff66c4",
            fg="white",
            relief="flat",
            activebackground="#ff99cc",
            activeforeground="white",
            padx=25,
            pady=12,
            cursor="hand2",
            command=self.perform_search
        )
        search_button.pack(side="left", padx=10)

        feeling_lucky_button = tk.Button(
            buttons_frame,
            text="Save That Shit",
            font=button_font,
            bg="#7b2cbf",
            fg="white",
            relief="flat",
            activebackground="#9d4edd",
            activeforeground="white",
            padx=25,
            pady=12,
            cursor="hand2"
        )
        feeling_lucky_button.pack(side="left", padx=10)

        footer = tk.Label(
            main_frame,
            text="✦ love now, cry later ✦",
            font=footer_font,
            fg="#ff99cc",
            bg="#1a001f"
        )
        footer.pack(pady=(10, 0))

    def on_entry_click(self, event):
        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="white")

    def on_focus_out(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="#aaaaaa")

    def perform_search(self, event=None):
        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"🖤 Searching for: {query}")

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()