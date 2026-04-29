def estar_na_lista (lista_nomes, busca):
    for nome in lista_nomes:
        if nome == busca:
            return "Encontrado!"
    return "Não disponível!"

lista_frutas =["maça", "banana", "morango", "uva"]
busca = input("Digite a fruta que você procura: ")
teste = estar_na_lista(lista_frutas, busca)
print(teste)