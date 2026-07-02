import sqlite3
# o aluno criou a conexao fora das funções para "facilitar"
# por que  isso quebra o sistema quando usamos multiplos arqivos (modulos)?

def inserir_escola (nome):
    conexao = sqlite3.connect('sistema-escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome))
    conexao.commit()
    conexao.close()


# R= O erro foi por que foi criado fora do def e não teria como ser executado