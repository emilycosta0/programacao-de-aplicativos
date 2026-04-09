nomes = ["Emily", "Gabi", "Maria", "João"]

antigo = input("Qual nome você deseja mudar? ")
novo = input("Qual o novo nome? ")

for i in range(len(nomes)):
    if nomes[antigo] == antigo:
        nomes[novo] = nome_novo

print("Lista atualizada:", nomes)
