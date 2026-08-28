import sqlite3 

def conectar():
    conexao = sqlite3.connect("gestão_escolar.db")

    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    return conexao

def criar_tabelas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cidade TEXT)''')

        
        cursor.execute('''
                CREAT TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT,
                id_escola INTEGER,
                FOREIGN KEY (id_turma) REFERENCES turmas (id)
                )''')

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                id_turma INTEGER,
                FOREIGN KEY (id_turma) REFERENCES turmas (id)
                )''')

        
        conexao.commit()
        conexao.close()

        print("Banco de dados criado!")

    except sqlite3.Error as erro:
        print("Erro ao criar o banco!", erro)
        

    

