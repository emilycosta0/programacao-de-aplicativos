import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o relatorio roda, mas repete os dados erroneamente em formato de matriz cruzada
    # por que falta definir a regra de colagem (vinculo) . Conserte o comando SQL
    cursor.execute("SELECT alunos.nome, turma.nome_turma FROM alunos INNER JOIN turmas ON aluno.id_turma = turmas.id")

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | Turma: {linha[1]}")
    conexao.close()

# R= o erro é que faltou o 'ON' para ligar as turmas com os alunos


