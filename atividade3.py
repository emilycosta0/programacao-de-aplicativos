temperatura = float(input("Qual a temperatura atual da estufa?:  "))

if temperatura <= 30:
    print("Clima estável.")
else:
    print("Alerta de calor!")

umidade = float(input("Digite a umidade da estufa: "))

if umidade <= 40:
    print("Ação: Ligar Irrigação!")
else:
    print("Ação: Ligar apenas ventiladores")