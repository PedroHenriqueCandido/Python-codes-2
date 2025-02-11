import random

def jogar_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    while not acertou:
        try:
            palpite = int(input("Qual é o seu palpite? "))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("O número é maior que isso. Tente novamente!")
            elif palpite > numero_secreto:
                print("O número é menor que isso. Tente novamente!")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        
        except ValueError:
            print("Por favor, insira um número válido.")

# Chama a função para rodar o jogo
if __name__ == "__main__":
    jogar_adivinhacao()
