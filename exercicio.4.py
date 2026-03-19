vagas = ["Ocupado","Livre","Ocupado","Livre"]
indice = int(input("Digite um número de 0 á 3: "))

if indice % 2 == 0 and vagas == "Livre":
    print(f"Vaga {indice} autorizada para estacionar.")

else:
    print(f"Vaga {indice} indisponível ou fora das regras.")
