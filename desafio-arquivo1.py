open('viagens.txt', 'w').close()

def criar_destino():
    viagem = input("Digite a cidade que você deseja conhecer: ")
    with open('viagens.txt', 'a') as arquivo:
        arquivo.write(viagem + '\n')
        print("Destino adicionado!")


def ler():
    with open('viagens.txt', 'r') as arquivo:
        lugares = arquivo.readlines()

    i = 0

    for lugar in lugares:
        print(f"{i} - {lugar.strip()}")
        i += 1

def atualizar():
    ler()
    alterar_destino = int(input("Digite o destino que você deseja alterar: "))
    novo_destino = input("Novo destino: ")

    with open('viagens.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    linhas[alterar_destino] = novo_destino + '\n'

    with open('viagens.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
        print("Destino atualizado!")


def deletar():
    ler()
    alterar_destino = int(input("Digite o destino que deseja excluir: "))

    with open('viagens.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    del linhas[alterar_destino]

    with open('viagens.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    print("Destino removido!")


while True:
    print("\n1-Adicionar Destino | 2-Listar Sugestões | 3-Editar Sugestões | 4-Remover Sugestão | 5-Sair ")
    opcao = input("Escolha uma das opções acima: ")

    if opcao == '1': criar_destino()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break 

