sigla = input("Digite uma sigla: ")

match sigla:
    case "PR":
        print("Paraná.")
    case "SC":
        print("Santa Catarina.")
    case "RS":
        print("Rio Grande do Sul.")
    case _:
        print("Estado fora da região Sul!")