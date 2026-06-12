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
telefone_aluno = input("Digite o telefone do aluno: ")
turma_aluno = input("Digite a turma do aluno: ")
idade_aluno = int(input("Digite a idade do aluno: "))
cpf_aluno = input("Digite o cpf do aluno: ")

comando_inserir = f''' 
                INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}')'''

cursor.execute(comando_inserir)
conexao.commit()

cursor.execute('''SELECT * FROM alunos''')
todos_alunos = cursor.fetchall()

if not todos_alunos:
    print("Nenhum aluno cadastrado.")
else:
    for aluno in todos_alunos:
        print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Telefone: {aluno[2]}, Turma: {aluno[3]}, Idade: {aluno[4]}, CPF: {aluno[5]} ")
conexao.close()



def atualizar_dados_aluno():
    conn = sqlite3.connect('escola_demonstracao.db')
    cursor = conn.cursor()
    
    id_aluno = 1
    novo_nome = "Gabriela Ropelatto"
    novo_cpf = "111.222.333-44"

    cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
    aluno_antigo = cursor.fetchone()
    
    if aluno_antigo:
        print(f"Aluno encontrado antes da atualização: {aluno_antigo}")
        
        sql_atualiza = """
            UPDATE Alunos 
            SET nome = ?, cpf = ? 
            WHERE id = ?
        """
        cursor.execute(sql_atualiza, (novo_nome, novo_cpf, id_aluno))
        
        conn.commit()
        print("Dados alterados com sucesso!")
        
        cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
        aluno_atualizado = cursor.fetchone()
        print(f"Aluno após a atualização: {aluno_atualizado}")
    else:
        print("Aluno não encontrado com o ID especificado.")

    
    conn.close()

if __name__ == "__main__":
    atualizar_dados_aluno()