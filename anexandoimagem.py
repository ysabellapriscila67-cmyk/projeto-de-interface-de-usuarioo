import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("Anexando Imagem")
janela.geometry("500x500")

try:
   
    imagem_original = Image.open("C:/Users/Aluno/Pictures/illustration-c15d49043e4645a889a8fc017199099c.png")
    imagem_redimensionada = imagem_original.resize((300, 300))
    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)

    #Criando um rótulo (Label) para exibir a imagem

    rotulo_imagem = tk.Label(janela, image=imagem_tk)
    rotulo_imagem.pack(pady=20)

except FileNotFoundError:
     
     avise_erro = tk.Label(janela, text="Erro: Imagem não encontrada!\nVerifique o caminho da imagem.", fg="red")
     avise_erro.pack(pady=20)

janela.mainloop()
