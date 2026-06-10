import sqlite3

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
telefone_aluno = input("Dgite o telefone do aluno: ")
turma_aluno = input("Digite a turma do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
cpf_aluno = input("Digite o cpf do aluno: ")

comando_inserir = f''' 
                INSERT INTO alunos (nome, telefone, idade, cpf)
                VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno})'''

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()