def aplicar_promocao(lista_precos, nova_lista):
    for preco in lista_precos:
        if preco >= 100.00: 
            desconto = preco * 0.15
            novo_valor = preco - desconto 
            nova_lista.append(novo_valor)
        nova_lista.append(preco)
    return nova_lista

lista_compras =[150.0, 80.0, 200.0, 50.0]
lista = []
mensagem = aplicar_promocao(lista_compras, lista)
print(mensagem)

        

