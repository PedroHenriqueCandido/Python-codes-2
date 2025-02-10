def contar_palavras():
    
    texto = input("Digite o texto para contar as palavras: ")

   
    palavras = texto.split()

   
    num_palavras = len(palavras)

    
    print(f"O texto contém {num_palavras} palavras.")


contar_palavras()
