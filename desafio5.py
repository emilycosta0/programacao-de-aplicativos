autorizados = ["alice","bob","carlos"]
nome = input("digite um nome de um pesquisador: ")

if nome in autorizados: 
    indice = autorizados.index(nome)
    print(f"O acesso permitido! o pesquisador {nome} está na posição {indice}")

    remover = input("Você gostaria de remover esse pesquisador da lista? (s/n): ")
    if remover == "s":
        autorizados.remove(nome)
        print(f"A lista atual {autorizados}")
    else:
        print(f"Acesso negado! O pesquisador {nome} não foi encontrado")
        cadastrar = input("Você gostaria de cadrastar este pesquisador? (s/n): ")
        if cadastrar == "s":
            autorizados.append(nome)
            print("O pesquisador foi cadrastado.")
            print(f"Nova lista {autorizados}")
        else:
            print("Nem uma alteração foi feita.")