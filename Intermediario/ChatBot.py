def chatbot_resposta(mensagem):
    respostas = {
        'olá': 'Oi! Como posso ajudar você?',
        'tchau': 'Até logo! Tenha um ótimo dia!',
        'como você está?': 'Eu estou bem, obrigado por perguntar!',
        'qual é o seu nome?': 'Eu sou um chatbot simples!',
        'o que você faz?': 'Eu respondo suas perguntas de forma simples!',
        'o que vc é?': 'Eu sou um bot Simples em python feito pelo Pedro',
        'qual sua idade?': 'Eu tenho o total de 19 anos'
    }

    mensagem = mensagem.lower()

    if mensagem in respostas:
        return respostas[mensagem]
    else:
        return "Desculpe, não entendi. Pode reformular?"


def iniciar_chat():
    print("Chatbot está online! Digite 'tchau' para encerrar.")
    
    while True:
        mensagem_usuario = input("Você: ")
        
        if mensagem_usuario.lower() == 'tchau':
            print("Chatbot: Até logo! Tenha um ótimo dia!")
            break
        
        resposta = chatbot_resposta(mensagem_usuario)
        print(f"Chatbot: {resposta}")


iniciar_chat()
