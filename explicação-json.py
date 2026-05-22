import json # importa do python para o json.
import os # vê se o arquivo existe.

BANCO_DADOS = 'alunos.json' #variavel que guarda o nome do arquivo.

def cadastrar(): # cria uma função que se chama cadastrar, que posso colocar comandos para ser executados depois.
    print("\n--- Novo Cadastro ---") # quebra a linha e quando mostrar no terminal vai estar organizado.
    
    if os.path.exists(BANCO_DADOS): # se o arquivo realmente existir chamado banco_dados.
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação
            alunos = json.load(f) # lê o que está dentro do arquivo f e transforma em um objeto, guardando o resultado na variável 'alunos'
    else: # se não existir um arquivo chamado banco_dados ele vai parao else
        alunos = [] # e no else ele cria uma nova lista e ela está vazia

    novo_aluno = { # abre um dicionário que armazena os dados chamado 'novo_aluno'
        "nome": input("Nome: "), # na linha 16 até a linha 20 tem as chaves e os valores que estão dentro do dicionário
        "telefone": input("Telefone: "), # ex: "telefone" é a chave e o usuário que irá digitar o telefone é o valor
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    } # fecha o dicionário 
    
    alunos.append(novo_aluno) # adiciona o dicioário novo_aluno dentro da lista de alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo de texto para salvar as informações
        json.dump(alunos, f, indent=4, ensure_ascii=False) # salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
        
    print("Aluno cadastrado com sucesso!") # exibe essa mensagem no terminal avisando que o cadrasto deu certo

def listar(): # listar os alunos que já estão cadrastados
    print("\n--- Lista de Alunos ---") # quebra a linha e deixa o terminal organizado
    
    if os.path.exists(BANCO_DADOS): # se o arquivo realmente existir chamado banco_dados
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação
            alunos = json.load(f) # lê o que está dentro do arquivo f e transforma em um objeto, guardando o resultado na variável 'alunos'
    else: # se não existir um arquivo chamado banco_dados ele vai parao else
        alunos = [] # e no else ele cria uma nova lista e ela está vazia

    if not alunos: # verifica se a lista de alunos está vazia ou não
        print("Nenhum aluno cadastrado.") # exibe essa mensagem no terminal avisando que não há nenhum cadatrado
        return # o return encerra a função por que está sozinho

    for aluno in alunos: # percorre cada aluno dentro da lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") # essa linha pega os dados do objeto 'aluno' e monta uma frase com os dados

def atualizar(): # atualiza a lista de alunos cadastrados
    print("\n--- Atualizar Aluno ---") # quebra a linha e deixa o terminal organizado
    if not os.path.exists(BANCO_DADOS): # o comando if not verifica se o arquivo existe ou não dentro da variável
        print("Nenhum aluno cadastrado no sistema.") #exibe no terminal avisando que não tem nenhum aluno cadatrado no sistema
        return # encerra a função por que está sozinho

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação
        alunos = json.load(f)  # lê o que está dentro do arquivo f e transforma em um objeto, guardando o resultado na variável 'alunos'
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: ")) # aqui a pessoa digita o cpf do aluno que deseja editar na lista
    
    for aluno in alunos: # percorre cada aluno dentro da lista
        if aluno['cpf'] == cpf_busca: # percorre a lista 'aluno' e vê se tem algum cpf igual ao cpf que a pessoa digitou em 'cpf_busca'
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()