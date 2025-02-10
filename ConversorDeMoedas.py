def converter_moeda(valor,taxa):
    return valor*taxa

print("Bem vindo ao conversor de moedas do Pedro!")
moeda_origem = input("Digite a sua moeda de origem (USD,EUR,BRL): ").upper()
moeda_final = input("Digite a sua moeda de origem (USD,EUR,BRL): ").upper()
valor = float(input(f"Digite o valor da moeda em {moeda_origem}: "))

taxas = {
    ("USD", "BRL"): 6.0,  
    ("BRL", "USD"): 0.2,  
    ("EUR", "BRL"): 5.3,  
    ("BRL", "EUR"): 0.19  
}
taxa = taxas.get((moeda_origem, moeda_final), None)
if taxa:
    convertido = converter_moeda(valor,taxa)
    print(f"{valor} {moeda_origem} equivale a {convertido:.2f} {moeda_final}")
else:
    print("Conversão não disponível para essas moedas.")


