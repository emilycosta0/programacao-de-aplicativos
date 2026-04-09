ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

busca = input("Digite o nome da ferramenta que você procura: ")

encontrado = False

for indice, ferramenta in enumerate(ferramentas):
    if busca.lower() == ferramenta.lower():
        print(f"Peça encontrada na posição {indice}!")
        encontrado = True
        break

if not encontrado:
    print("Peça não encontrada.")
    
    while True:
        opcao = input("Deseja adicionar essa peça à lista? (s/n): ").lower()
        
        if opcao == "s":
            ferramentas.append(busca)
            print("Peça adicionada com sucesso!")
            break
        elif opcao == "n":
            print("Peça não adicionada.")
            break
        else:
            print("Digite apenas 's' ou 'n'.")

print("Lista final de ferramentas:", ferramentas)