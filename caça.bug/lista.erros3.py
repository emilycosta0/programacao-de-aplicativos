import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema-escola.db')
    cursor = conexao.cursor()

    #este bloco quebra ao rodar pela primeira vez um bloco limpo. por quê
    # R= Se a tabela esta vazia, sem registro algum, então o ID não existe.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_serie TEXT,
        id_escola INTEGER,
        FOREIGN KEY REFERENCES escolas) 
        )''')

    cursor.execute('''
         CREATE TABLE IF NOT EXISTS ESCOLAS (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         nome TEXT
         )''')

    conexao.commit()
    conexao.close()
        