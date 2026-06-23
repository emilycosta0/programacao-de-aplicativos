import sqlite3

def cadastrar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                materia TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL,
                salario REAL,
                escola TEXT NOT NULL
                endereço TEXT
                cidade TEXT
                estado TEXT
                
         )''')
    
    nome_prof = input("Digite o nome completo: ")
    telefone_prof = input("Digite o telefone: ")
    materia_prof = input("Digite a matéria: ")
    idade_prof = int(input("Digite a idade: "))
    cpf_prof = input("Digite o CPF: ")
    salario_prof = float(input("Digite o salário: "))
    escola_prof = input("Digite o nome da escola: ")
    endereco_prof = input("Digite o endereço: ")
    cidade_prof = input("Digite a cidade: ")
    estado_prof = input("Digite o estado: ")

    comando_inserir = (f'''
                        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola)
                        VALUES ('{nome_prof}', '{telefone_prof}', '{materia_prof}', {idade_prof}, '{cpf_prof}',
                        '{salario_prof}', '{escola_prof}', '{endereco_prof})', '{cidade_prof}', '{estado_prof}' ''')
               
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()



def listar_professores():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM professores''')
    todos_professores = cursor.fetchall()

    if not todos_professores:
        print("Nenhum professor no cadastro!")
    else:
        for professor in todos_professores:
            print(f"ID = {professor[0]}, Nome = {professor[1]}, Telefone = {professor[2]}, Materia = {professor[3]}, Idade = {professor[4]}, CPF = {professor[5]}, Salário = {professor[6]}, Escola = {professor[7]}, Endereço = {professor[8]}, Cidade = {professor[9]}, Estado = {professor[10]}") 
    conexao.close()


def atualizar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    id_busca = int(input("Digite o ID do professor para atualizar: "))

    cursor.execute(f'''SELECT * FROM professores WHERE id={id_busca}''')
    professor = cursor.fetchone()

    if not professor:
        print("Professor não encontrado no cadastro!")
        conexao.close()
        return
    else:
        novo_nome = input("Digite o novo nome:  ")
        novo_telefone = input("Digite o novo telefone: ")
        nova_materia = input("Digite a nova materia: ")
        nova_idade = int(input("Digite a nova idade: "))
        novo_cpf = input("Digite o novo CPF: ")
        novo_salario = float(input("Digite  o novo salário: "))
        nova_escola = input("Digite a nova escola: ")
        novo_endereço = input("Digite o novo endereço: ")
        nova_cidade = input("Digite a nova cidade: ")
        novo_estado = input("Digite o novo estado: ")

        comando = f'''UPDATE professores SET nome ='{novo_nome}', telefone ={novo_telefone}, materia ='{nova_materia}', idade={nova_idade}, cpf='{novo_cpf}', salario={novo_salario}, escola='{nova_escola}', endereço='{novo_endereço}', cidade='{nova_cidade}', estado='{novo_estado}' WHERE id={id_busca}'''

        cursor.execute(comando)
        conexao.commit()
        conexao.close()



def excluir():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()
    listar_professores()
    id_professor = int(input("Digite o ID do aluno que deseja excluir: "))

    cursor.execute(f'''DELETE FROM professores
                    WHERE id={id_professor}''')
    print("Professor excluido!")
    conexao.commit()
    conexao.close()

    
while True:
    print("--------Cadastro de professores--------")
    print("1-Cadastar | 2-Listar | 3-Atualizar | 4-Excluir | 5-Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1": cadastrar()
    elif opcao == "2" : listar_professores()
    elif opcao == "3" : atualizar()
    elif opcao == "4" : excluir()
    elif opcao == "5" : break

