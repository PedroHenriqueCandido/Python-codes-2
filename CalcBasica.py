def pegar_num():
    n1 = float(input("Digite seu número agora: "))
    n2 = float(input("Digite seu outro número agora: "))
    return n1, n2  

print("Bem-vindo à calculadora do Pedro!")
resposta = input("Você quer fazer uma operação?(Y,N)")
if resposta == "N":
    print("Fim do programa") 
    exit()
else:
    op = input("Selecione uma operação básica (-, x, +, /): ")
    if op == "-":
        n1, n2 = pegar_num() 
        resultado = n1 - n2
        print(f"Resultado: {resultado}")
    elif op == "+":
        n1, n2 = pegar_num()
        resultado = n1 + n2 
        print(f"Resultado: {resultado}")
    elif op == "x":
        n1, n2 = pegar_num()
        resultado = n1 * n2 
        print(f"Resultado: {resultado}") 
    elif op == "/":
        n1, n2 = pegar_num()
        resultado = n1 / n2 
        print(f"Resultado: {resultado}")