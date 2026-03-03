media = float(input("Digite sua media: "))
renda = float(input("Digite sua renda: ")) 
escola = input("Escola publica ou privada: ")

if media >= 8.0 and (renda <= 2000.00 or escola == "publica" ):
    print("Ganhou a bolsa.")
else:
    print("Não atende os requisitos.")
