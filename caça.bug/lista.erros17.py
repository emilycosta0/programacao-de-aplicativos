import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
    	cursor = conexao.cursor() 
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
        finally:
            conexao.close()

# R= o erro é que tem um erro de digitação (INSERTO - INSERT)
# e que o programa exibe o cpf incorretamente, por que o código mnada imprimir a mensagem independente do tipo de erro que aconteceu


