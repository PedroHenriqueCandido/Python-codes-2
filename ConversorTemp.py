def kelvin_celsius(temp_kelvin):

    temp_celsius = temp_kelvin - 273.15
    print(f'A temperatura em Celsius é: {temp_celsius:.2f}°C')
    return temp_celsius

def kelvin_fahrenheit(temp_kelvin):

    temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
    print(f'A temperatura em Fahrenheit é: {temp_fahrenheit:.2f}°F')
    return temp_fahrenheit

def celsius_kelvin(temp_celsius):

    temp_kelvin = temp_celsius + 273.15
    print(f'A temperatura em Kelvin é: {temp_kelvin:.2f}K')
    return temp_kelvin

def fahrenheit_kelvin(temp_fahrenheit):

    temp_kelvin = (temp_fahrenheit - 32) * 5/9 + 273.15
    print(f'A temperatura em Kelvin é: {temp_kelvin:.2f}K')
    return temp_kelvin

def menu():

    print("\nBem-vindo ao conversor de temperatura do Pedro!")
    print("Escolha uma conversão:")
    print("1. Kelvin para Celsius")
    print("2. Kelvin para Fahrenheit")
    print("3. Celsius para Kelvin")
    print("4. Fahrenheit para Kelvin")
    print("5. Sair")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == '1':
        temp = float(input("Digite a temperatura em Kelvin: "))
        kelvin_celsius(temp)
    elif escolha == '2':
        temp = float(input("Digite a temperatura em Kelvin: "))
        kelvin_fahrenheit(temp)
    elif escolha == '3':
        temp = float(input("Digite a temperatura em Celsius: "))
        celsius_kelvin(temp)
    elif escolha == '4':
        temp = float(input("Digite a temperatura em Fahrenheit: "))
        fahrenheit_kelvin(temp)
    elif escolha == '5':
        print("Saindo do conversor... Até logo!")
    else:
        print("Opção inválida! Tente novamente.")
        menu()


menu()
