def menu():
  
    print("\nBem-vindo ao conversor de unidades do Pedro!")
    print("Escolha uma opção:")
    print("1 - Metro para Km")
    print("2 - Km para Metro")
    print("3 - Cm para Metro")
    print("4 - Metro para Cm")
    print("5 - Cm para Km")
    print("6 - Km para Cm")
    print("7 - Sair")

def metro_km(num): 
    return num / 1000

def km_metro(num):
    return num * 1000

def cm_metro(num):
    return num / 100

def metro_cm(num):
    """Converte metros para centímetros"""
    return num * 100

def cm_km(num):
   
    return num / 100000

def km_cm(num):
   
    return num * 100000

def obter_numero():
   
    while True:
        try:
            numero = float(input("Digite o seu número: "))
            return numero
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_opcao():
    
    while True:
        try:
            opcao = int(input("Digite a sua opção: "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Por favor, escolha uma opção válida entre 1 e 7.")
        except ValueError:
            print("Opção inválida. Digite um número entre 1 e 7.")

def main():
    while True:
        menu()
        opcao = obter_opcao()

        if opcao == 7:
            print("Fim do programa")
            break

        numero = obter_numero()

        if opcao == 1:
            resultado = metro_km(numero)
            print(f"A medida em Km é: {resultado:.6f}")
        elif opcao == 2:
            resultado = km_metro(numero)
            print(f"A medida em metro é: {resultado:.2f}")
        elif opcao == 3:
            resultado = cm_metro(numero)
            print(f"A medida em metro é: {resultado:.2f}")
        elif opcao == 4:
            resultado = metro_cm(numero)
            print(f"A medida em centimetro é: {resultado:.2f}")
        elif opcao == 5:
            resultado = cm_km(numero)
            print(f"A medida em Km é: {resultado:.6f}")
        elif opcao == 6:
            resultado = km_cm(numero)
            print(f"A medida em centimetro é: {resultado:.0f}")

if __name__ == "__main__":
    main()
