open('habitos.txt', 'w').close()

def mudar_habitos():
    novos_habitos = input("Digite um novo hábito: ")
    with open('habitos.txt', 'a') as arquivo:
        arquivo.write(novos_habitos + '\n')
        print("Novo hábito adicionado!")


def ler():
    with open('habitos.txt', 'r') as arquivo:
        habitos = arquivo.readlines() 

    h = 0

    for habito in habitos:
        print(f"{h} - {habito.strip()}")
        h += 1

def atualizar():
    ler()
    alterar_habitos = int(input("Digite os hábitos que deseja alterar: "))
    novo_habito = input("Novo hábito: ")

    with open('habitos.txt','r') as arquivo:
        linhas = arquivo.readlines()

    linhas[alterar_habitos] = novo_habito + '\n'

    with open('habitos.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
        print("Hábitos atualizados!")


def deletar():
    ler()
    alterar_habitos = int(input("Digite o hábito que deseja excluir: "))

    with open('habitos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    del linhas [alterar_habitos]

    with open('habitos.txt', 'w') as arquivo:
        arquivo.writelines(linhas)
    print("Hábito removido!")

while True:
    print("\n1-Adicionar | 2-Ver Todos | 3-Editar | 4-Excluir | 5-Sair" )
    opcao = input("Escolha uma das opções acima: ")

    if opcao == "1": mudar_habitos()
    elif opcao == "2": ler()
    elif opcao == "3": atualizar()
    elif opcao == "4": deletar()
    elif opcao == "5": break


