import sqlite3

def criar():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT,
            shopping TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS salas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER,
            capacidade INTEGER,
            id_cinema INTEGER,
            FOREIGN KEY(id_cinema) REFERENCES cinemas(id)
        )
        """)

        nome = input("Nome do cinema: ")
        shopping = input("Shopping: ")

        cursor.execute(
            "INSERT INTO cinemas(nome_cinema, shopping) VALUES (?, ?)",
            (nome, shopping)
        )

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def cadastrar():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        numero = int(input("Número da sala: "))
        capacidade = int(input("Capacidade: "))
        id_cinema = int(input("ID do cinema: "))

        cursor.execute("SELECT * FROM cinemas WHERE id = ?", (id_cinema,))

        if cursor.fetchone():
            cursor.execute("""
                INSERT INTO salas(numero_sala, capacidade, id_cinema)
                VALUES (?, ?, ?)
            """, (numero, capacidade, id_cinema))

            conexao.commit()
            print("Sala cadastrada!")

        else:
            print("Cinema não encontrado.")

    except ValueError:
        print("Digite apenas números nos campos numéricos.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM salas")
        salas = cursor.fetchall()

        if salas:
            for sala in salas:
                print(sala)
        else:
            print("Nenhuma sala cadastrada.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


criar()
cadastrar()
listar()


