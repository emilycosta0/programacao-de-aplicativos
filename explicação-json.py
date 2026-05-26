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
            print(f"Editando dados de: {aluno['nome']}") #exibe essa mensagem no terminal, mostrando o nome do aluno que foi encontrado e confirmando para o usuário que ele está alterando a pessoa certa.
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome'] # pede um novo nome ao aluno
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']  # pede o novo telefone do aluno
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] # pede a nova turma do aluno 
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) # pede a nova idade do aluno
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] # pede o novo cpf do aluno
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
                json.dump(alunos, f, indent=4, ensure_ascii=False)  # salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
            print("Dados atualizados com sucesso!") #exibe esta mensagem quando atualizar todos os dados
            return #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada
            
    print("Aluno não encontrado.") # exibe essa mensagem se não encontrar um aluno

def excluir(): # def cria a função, e o nome da função(excluir) onde a função vai executar comandos
    print("\n--- Excluir Aluno ---") # quebra a linha e deixa o terminal organizado na parte de excluir um aluno
    if not os.path.exists(BANCO_DADOS): # o comando if not verifica se o arquivo existe ou não dentro da variável
        print("Nenhum aluno cadastrado no sistema.") # mostra essa mensagem se não tiver nunhum aluno cadrastado
        return # encerra a função por que está sozinho

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: # abre o arquivo banco_dados em modo de leitura, usando o utf-8 para conseguir usar acentuação
        alunos = json.load(f) # lê o que está dentro do arquivo f e transforma em um objeto, guardando o resultado na variável 'alunos'
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: ")) # pede o id do aluno que deseja remover
    
    nova_lista = [a for a in alunos if a['id'] != id_busca] # cria uma nova lista onde vai adicionar um novo id e o outro vai ser excluido 
    
    if len(nova_lista) < len(alunos): # o if cria uma nova função e dentro dela tem o len e ele conta quantas pessoas tem dentro da nova_lista 
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump(nova_lista, f, indent=4, ensure_ascii=False) # salva a lista de alunos no formato json, mantendo o arquivo organizado com recuo e acentos
        print("Aluno removido com sucesso!") # mostra essa mensagem no terminal quando remover um aluno
    else: # se a opção não existir vai para o else
        print("Aluno não encontrado.") # mostra essa mensagem se não encontrar aluno cadastrado

def menu(): # de cria a função, e o nome da função(menu) onde a função vai executar comandos
    if not os.path.exists(BANCO_DADOS): # o comando if not verifica se o arquivo existe ou não dentro da variável
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:  # abre o arquivo banco_dados em modo de escrita, usando o utf-8 para conseguir usar acentuação
            json.dump([], f) # o json.dump aqui armazena uma lista vazia ([]) no arquivo representado por f

    while True:  # laço de repetição que faz ele executar todas as opções
        print("\n=== SISTEMA ESCOLAR ===")  # mostra a mensagem, quebra a lista e começa a mostrar as opções
        print("1. Cadastrar Aluno") # print com a priemira opção
        print("2. Listar Alunos")  # print com a segunda opção 
        print("3. Atualizar Aluno") # print com a terceira opção
        print("4. Excluir Aluno")  # print com a quarta opção
        print("5. Sair") # ultimo print para sair das opções
        
        opcao = input("Escolha uma opção: ") # uma nova variavel, com o input para armazenar ela e para o usuário digitar uma das opções do print
        
        if opcao == '1': cadastrar() # o if cria uma função para o cadastro
        elif opcao == '2': listar() # o elif cria outra função igual a opção para listar
        elif opcao == '3': atualizar() # o elif cria oura função igual para atualizar
        elif opcao == '4': excluir() # o elif cria outra função igual a opção para excluir
        elif opcao == '5': break # o break serve para quebrar o loop
        else: print("Opção inválida!") # cria um else já com a mensagem e com a opção inválida

menu() # criada para mostrar o menu no terminal