nome = input("Digite seu nome: ")
valor_total_da_compra = float(input("Digite o valor total da compra: "))
distancia_de_entrega = int(input("Digite a distância de entrega: "))
cupom = input("Digite seu cupom: ")
frete = 40.00

if valor_total_da_compra >= 1000 and cupom == "S":
   multiplicacao = valor_total_da_compra * 0.20
   valor_com_desconto = multiplicacao - valor_total_da_compra
   print ("Parabéns! Você ganhou um mouse pad Gamer de brinde. ")

elif valor_total_da_compra > 500 and valor_total_da_compra < 1000.00 == "S":
    multiplicacao = valor_total_da_compra * 0.10
    valor_com_desconto = valor_total_da_compra - multiplicacao 

elif distancia_de_entrega <= 50 and valor_total_da_compra > 200.00:
    frete = 0.00
    valor_com_desconto = valor_total_da_compra + frete
else:
    valor_total_da_compra = valor_com_desconto + frete

print ("Olá", nome)
print ("O valor total da compra é ", valor_total_da_compra )
print ("Valor com desconto ", cupom )
print ("Valor final da compra ", valor_total_da_compra )

