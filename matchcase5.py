num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+ ou -): ")

match operacao:
    case "+":
        print("Resultado:", num1 + num2)
    case "-":
        print("Resultado:", num1 - num2)
    case _:
        print("Operação inválida!")
        