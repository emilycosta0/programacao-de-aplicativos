carrinho = []
item = ""
while item != "Fim":
    item = input("Produto:" )
    if item != "Fim":
        carrinho.append(item)
for produto in carrinho:
    print(produto)