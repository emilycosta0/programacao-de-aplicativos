import sqlite3

def cadastrar_escolas():
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        nome = input("Digite o nome da escola: ")
        cidade = input("Digite o nome da cidade: ")

        if nome == "":
            print("O nome da escola não pode ficar vazio.")

        elif cidade == "":
            print("A cidade não pode ficar vazia.")

        else:
            comando = f'''
                    INSERT INTO escolas (nome, cidade)
                    VALUES ('{nome}', '{cidade}')'''

        
        cursor.execute(comando)
        conexao.commit()

        print("Escola cadastrada!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar_ecolas():
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")

        escolas = cursor.fetchall()

        if escolas:
            for escola in escolas:
                print(escola)

        else:
            print("Nenhuma escola cadastrada.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def atualizar_escolas():
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        id_escola = int(input("Digite o ID da escola: "))
        nome = input("Digite o novo nome da escola: ")
        cidade = input("Digite a nova cidade: ")

        if nome == "":
            print("O nome da escola não pode ficar vazio.")

        elif cidade == "":
            print("A cidade não pode ficar vazia.")

        else:
            cursor.execute(
                f''' SELECT * FROM escolas WHERE id = {id_escola}'''
            )

            if cursor.fetchone():
                comando = f'''
                        UPDATE escolas
                        SET nome = '{nome}',
                            cidade = '{cidade}'
                        WHERE id = {id_escola}
                    '''

                cursor.execute(comando)
                conexao.commit()

                print("Escola atualizada!")

            else:
                print("Escola não encontrada!")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def excluir_escolas():
    try:
        conexao = sqlite3.connect("gestao_escolar.db")
        cursor = conexao.cursor()

        id_escola = int(input("Digite o ID da escola: "))

        cursor.execute(
            f"SELECT * FROM escolas WHERE id = {id_escola}"
        )

        if cursor.fetchone():

            cursor.execute(
                    f'''DELETE FROM escolas WHERE id = {id_escola}'''
            )
        
            conexao.commit()

            print("Escola excluída!")
        
        else:
            print("Escola não emcontrada.")

    except ValueError:
        print("Digite apenas números no ID.")

    except sqlite3.Error as erro:
        print("Não foi possível excluir a escola.")
        print("Existem turmas vinculadas a esta escola.")
        print("Erro:", erro)

    finally:
        conexao.close()




        



