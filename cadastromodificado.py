import tkinter as tk
from tkinter import ttk, messagebox

class ConcursoLilPeep(tk.Tk):
    def __init__(self):
        super().__init__()

        # CONFIGURAÇÃO DA JANELA
        self.title("Concurso VIP - Lil Peep")
        self.geometry("900x650")
        self.configure(bg="#0A0A0A")
        self.resizable(False, False)

        # PALETA DARK / VAMPIRA
        self.bg_color = "#0A0A0A"          # Preto profundo
        self.secondary_bg = "#140B0B"     # Preto avermelhado
        self.fg_color = "#F5EDED"         # Branco suave
        self.accent_color = "#8B0000"     # Vermelho sangue
        self.hover_color = "#B22222"      # Vermelho vivo
        self.input_bg = "#1A1111"         # Fundo dos inputs
        self.border_color = "#3B1F1F"
        self.text_muted = "#C2A9A9"

        # Fonte estilo dark/vampiro
        self.main_font = ("Georgia", 13)
        self.title_font = ("Times New Roman", 34, "bold")
        self.small_font = ("Georgia", 11, "bold")

        # ESTILO DO COMBOBOX
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.input_bg,
            background=self.secondary_bg,
            foreground=self.fg_color,
            bordercolor=self.border_color,
            arrowcolor=self.accent_color,
            padding=6
        )

        self.create_widgets()

    def create_widgets(self):

        # ================= HEADER =================
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(40, 20))

        title = tk.Label(
            header_frame,
            text="L I L   P E E P",
            font=("Times New Roman", 18, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        title.pack()

        subtitle = tk.Label(
            header_frame,
            text="CONCURSO VIP",
            font=self.title_font,
            bg=self.bg_color,
            fg=self.fg_color
        )
        subtitle.pack()

        frase = tk.Label(
            header_frame,
            text="Concorra a um ingresso exclusivo para o show",
            font=("Georgia", 12, "italic"),
            bg=self.bg_color,
            fg=self.text_muted
        )
        frase.pack(pady=(5, 10))

        separator = tk.Frame(
            header_frame,
            bg=self.accent_color,
            height=2,
            width=160
        )
        separator.pack()

        # ================= FORMULÁRIO =================
        form_frame = tk.Frame(self, bg=self.bg_color)
        form_frame.pack(expand=True, fill="both", padx=100, pady=20)

        def create_input(parent, label_text, row, col, width=30):

            lbl = tk.Label(
                parent,
                text=label_text,
                font=self.small_font,
                bg=self.bg_color,
                fg=self.text_muted
            )
            lbl.grid(row=row, column=col, sticky="w", pady=(15, 0), padx=15)

            entry = tk.Entry(
                parent,
                font=self.main_font,
                bg=self.input_bg,
                fg=self.fg_color,
                insertbackground=self.accent_color,
                relief="flat",
                width=width,
                highlightthickness=1,
                highlightbackground=self.border_color,
                highlightcolor=self.accent_color
            )

            entry.grid(
                row=row + 1,
                column=col,
                sticky="we",
                pady=(5, 5),
                padx=15,
                ipady=10
            )

            return entry

        self.ent_nome = create_input(form_frame, "NOME COMPLETO", 0, 0, 35)
        self.ent_idade = create_input(form_frame, "IDADE", 0, 1, 15)

        self.ent_email = create_input(form_frame, "E-MAIL", 2, 0, 35)
        self.ent_instagram = create_input(form_frame, "@INSTAGRAM", 2, 1, 25)

        # Tipo de ingresso
        lbl_tipo = tk.Label(
            form_frame,
            text="TIPO DE INGRESSO",
            font=self.small_font,
            bg=self.bg_color,
            fg=self.text_muted
        )
        lbl_tipo.grid(row=4, column=0, sticky="w", pady=(15, 0), padx=15)

        self.combo_tipo = ttk.Combobox(
            form_frame,
            values=[
                "Pista",
                "VIP",
                "Backstage",
                "Meet & Greet"
            ],
            font=self.main_font,
            state="readonly"
        )

        self.combo_tipo.grid(
            row=5,
            column=0,
            sticky="we",
            pady=(5, 5),
            padx=15
        )

        self.combo_tipo.set("VIP")

        # Estilo do menu dropdown
        self.option_add('*TCombobox*Listbox.font', ("Georgia", 12))
        self.option_add('*TCombobox*Listbox.background', self.input_bg)
        self.option_add('*TCombobox*Listbox.foreground', self.fg_color)
        self.option_add('*TCombobox*Listbox.selectBackground', self.accent_color)
        self.option_add('*TCombobox*Listbox.selectForeground', "#FFFFFF")

        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # ================= BOTÃO =================
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=(20, 40))

        def on_enter(e):
            self.btn_cadastrar.config(
                bg=self.hover_color,
                fg="#FFFFFF"
            )

        def on_leave(e):
            self.btn_cadastrar.config(
                bg=self.accent_color,
                fg="#FFFFFF"
            )

        self.btn_cadastrar = tk.Button(
            btn_frame,
            text="ENTRAR NO CONCURSO",
            font=("Times New Roman", 14, "bold"),
            bg=self.accent_color,
            fg="#FFFFFF",
            activebackground=self.hover_color,
            activeforeground="#FFFFFF",
            relief="flat",
            cursor="hand2",
            command=self.cadastrar
        )

        self.btn_cadastrar.pack(ipady=14, ipadx=60)

        self.btn_cadastrar.bind("<Enter>", on_enter)
        self.btn_cadastrar.bind("<Leave>", on_leave)

        # STATUS
        self.status_lbl = tk.Label(
            self,
            text="",
            font=("Georgia", 11),
            bg=self.bg_color,
            fg=self.accent_color
        )

        self.status_lbl.pack(pady=(10, 0))

    # ================= CADASTRO =================
    def cadastrar(self):

        nome = self.ent_nome.get()
        idade = self.ent_idade.get()
        email = self.ent_email.get()

        if not nome or not idade or not email:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos obrigatórios!",
                parent=self
            )
            return

        self.status_lbl.config(
            text="Enviando inscrição...",
            fg=self.fg_color
        )

        self.update()
        self.after(700)

        self.status_lbl.config(
            text=f"✓ {nome.split()[0]}, sua inscrição foi enviada.",
            fg=self.accent_color
        )

        # Limpar campos
        self.ent_nome.delete(0, tk.END)
        self.ent_idade.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_instagram.delete(0, tk.END)

        self.combo_tipo.set("VIP")

        self.ent_nome.focus()


if __name__ == "__main__":
    app = ConcursoLilPeep()
    app.mainloop()