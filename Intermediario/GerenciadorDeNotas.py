import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="p3dr0h3n",  
    database="sistema_notas"
)

cursor = conexao.cursor()

# Função para exibir o menu
def menu():
    print("\nBem-vindo ao gerenciador de notas do Pedro!")
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Consultar notas")
    print("4 - Listar todos os alunos")
    print("5 - Sair")

# Loop principal
while True:
    menu()
    
    try:
        opcao = int(input("Digite a sua opção: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if opcao == 1:
        # Cadastrar aluno
        nome_aluno = input("Digite o nome do aluno para ser adicionado: ").strip()
        if nome_aluno:
            cursor.execute("INSERT INTO alunos (nome) VALUES (%s)", (nome_aluno,))
            conexao.commit()
            id_aluno = cursor.lastrowid
            print(f"Aluno '{nome_aluno}' adicionado com ID {id_aluno}.")
        else:
            print("O nome do aluno não pode ser vazio.")

    elif opcao == 2:
        # Adicionar nota
        try:
            verificador_aluno = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("ID inválido! Digite um número inteiro.")
            continue

        cursor.execute("SELECT * FROM alunos WHERE id = %s", (verificador_aluno,))
        aluno = cursor.fetchone()
        
        if aluno:
            try:
                nota_aluno = float(input("Digite a nota do aluno: "))
                cursor.execute("INSERT INTO notas (aluno_id, nota) VALUES (%s, %s)", (verificador_aluno, nota_aluno))
                conexao.commit()
                print(f"Nota {nota_aluno} adicionada para o aluno de ID {verificador_aluno}.")
            except ValueError:
                print("Por favor, insira uma nota válida (número).")
        else:
            print("Aluno não encontrado. Verifique o ID e tente novamente.")

    elif opcao == 3:
        # Consultar todas as notas
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()

        if notas:
            print("\nID Nota | ID Aluno | Nota")
            print("-" * 30)
            for nota in notas:
                print(f"{nota[0]:<7} | {nota[1]:<8} | {nota[2]:.2f}")
        else:
            print("Nenhuma nota cadastrada.")

    elif opcao == 4:
        # Listar todos os alunos
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        if alunos:
            print("\nID | Nome do Aluno")
            print("-" * 25)
            for aluno in alunos:
                print(f"{aluno[0]:<2} | {aluno[1]}")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == 5:
        # Sair do programa
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Escolha entre 1 e 5.")

# Fechar conexão com o banco de dados
cursor.close()
conexao.close()
