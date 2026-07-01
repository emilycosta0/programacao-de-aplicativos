import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o professor pediu para mudar o nome do aluno de ID 3,
    # mas o sistema alterou o nome de TODOS os alunos do banco de dados! Correção urgente:

    cursor.execute("UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()

    # o erro é que faltava o WHERE no cursor execute, sem ele o banco atualiza todas as linhas na tabela
    # e tambem não chamaou a funcao 'id_aluno' no cursor execute