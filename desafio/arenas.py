import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS arenas_digitais(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_servidor TEXT,
                id_liga INTEGER,
                FOREIGN KEY (id_liga) REFERENCES liga_games(id)
            )
        """)

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco!", erro)

    finally:
        conexao.close()


def cadastrar_arenas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        nome = input("Digite o nome do servidor: ")
        id_liga = int(input("Digite o ID da liga: "))

        cursor.execute(
            f"SELECT * FROM liga_games WHERE id = {id_liga}"
        )

        if cursor.fetchone():

            comando = f"""
                INSERT INTO arenas_digitais (nome_servidor, id_liga)
                VALUES ('{nome}', {id_liga})
            """

            cursor.execute(comando)
            conexao.commit()

            print("Arena cadastrada!")

        else:
            print("Liga não encontrada.")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar_arenas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM arenas_digitais")

        arenas = cursor.fetchall()

        if arenas:
            for arena in arenas:
                print(arena)
        else:
            print("Nenhuma arena cadastrada.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def atualizar_arenas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        id_arena = int(input("Digite o ID da arena: "))
        nome = input("Digite o novo nome do servidor: ")
        id_liga = int(input("Digite o novo ID da liga: "))

        cursor.execute(
            f"SELECT * FROM arenas_digitais WHERE id = {id_arena}"
        )

        if cursor.fetchone():

            cursor.execute(
                f"SELECT * FROM liga_games WHERE id = {id_liga}"
            )

            if cursor.fetchone():

                comando = f"""
                    UPDATE arenas_digitais
                    SET nome_servidor = '{nome}',
                        id_liga = {id_liga}
                    WHERE id = {id_arena}
                """

                cursor.execute(comando)
                conexao.commit()

                print("Arena atualizada!")

            else:
                print("Liga não encontrada!")

        else:
            print("Arena não encontrada!")

    except ValueError:
        print("Digite apenas números nos IDs.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def excluir_arenas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        id_arena = int(input("Digite o ID da arena: "))

        cursor.execute(
            f"SELECT * FROM arenas_digitais WHERE id = {id_arena}"
        )

        if cursor.fetchone():

            cursor.execute(
                f"DELETE FROM arenas_digitais WHERE id = {id_arena}"
            )

            conexao.commit()

            print("Arena excluída!")

        else:
            print("Arena não encontrada.")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()
