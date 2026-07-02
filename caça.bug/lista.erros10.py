import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a revomer: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #esse comando vai apagar o banco inteiro se o aluno não prestar atenção
    cursor.execute("DELETE FROM escolas WHERE id = id_escola")

    conexao.commit()
    conexao.close()

    # R= Falta o "?" para reconhecer o ID que deseja remover