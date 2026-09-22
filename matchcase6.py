dia = input("Digite um dia da semana: ")

match dia:
    case "Sábado" | "Domingo":
        print("Fim de semana")
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
        print("Dia útil.")
    case _:
        print("Texto inválido!")