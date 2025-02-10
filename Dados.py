import random

def simular_dados():
    tipo_de_dados = int(input("Digite o tipo do dado (6 para D6 e 20 para D20): "))
    if tipo_de_dados not in [6, 20]:
        print("Tipo de dado inválido!")
        return
    num_lancamentos = int(input("Digite a quantidade de lançamentos a ser realizada: "))
    resultados = []
    for i in range(num_lancamentos):
        resultado = random.randint(1, tipo_de_dados)
        resultados.append(resultado)  
    print(f"Resultados dos lançamentos de dados do tipo D{tipo_de_dados}: ")
    print(resultados)

simular_dados()
