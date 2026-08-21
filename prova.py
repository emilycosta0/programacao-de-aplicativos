import sqlite3

def criar_tabelas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute(''' CREATE TABLE IF NOT EXISTS liga_games(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_liga TEXT,
                            empresa_publisher TEXT
                     )''')


        cursor.execute(''' CREATE TABLE IF NOT EXISTS arenas_digitais(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome_servidor TEXT,
                            id_liga INTEGER,
                            FOREIGN KEY (id_liga) REFERENCES liga_games(id)
                            )''')

        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco!", erro)
criar_tabelas()


def cadastrar_ligas(nome, empresa):
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
        
        comando_inserir = f'''
                            INSERT INTO liga_games (nome_liga, empresa_publisher)
                            VALUES ('{nome}', '{epresa}')'''
                            

        conexao.commit()

        return "Liga cadastrada!"
        

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
        print("Dados encontrados:", ligas)

        if ligas:
            for liga in ligas:
                print(liga)
        
        else:
            print("Liga não cadastrada.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()        


def atualizar_ligas(id_liga, nome, empresa):
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()

        
        cursor.execute("SELECT * FROM liga_games WHERE id = ?", (id_liga,))
        

        if cursor.fetchone():
            cursor.execute('''
                 UPDATE ligas_games
                 SET nome_liga = ?, empresa_publisher = ? 
                 WHERE id = ? 
                 ''', (nome, empresa, id_liga)) 

            conexao.commit()
            return "Liga atualizada!"

        else:
            print("Liga não encontrada!")

    except ValueError:
            print("Digite apenas número no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def excluir_ligas(id_liga):
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        cursor.execute(
                "SELECT * FROM arenas_digitais WHERE id_liga = ?",(id_liga,))
         
        if cursor.fetchone():
            print("Não é possivel excluir esta liga.")
            print("Existem arenas vinculadas a ela.")

        else:
            cursor.execute("DELETE FROM liga_games WHERE id = ?", (id_liga,))

            conexao.commit()

            return "Liga excluida!"   
   
    except ValueError:
        print("Digite apenas numeros no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()



def cadastrar_arenas():
    try:
        conexao = sqlite3.connect("torneio.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
        nome = input("Digite o nome do servidor: ")
        id_liga = input("Digite o ID da liga: ")

        cursor.execute (" SELECT * FROM liga_games WHERE id = ?", (id_liga,))


        if cursor.fetchone():

            cursor.execute = f'''
                            INSERT INTO arenas_digitas (nome_servidor, id_liga)
                            VALUES ('{nome}', '{id_liga}')'''

            conexao.commit()

            print("Arena cadastrada!")

        else:
            print("Liga não econtrada.")

    except ValueError:
        print("Digite apenas numeros no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)


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
        cursor.execute("PRAGMA foreign_keys = ON")

        id_arena = int(input("Digite o id da arena: "))
        nome = input("Digite o novo nome do servidor: ")
        id_liga = int(input("Digite o novo ID da liga: "))

        cursor.execute("SELECT * FROM arenas_digitais WHERE id = ?", (id_arena,))

        if cursor.fetchone():
            cursor.execute('''
                 UPDATE arenas_digitais
                 SET nome_servidor = ?, id_liga = ? 
                 WHERE id = ? 
                 ''', (nome, id_liga, id_arena)) 

            conexao.commit()
            print("Arena atualizada!")

        else:
            print("Arena não encontrada!")

    except ValueError:
            print("Digite apenas número nos ID.")

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
                "SELECT * FROM arenas_digitais WHERE id = ?",(id_arena,))

        if cursor.fetchone():

            cursor.execute(
                    "DELETE FROM arenas_digitais WHERE id = ?", (id_arena,))

            conexao.commit()
            print("Arena excluida!")

        else:
            print("Arena não encontrada.")    
   
    except ValueError:
        print("Digite apenas numeros no ID.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def menu():
    while True:
        try:
            print("---SISTEMAS DE TORNEIOS DE E-SPORTS---")
            print("1- Cadastrar Liga")
            print("2- Listar Liga")
            print("3- Atualizar Liga")
            print("4- Excluir Liga")
            print("5- Cadastrar Arena")
            print("6- Listar Arena")
            print("7- Atualizar Arena")
            print("8- Excluir Arena")
            print("9- Sair")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1: 
                nome = input("Digite o nome da liga: ")
                empresa = input("Empresa/Publisher: ")
                cadastrar_ligas()

            elif opcao == 2:
                listar_ligas()

            elif opcao == 3:
                id_liga = int(input("Digite o id da liga: "))
                nome = input("Digite o novo nome da liga: ")
                empresa = input("Digite a nova empresa: ")
                atualizar_ligas()

            elif opcao == 4:
                id_liga = input("Digite o ID da liga: ")
                excluir_ligas()

            elif opcao == 5:
                cadastrar_arenas()

            elif opcao == 6:
                listar_arenas()

            elif opcao == 7:
                atualizar_arenas()

            elif opcao == 8:
                excluir_arenas()

            elif opcao == 9:
                print("Fechando o Programa!")
                break

            else:
                print("Opção invalida, tente novamente!")

        except ValueError:
            print("Digite apenas numeros no ID.")

        except sqlite3.Error as erro:
            print("Erro:", erro)

criar_tabelas()
#menu()

assert cadastrar_ligas("Mario", "Nintendo") ==  "Liga cadastrada!"

assert atualizar_ligas("PlayStation", "Sony") == "Liga atualizada!" 
assert excluir_ligas("PlayStation", "Sony") == "Liga excluida!"






        

        

    





        