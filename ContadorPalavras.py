def contar_palavras():
    # Passo 1: Receber o texto do usuário
    texto = input("Digite o texto para contar as palavras: ")

    # Passo 2: Dividir o texto em palavras usando o método split()
    palavras = texto.split()

    # Passo 3: Contar o número de palavras
    num_palavras = len(palavras)

    # Passo 4: Exibir o resultado
    print(f"O texto contém {num_palavras} palavras.")

# Chamar a função para executar o contador de palavras
contar_palavras()
