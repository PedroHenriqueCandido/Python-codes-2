import tkinter as tk
import random

# Função para o jogo
def escolha_pc():
    return random.randint(1, 3)

def determinar_vencedor(usuario, pc):
    if usuario == pc:
        return "Empate!"
    elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def jogar(escolha_usuario):
    pc_escolha = escolha_pc()

    # Mapeando as escolhas
    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    # Exibindo as escolhas
    usuario_escolha_label.config(text=f"Você escolheu: {opcoes[escolha_usuario]}")
    pc_escolha_label.config(text=f"O computador escolheu: {opcoes[pc_escolha]}")

    # Determinando o vencedor
    resultado = determinar_vencedor(escolha_usuario, pc_escolha)
    resultado_label.config(text=resultado)

# Função para o botão reiniciar
def reiniciar():
    usuario_escolha_label.config(text="Você escolheu: ")
    pc_escolha_label.config(text="O computador escolheu: ")
    resultado_label.config(text="")

# Configuração da janela
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")

# Configurando as labels
usuario_escolha_label = tk.Label(root, text="Você escolheu: ", font=("Arial", 14))
usuario_escolha_label.pack(pady=10)

pc_escolha_label = tk.Label(root, text="O computador escolheu: ", font=("Arial", 14))
pc_escolha_label.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
resultado_label.pack(pady=10)

# Botões de escolha
pedra_button = tk.Button(root, text="Pedra", font=("Arial", 14), command=lambda: jogar(1))
pedra_button.pack(side=tk.LEFT, padx=10, pady=10)

papel_button = tk.Button(root, text="Papel", font=("Arial", 14), command=lambda: jogar(2))
papel_button.pack(side=tk.LEFT, padx=10, pady=10)

tesoura_button = tk.Button(root, text="Tesoura", font=("Arial", 14), command=lambda: jogar(3))
tesoura_button.pack(side=tk.LEFT, padx=10, pady=10)

# Botão reiniciar
reiniciar_button = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=reiniciar)
reiniciar_button.pack(pady=20)

# Iniciar a interface
root.mainloop()
