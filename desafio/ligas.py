import sqlite3


def criar_tabelas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS liga_games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_liga TEXT,
                empresa_publisher TEXT
            )
        """)


        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco!", erro)

    finally:
        conexao.close()

def cadastrar_ligas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        nome = input("Digite o nome da liga: ")
        empresa = input("Digite a empresa/publisher: ")

        comando_inserir = f"""
            INSERT INTO liga_games (nome_liga, empresa_publisher)
            VALUES ('{nome}', '{empresa}')
        """

        cursor.execute(comando_inserir)
        conexao.commit()

        print("Liga cadastrada!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar_ligas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM liga_games")

        ligas = cursor.fetchall()

        if ligas:
            for liga in ligas:
                print(liga)
        else:
            print("Liga não cadastrada.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def atualizar_ligas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        id_liga = int(input("Digite o ID da liga: "))
        nome = input("Digite o novo nome da liga: ")
        empresa = input("Digite a nova empresa: ")

        cursor.execute(
            f"SELECT * FROM liga_games WHERE id = {id_liga}"
        )

        if cursor.fetchone():

            comando = f"""
                UPDATE liga_games
                SET nome_liga = '{nome}',
                    empresa_publisher = '{empresa}'
                WHERE id = {id_liga}
            """

            cursor.execute(comando)
            conexao.commit()

            print("Liga atualizada!")

        else:
            print("Liga não encontrada!")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def excluir_ligas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        id_liga = int(input("Digite o ID da liga: "))

        cursor.execute(
            f"SELECT * FROM arenas_digitais WHERE id_liga = {id_liga}"
        )

        if cursor.fetchone():
            print("Não é possível excluir esta liga.")
            print("Existem arenas vinculadas a ela.")

        else:
            cursor.execute(
                f"SELECT * FROM liga_games WHERE id = {id_liga}"
            )

            if cursor.fetchone():

                cursor.execute(
                    f"DELETE FROM liga_games WHERE id = {id_liga}"
                )

                conexao.commit()

                print("Liga excluída!")

            else:
                print("Liga não encontrada!")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()
