import sqlite3
def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    # se o usuario digitar "Turma B" em vez do numero do ID, o sistema quebra.
    # o try/except abaixo falhou em capturar esse erro. Qual o problema?
    # R= o problema era que não estava mostrando ese erro e iria continuar rodando sem aparecer.
    try: 
        id_turma = int(input("Digite o ID numérico da turma: "))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome,id_turma))
        conexao.commit()
    except (Valueerror, sqlite3.Error) as e:
        print("Erro", e)
    finally:
        print("Codigo encerrado.")
        conexao.close()