import sqlite3
from banco import conectar

def cadastrar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        nome = input("Digite o nome das escolas: ")
        cidade = input("Digite a cidadade: ")

        assert nome != "", "O nome da escola não pode ficar vazia"
        assert cidadade != "", "A cidade não pode ficar vazia"

        cursor.execute('''
                INSERT INTO escolas (nome, cidade)
                VALUES (?,?)
                ''', (nome, cidade))


        conexao.commit()
        conexao.close()

        print("Escola cadastrada!")

    except AssertionError as erro:
        print("Erro:" erro)

    except sqlite3.Error as erro:
        print("Erro:", erro)


def listar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        