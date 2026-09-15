# 1-BUSCA SEQUENCIAL EM UM VETOR DE 10 POSIÇÕES
def busca_sequencial():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número que deseja procurar: "))

    for i in range(len(vetor)):
        if vetor[i] == numero:
            print("Número encontrado no índice:", i)

    print("Número não encontrado!")

busca_sequencial()

# 2-CONTAR QUANTAS VEZES UM VALOR APARECE
def contar_valor():
    vetor = [10, 20, 10, 30, 10, 40, 50, 10]

    numero = 0

    for i in range(len(vetor)):
        if vetor[i] == numero:
            contador += 1

    print("O número aparece", contador, "vezes.")

contar_valor()

# 3-ENCONTRAR O MAIOR NUMERO E SUA POSIÇÃO
def maior_numero():
    vetor = [15, 8, 32, 45, 12, 60, 25]

    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[1] > maior:
            maior = vetor[i]
            posicao = i

    print("Maior número:", maior)
    print("Posição:", posicao)

maior_numero()

# 4-BUSCAR UM NOME NA LISTA DE ALUNOS
def buscar_aluno():
    alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]

    nome = input("Digite o nome do aluno: ")

    encontrado = False

    for i in range(len(alunos)):
        if alunos[i] == nome:
            encontrado = True
            break

    if encontrado:
        print("Aluno encontrado!")
    else:
        print("Aluno não encontrado!")

buscar_aluno()

# 5-PRIMEIRA E ULTIMA POSIÇÃO DE UM NUMERO REPETIDO
def primeira_ultima_posicao():
    vetor = [5, 10, 20, 10, 30, 10, 40, 50]

    numero = int(input("Digite o número: "))

    primeira = -1
    ultima = -1

    for i in range(len(vetor)):
        if vetor[i] == numero:

            if primeira == -1:
                primeira = i

            ultima = i

    if primeira != -1:
        print("Primeira posição: ", primeira)
        print("Última posição: ", ultima)
    else:
        print("Número não encontrado!")

primeira_ultima_posicao()

# 6-BUSCA BINARIA
def busca_binaria():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número que deseja procurar: "))
    
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == numero:
            print("Número encontrado no índice:", meio)
            return

        elif numero > vetor[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Número não encontrado!")

busca_binaria()

# 7-BUSCA BINARIA DE UMA PALAVRA
def buscar_palavra():
    palavras = ["emily", "mayra", "bianca", "gabi", "paloma", "lara" ]

    palavra = input("Digite a palavra: ").lower()
     
    inicio = 0
    fim = len(palavras) - 1
    
    while inicio <= fim:

        meio = (inicio + fim) // 2

        if palavras[meio] == palavra:
            print("Palavra encontrada!")
            return

        elif palavra > palavras[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Palavra não encontrada!")

buscar_palavra()

# 8-BUSCA BINARIA CONTANDO AS COMPARAÇÕES
def busca_binaria_comparacoes():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número: "))

    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if vetor[meio] == numero:
            print("Número encontrado no índice:", meio)
            print("Quantidade de comparações:", comparacoes)
            return 

        elif numero > vetor[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Número não encontrado!")
    print("Quantidade de comparações:", comparacoes)

busca_binaria_comparacoes()

# 9-DESCOBRIR A POSIÇÃO ONDE UM NUMERO DEVE SER INSERIDO
def posicao_insecao():
    vetor = [10, 20, 30, 40, 50, 60]

    numero = int(input("Digite o número que deseja inserir: "))

    inicio = 0
    fim = len(vetor)

    while inicio < fim:

        meio = (inicio + fim) // 2

        if vetor[meio] < numero:
            inicio = meio + 1

        else:
            fim = meio

    print("O número deve serinserido na posição:", inicio)

posicao_insecao()

# 10- COMPARAR BUSCA SEQUENCIAL E BUSCA BINARIA
def busca_sequencial(vetor, numero):
    comparacoes = 0

    for i in range(len(vetor)):

        comparacoes += 1

        if vetor[1] == numero:
            return i, comparacoes

    return -1, comparacoes 

def busca_binaria(vetor, numero):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:

        meio = (inicio + fim) // 2

        comparacoes += 1

        if vetor[meio] == numero:
            return meio, comparacoes

        elif numero > vetor[meio]:
            inicio = meio + 1

        else:
            fim = meio - 1

    return - 1, comparacoes

def comparar_buscas():

    vetor = []

    for i in range(1, 101):
        vetor.append(i)

    valores = [1, 50, 100]

    for numero in valores:
        indice_sequencial, comparacoes_sequencial = busca_sequencial(
            vetor, numero
        )

        indice_binaria, comparacoes_binaria = busca_binaria(
            vetor, numero
        )

        print("\nNúmero procurado:", numero)

        print("Busca sequencial:")
        print("Índice:", indice_sequencial)
        print("Comparações:", comparacoes_sequencial)

        print("Busca binária:")
        print("Índice:", indice_binaria)
        print("Comparações:", comparacoes_binaria)


comparar_buscas()
