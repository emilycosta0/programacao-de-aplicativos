import sqlite3

def cadastrar_aluno():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL,
                id_professor INTEGER,
                FOREIGN KEY (id_professor) REFERENCES professores (id)
                
        )
    ''')

    nome_aluno = input("Digite o nome do aluno: ")
    telefone_aluno = input("Digite o telefone do aluno: ")
    turma_aluno = input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno = input("Digite o cpf do aluno: ")
    id_professor = int(input("Digite o ID do professor: "))

    comando_inserir = f''' 
                    INSERT INTO alunos (nome, telefone, turma, idade, cpf, id)
                    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}', '{id_professor}')'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()


def listar_alunos():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM alunos''')
    todos_alunos = cursor.fetchall()

    if not todos_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in todos_alunos:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Telefone: {aluno[2]}, Turma: {aluno[3]}, Idade: {aluno[4]}, CPF: {aluno[5]} ")
    conexao.close()


def atualizar_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    listar_alunos()

    id_busca = int(input("Digite o ID do aluno que deseja atualizar: "))

    cursor.execute(f'''SELECT * FROM alunos WHERE id={id_busca}''')
    aluno = cursor.fetchone()

    if not aluno:
        print("Aluno não encontrado.")
        conexao.close()
        return
    else:
        novo_nome = input("Digite o novo nome do aluno: ")
        novo_telefone = input("Digite o novo telefone do aluno: ")
        nova_turma = input("Digite a nova turma do aluno: ")
        nova_idade = int(input("Digite a nova idade do aluno: "))
        novo_cpf = input("Digite o novo CPF do aluno: ")
        novo_id_professor = int(input(f"Novo ID Professor ({aluno[6]}): "))

        comando = f'''UPDATE alunos SET nome ='{novo_nome}', telefone ={novo_telefone}, turma='{nova_turma}', idade={nova_idade}, cpf={novo_cpf}, novo id={novo_id_professor} WHERE id={id_busca}'''

        cursor.execute(comando)
        conexao.commit()
        conexao.close()


def excluir_aluno():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    listar_alunos()
    
    id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

    cursor.execute(f'''SELECT * FROM alunos WHERE id={id_aluno}''')
    conexao.commit()
    conexao.close()
     

while True: 
    print("1-Cadastar | 2-Listar | 3-Atualizar | 4-Excluir | 5-Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1": cadastrar_aluno()
    elif opcao == "2" : listar_alunos()
    elif opcao == "3" : atualizar_aluno()
    elif opcao == "4" : excluir_aluno()
    elif opcao == "5" : break   

    










