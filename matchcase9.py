codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1 | 2:
        print("Alimentos não perecíveis")
    case 3 | 4:
        print("Bebidas")
    case 5:
        print("Produtos de limpeza")
    case _:
        print("Código não cadastrado!")