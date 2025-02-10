def menu():
    print("Bem-vindo ao caixa digital do Pedro!")
    print("Qual operação deseja realizar?")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver Saldo")
    print("4 - Sair")
    return

saldo = 0
menu()

opcao = int(input("Digite a sua opção: "))
while opcao != 4:
    if opcao == 1:
        retirar = float(input("Quanto você deseja sacar: R$ "))
        if saldo < retirar:
            print("Sem saldo suficiente!")
        else:
            saldo = saldo - retirar
            print(f"Saque concluído. O saldo atual é R${saldo}!")
    elif opcao == 2:
        depositar = float(input("Quanto deseja depositar: R$ "))
        saldo = saldo + depositar
        print(f"Depósito concluído. O saldo atual é R${saldo}!")
    elif opcao == 3:
        print(f"O saldo é de R${saldo}")
    else:
        print("Opção inválida! Tente novamente.")
    

    menu()
    opcao = int(input("Digite a sua opção: "))

print("Fim do programa!")
