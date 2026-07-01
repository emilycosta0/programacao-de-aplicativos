import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o sistema aceita cadastrar dois professores coom o mesmo CPF.
    # Como restringir isso direto na estrutura da tabela abaixo?

    cursor.execute('''
                   CREAT TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY AUTOINCREMENT,
                    nome TEXT,
                    cpf TEXT UNIQUE
                    ) ''')
    

# R= faltou o UNIQUE para identificar que o cpf é unico (só uma pessoa que tem)