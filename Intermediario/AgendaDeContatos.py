import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="suasenha",  
    database="AgendaContatos"
)

cursor = conexao.cursor()

def adicionar_contato(nome, telefone, email):
    sql = "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)"
    valores = (nome, telefone, email)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Contato adicionado com sucesso!")

def listar_contatos():
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    
    print("\nLista de Contatos:")
    for contato in contatos:
        print(f"ID: {contato[0]}, Nome: {contato[1]}, Telefone: {contato[2]}, Email: {contato[3]}")

def atualizar_contato(id, novo_nome, novo_telefone, novo_email):
    sql = "UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id=%s"
    valores = (novo_nome, novo_telefone, novo_email, id)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Contato atualizado com sucesso!")

def excluir_contato(id):
    sql = "DELETE FROM contatos WHERE id=%s"
    valores = (id,)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Contato excluído com sucesso!")

def menu():
    while True:
        print("\nAgenda de Contatos do Pedro")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_contato(nome, telefone, email)
        
        elif opcao == "2":
            listar_contatos()

        elif opcao == "3":
            id = input("ID do contato a ser atualizado: ")
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            novo_email = input("Novo Email: ")
            atualizar_contato(id, novo_nome, novo_telefone, novo_email)

        elif opcao == "4":
            id = input("ID do contato a ser excluído: ")
            excluir_contato(id)

        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()

cursor.close()
conexao.close()
