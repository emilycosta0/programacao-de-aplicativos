import sqlite3

def criar_tabelas():
    try:
        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cinema(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cinema TEXT NOT NULL,
                        shopping TEXT NOT NULL
                        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS salas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_sala INTEGER NOT NULL,
                        capacidade INTEGER NOT NULL,
                        id_cinema INTEGER NOT NULL,
                        FOREIGN KEY (id_cinema) REFERENCES cinema(id)
                        )''')

        conexao.commit()


    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()
criar_tabelas()


def inserir_tabelas():
    try:
        conexao = sqlite3.connect("cinema.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()

        nome_cinema = input("Digite o nome do cinema: ")
        shopping = input("Digite o nome do Shopping: ")
        numero_sala = int(input("Digite o numero da sala: "))
        capacidade = int(input("Digite a capacidade de pessoas na sala: "))
        id_cinema = int(input("ID do cinema: "))
    except ValueError:
        print("Digite apenas números.")
        return

        comando_inserir = f'''
                            INSERT INTO cinemas (nome_cinema, shopping)
                            VALUES ('{nome_cinema}', '{shopping}')'''

        cursor.execute(comando_inserir)
        conexao.commit()

        cursor.execute(f"SELECT * FROM cinemas WHERE id = {id_cinema}")


        if cursor.fetchone():

            comando_inserir = f'''
                                INSERT INTO salas (numero_sala, capacidade, id_cinema)
                                VALUES ({numero_sala}, {capacidade}, {id_cinema})'''
            

            cursor.execute(comando_inserir)
            conexao.commit()

            print("Sala cadastrada!")

        else:
            print("Cinema não encontrado.")

        cursor.execute("SELECT * FROM salas")
        salas = cursor.fetchall()

        for sala in salas:
            print(sala)

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()

inserir_tabelas()