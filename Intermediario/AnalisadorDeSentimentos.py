from textblob import TextBlob

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    if polaridade > 0:
        return "positivo"
    if polaridade == 0:
        return "neutro"
    else:
        return "negativo"
    
texto1 = input("Digite o texto para ser analisado: ")
resultado = analisar_sentimento(texto1)
print(f"Sentimento: {resultado}")

#Só funciona se digitar em ingles!!!!!!!!!!!!!!!!!