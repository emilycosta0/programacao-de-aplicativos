valor_total = float(input("Digite o valor total da compra: "))
cliente = input("você é Prime?: ")
frete = 50.00

if valor_total >= 500.00 or (cliente == "sim" and valor_total >= 100.00):
    print("Parabéns você ganhou frete grátis")
    frete = 0.0
    print("Valor total", valor_total)

valor_total = valor_total = frete
print("Valor total", valor_total)


    
