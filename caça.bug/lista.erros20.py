import sqlite3 
 
def cadastrar_escola_manual(): 
	# O aluno resolveu gerar o ID por conta própria 
    id_escola = int(input("Digite o ID para a nova escola: ")) 
	nome = input("Nome da escola: ") 
     
    conexao = sqlite3.connect('sistema_escola.db') 
	cursor = conexao.cursor() 
     
    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: este ID de escola já existe!")

    finally:
        conexao.close()

	# Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
	# Aplique a blindagem protetora necessária: 
    
# o erro é que se colocar um 'id' que ja existe na tabela, o SQlite gera um 'sqlite3.IntegrityError' por violar a chave primaria, encerrando o programa se não arrumar o erro.
