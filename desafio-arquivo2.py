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