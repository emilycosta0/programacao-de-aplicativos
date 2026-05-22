import json

def criar_arquivo():
    open("alunos.json", 'w').close()

def listar_dados(dados):
    with open("alunos.json", 'r') as arquivo:
        json.dump(dados,arquivo,indent=4)


def cadatrar_aluno(dados,cpf):
    dados = listar_dados()
    nome = input("Digite o nome completo do aluno: ")
    telefone = int(input("Digite o telefone do aluno: "))
    turma = input("Digite a turma do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = int(input("Digite o CPF do aluno: "))


    aluno = {
        "nome": nome,
        "tlefone": telefone,
        "turma": turma,
        "idade": idade,
        "cpf": idade
    }


def listar_alunos():
    with open("alunos.json",'r') as arquivo:
        dados = json.load(arquivo)
print()


def atualizar_dados():
    with open("alunos.json", 'r') as arquivo:
        dados = json.load(arquivo)
        dados['telefone']


def remover_aluno():
    with open("alunos.json", 'r') as arquivo:
        dados = json.load(arquivo)
    if 'cpf' in dados:
        del dados ['cpf']
        print("Campo 'CPF' removido com sucesso")
    with open("alunos.json", 'w',encoding='utf-8') as arquivo:
        json.dump(dados,arquivo,indent=4,ensure_ascii=False)