import sqlite3

def criar_aluno():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
        )
    ''')


    nome_aluno = input("Digite o nome do aluno: ")
    telefone_aluno = input("Digite o telefone do aluno: ")
    turma_aluno = input("Digite a turma do aluno: ")
    idade_aluno = int(input("Digite a idade do aluno: "))
    cpf_aluno = input("Digite o cpf do aluno: ")

    comando_inserir = f''' 
                    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}')'''

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
        novo_telefone = int(input("Digite o novo telefone do aluno: "))
        nova_turma = input("Digite a nova turma do aluno: ")
        nova_idade = int(input("Digite a nova idade do aluno: "))
        novo_cpf = int(input("Digite o novo CPF do aluno: "))

        comando = f'''UPDATE alunos SET nome ='{novo_nome}', telefone ={novo_telefone}, turma='{nova_turma}', idade={nova_idade}, cpf={novo_cpf} WHERE id={id_busca}'''

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
    conexao.close 
     
atualizar_aluno()



