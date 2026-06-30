import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(''' 
    CREATE TABLE IFNOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    )''')

    # o banco de dados náo está salvando as alterações. Por que?
    # R= Por que não tinha o commit para salvar antes de fechar a conexao!

    conexao.commit() 
    conexao.close()