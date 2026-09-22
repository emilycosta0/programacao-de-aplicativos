letra = input("Digite uma vogal: ")

match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("È uma vogal.")
    case _:
        print("Não é uma vogal!")