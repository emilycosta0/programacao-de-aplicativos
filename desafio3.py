saldo_inicial = 1000.0
nome = input("Digite seu nome:")
print("1 para depósito, 2 para saque e 3 para extrato")
menu_inicial = int(input("Digite uma das opções escolhidas: "))

if menu_inicial == 1:
    valor = float(input("Digite o valor: "))
    if valor > 0:
        valor_final = saldo_inicial + valor
        print("Seu saldo é:", valor_final)

elif menu_inicial == 2:
    valor = float(input("Digite o valor: "))
    if valor > 0 and (valor <= saldo_inicial or valor == 100.0):
        valor_final = saldo_inicial - valor
        print ("Valor final:", valor_final)

elif menu_inicial == 3:
    print("Seu extrato é:", saldo_inicial)

