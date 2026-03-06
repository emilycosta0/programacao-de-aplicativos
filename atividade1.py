comprimento = input("O comprimento da peça esta entre 10cm a 12cm? (S/N):  ")

if comprimento == "S":
    largura = input("A largura esta entre 5cm e 6cm? (S/N): ")
    if largura == "S":  
        print("Peça aprovada!")
    else:
        print("Reprovado! Peça invalida.")
else:
    print("reprovado! Peça invalida.")




