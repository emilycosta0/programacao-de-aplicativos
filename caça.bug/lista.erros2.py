import sqlite3

def cadastar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA  foreing_keys = ON")
    # o aluno tenta cadastrar uma serie com id_escola = 999 (que não existe)
    # o SQlite aceita o cadastro mesmo assim. O que eta falatndo ativar?
    # R= Tivemos que usar o PRAGMA, feito para alterar algumas configurações da conexão.
    try:
        curosr.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        print("Código encerrado!")
            conexao.close()

