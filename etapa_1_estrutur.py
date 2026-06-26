import tkinter as tk

def principal():
    # Inicializa a janela principal do Tkinter
    janela_principal = tk.Tk()
    janela_principal.title("NovaMarket - Login (Etapa 1)")
    
    # Define o tamanho da janela e impede o redimensionamento para manter o layout perfeito
    largura_janela = 900
    altura_janela = 550
    janela_principal.resizable(False, False)
    
    # Centraliza a janela na tela do usuário
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()
    posicao_x = (largura_tela - largura_janela) // 2
    posicao_y = (altura_tela - altura_janela) // 2
    janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    
    # Define a cor de fundo da janela principal
    janela_principal.configure(bg="#0a0f1d")  # Azul escuro profundo
    
    # --- Painel Esquerdo (Espaço para Ilustração) ---
    # Largura de 450px (metade de 900px), cobrindo toda a altura (550px)
    painel_esquerdo = tk.Frame(janela_principal, width=450, height=550, bg="#0a0f1d", bd=0, highlightthickness=0)
    painel_esquerdo.pack(side="left", fill="both", expand=True)
    # Impede que o frame mude de tamanho de acordo com seus elementos internos
    painel_esquerdo.pack_propagate(False)
    
    # Adicionamos um rótulo temporário apenas para identificar o painel esquerdo
    marcador_esquerdo = tk.Label(
        painel_esquerdo, 
        text="[Área da Ilustração do Marketplace]", 
        fg="#8a99ad", 
        bg="#0a0f1d", 
        font=("Helvetica", 12, "italic")
    )
    marcador_esquerdo.place(relx=0.5, rely=0.5, anchor="center")
    
    # --- Painel Direito (Espaço para Formulário de Login) ---
    # Largura de 450px, com fundo ligeiramente mais claro para contraste
    painel_direito = tk.Frame(janela_principal, width=450, height=550, bg="#161e35", bd=0, highlightthickness=0)
    painel_direito.pack(side="right", fill="both", expand=True)
    painel_direito.pack_propagate(False)
    
    # Adicionamos um rótulo temporário apenas para identificar o painel direito
    marcador_direito = tk.Label(
        painel_direito, 
        text="[Área do Formulário de Login]", 
        fg="#ffffff", 
        bg="#161e35", 
        font=("Helvetica", 12)
    )
    marcador_direito.place(relx=0.5, rely=0.5, anchor="center")
    
    # Inicia o loop de eventos da interface gráfica
    janela_principal.mainloop()

if __name__ == "__main__":
    principal()
