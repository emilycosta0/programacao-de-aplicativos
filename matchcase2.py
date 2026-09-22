print("1- Café")
print("2- Chá")
print("3- Suco")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Você escolheu café.")
    case 2:
        print("Você escolheu chá.")
    case 3:
        print("Você escolheu suco.")
    case _:
        print("Opção inexistente!")