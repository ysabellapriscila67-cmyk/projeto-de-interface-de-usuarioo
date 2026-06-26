import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.title("Catálogo de Filmes")
janela.geometry("500x450")
janela.config(bg="#EAF2F8")

titulo = tk.Label(
    janela,
    text="Cadastro de Filmes",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8",
    fg="#1B4F72"
)
titulo.pack(pady=10)

tk.Label(
    janela,
    text="Nome do Filme",
    bg="#EAF2F8",
    font=("Arial", 11)
).pack()

entry_filme = tk.Entry(janela, width=35, font=("Arial", 11))
entry_filme.pack(pady=5)

tk.Label(
    janela,
    text="Gênero",
    bg="#EAF2F8",
    font=("Arial", 11)
).pack()

combo_genero = ttk.Combobox(
    janela,
    values=[
        "Ação",
        "Comédia",
        "Drama",
        "Terror",
        "Romance",
        "Ficção Científica"
    ],
    state="readonly",
    width=30
)

combo_genero.current(0)
combo_genero.pack(pady=5)

listbox = tk.Listbox(
    janela,
    width=45,
    height=10,
    font=("Arial", 11)
)
listbox.pack(pady=15)

def adicionar():
    filme = entry_filme.get()

    if filme == "":
        messagebox.showwarning(
            "Aviso",
            "Digite o nome do filme!"
        )
        return

    genero = combo_genero.get()

    listbox.insert(
        tk.END,
        f"{filme} - {genero}"
    )

    entry_filme.delete(0, tk.END)

def remover():
    try:
        indice = listbox.curselection()[0]
        listbox.delete(indice)
    except:
        messagebox.showwarning(
            "Aviso",
            "Selecione um filme."
        )

def limpar():
    listbox.delete(0, tk.END)

frame = tk.Frame(janela, bg="#EAF2F8")
frame.pack()

tk.Button(
    frame,
    text="Adicionar",
    command=adicionar,
    bg="#2ECC71",
    fg="white",
    width=12
).grid(row=0, column=0, padx=5)

tk.Button(
    frame,
    text="Remover",
    command=remover,
    bg="#E74C3C",
    fg="white",
    width=12
).grid(row=0, column=1, padx=5)

tk.Button(
    frame,
    text="Limpar",
    command=limpar,
    bg="#3498DB",
    fg="white",
    width=12
).grid(row=0, column=2, padx=5)

janela.mainloop()