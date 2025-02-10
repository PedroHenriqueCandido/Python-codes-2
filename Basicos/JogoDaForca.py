import random

palavras = [
    "floresta", "computador", "cachorro", "inteligente", "mochila", 
    "felicidade", "montanha", "aventura", "carro", "livro", 
    "sol", "relógio", "guitarra", "amizade", "viagem", "coração", 
    "cidade", "bola", "laranja", "borboleta"
]

palavra_escolhida = random.choice(palavras)
letras_descobertas = ['_'] * len(palavra_escolhida)
tentativas_erradas = 0
tentativas_maximas = 6

while tentativas_erradas < tentativas_maximas and "_" in letras_descobertas:

    print("Palavra:", " ".join(letras_descobertas))
    

    letra = input("Digite uma letra: ").lower()
    
   
    if len(letra) == 1 and letra.isalpha():
        
        if letra in palavra_escolhida:
          
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    letras_descobertas[i] = letra
        else:

            tentativas_erradas += 1
            print(f"Letra errada! Tentativas restantes: {tentativas_maximas - tentativas_erradas}")
    else:
        print("Por favor, digite uma letra válida!")


if "_" not in letras_descobertas:
    print(f"Parabéns, você venceu! A palavra era: {palavra_escolhida}")
else:
    print(f"Você perdeu! A palavra era: {palavra_escolhida}")
