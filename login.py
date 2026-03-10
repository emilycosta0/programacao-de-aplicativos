senha = input("Qual a sua senha?: ")
tentativas = int(input("Qual o número de tentativas?: "))
token = input("Você possui TOKEN? Digite S ou N: ")

if senha == "admin123" or (tentativas % 3 == 0 or token == "S"):
    print(f"Tentativa n° {tentativas}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa n° {tentativas}: ACESSO BLOQUEADO POR PROTOCOLO.")