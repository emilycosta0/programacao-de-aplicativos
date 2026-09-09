import sqlite3

def criar_tabelas():
    try:
        conexao = sqlite3.connet("gestao_escolar.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS escolas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cidade TEXT )''')


        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS turmas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_turma TEXT,
                    id_escola INTEGER,
                    FOREIGN KEY (id_escola) REFERENCES escolas (id) )''')


        cursor.excute('''
                    CREAT TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    id_turma,
                    FOREIGN KEY (id_turma) REFERENCES turmas )''')


        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco!", erro)

    finally:
        conexao.close()


       