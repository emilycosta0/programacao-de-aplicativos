import json
import os

banco_dados = 'alunos.json'

def cadastrar():
    print("\n-----NOVO CADASTRO-----")

    if os.path.exists(banco_dados):
        with open(banco_dados, 'r', encoding='utf-8') as arquivo:
            alunos = json.load(arquivo)
    else:
        alunos = []
    
    novo_aluno = {
        "ID": int(input("ID: ")),
        "Nome": input("Nome: "),
        "Telefone": input("Telefone: "),
        "Turma": input("Turma: "),
        "Idade": int(input("Idade: ")),
        "CPF": input("CPF: ")
    }

    alunos.append(novo_aluno)

    with open(banco_dados, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

    print("Aluno cadastrado com sucesso!")

def listar():
    print("\n-----LISTA DE ALUNOS-----")

    if os.path.exists(banco_dados):
        with open(banco_dados, 'r', encoding='utf=8') as arquivo:
            alunos = json.load(arquivo)
    else:
        alunos = []
    
    for aluno in alunos:
        print(f"ID: {aluno['ID']} | Nome: {aluno['Nome']} | Telefone: {aluno["Telefone"]} | Turma: {aluno['Turma']} | Idade: {aluno['Idade']} | CPF: {aluno['CPF']}")


def atualizar():
    print("\n-----ATUALIZAR DADOS-----")
    if not os.path.exists(banco_dados):
        print("Nenhum aluno cadastrado no sistema.")
        return
    
    with open(banco_dados, 'r', encoding='utf=8') as arquivo:
        alunos = json.load(arquivo)

    id_busca = int(input("Digite o ID do aluno que deseja alterar: "))

    for aluno in alunos:
        if aluno['ID'] == id_busca:
            print(f"Editando dados de: {aluno['ID']}")
            aluno['Nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['Telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone'] 
            aluno['Turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma'] 
            aluno['Idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade']) 
            aluno['Cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf'] 

            with open(banco_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(alunos, arquivo, indent=4, ensure_ascii=False)  
            print("Dados atualizados com sucesso!")
            return 
    
    print("Aluno não encontrado.")


def excluir():
    print("\n-----REMOVER ALUNO-----")
    if not os.path.exists(banco_dados):
        print("Nenhum aluno cadastrado no sistema.")
        return
    
    with open(banco_dados, 'r', encoding='utf=8') as arquivo:
        alunos = json.load(arquivo)

    aluno_busca = int(input("Digite o ID do aluno que deseja remover: "))

    nova_lista = [ a for a in alunos if a['ID'] != aluno_busca]
    
    if len (nova_lista) < len(alunos):
         with open(banco_dados, 'w', encoding='utf-8') as arquivo:
            json.dump(nova_lista, arquivo, indent=4, ensure_ascii=False)
         print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def menu():
    if not os.path.exists(banco_dados):
        with open(banco_dados, 'w', encoding='utf=8') as arquivo:
            json.dump([], arquivo)

    while True:
        print("\n----- SISTEMA ESCOLAR -----")  
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")  
        print("3. Atualizar dados do aluno") 
        print("4. Remover Aluno")  
        print("5. Sair") 

        opcao = input("Escolha umas das opções acima: ")

        if opcao == '1': cadastrar() 
        elif opcao == '2': listar() 
        elif opcao == '3': atualizar() 
        elif opcao == '4': excluir() 
        elif opcao == '5': break 
        else: print("Opção inválida!")

menu()
        

    



