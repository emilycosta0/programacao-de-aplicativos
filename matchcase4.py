nota = input("Digite uma nota expressa em letra (A, B, C, D ou F): ")

match nota:
    case "A" | "B":
        print("Exelente desempenho!")
    case "C" | "D":
        print("Desempeho mediano.")
    case "F":
        print("Reprovado!")
    case _:
        print("Conceito inválido.")
    