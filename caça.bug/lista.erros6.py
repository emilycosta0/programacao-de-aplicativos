import sqlite3

def buscar-professores(id_prof):
    conexao = sqlite3.connect9('sistema_escola.db')
    cursor = conexao.cursor()

    # o python reclama de 'Incorrect number of bindings'.
    # estamos passando a variavel, por que ocorre o erro?
    # R= o erro é que: para criar uma tupla com só um elemento é necessario colocar uma virgula 
    
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,)) #virgula obragatoria em tupla com um unico elemneto
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()