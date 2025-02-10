def exibir_menu():
    print("\n--- To-Do List Do Pedro ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como feita")
    print("4. Remover tarefa")
    print("5. Sair")

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNão há tarefas na lista.")
    else:
        print("\n--- Tarefas ---")
        for i, tarefa in enumerate(tarefas, 1):
            status = "Feita" if tarefa['feita'] else "Pendente"
            print(f"{i}. {tarefa['descricao']} - {status}")

def adicionar_tarefa(tarefas):
    descricao = input("\nDigite a descrição da tarefa: ") 
    tarefas.append({'descricao': descricao, 'feita': False})
    print("Tarefa adicionada!")

def marcar_como_feita(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("\nDigite o número da tarefa para marcar como feita: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]['feita'] = True
            print("Tarefa marcada como feita!")
        else:
            print("Índice inválido!")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("\nDigite o número da tarefa para remover: "))
        if 1 <= indice <= len(tarefas):
            tarefas.pop(indice - 1)
            print("Tarefa removida!")
        else:
            print("Índice inválido!")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    tarefas = []
    
    while True:
        exibir_menu()
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if escolha == 1:
                adicionar_tarefa(tarefas)
            elif escolha == 2:
                listar_tarefas(tarefas)
            elif escolha == 3:
                marcar_como_feita(tarefas)
            elif escolha == 4:
                remover_tarefa(tarefas)
            elif escolha == 5:
                print("Saindo... Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
