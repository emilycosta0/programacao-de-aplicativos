def analisar_desempenho (nota):

    if nota >=9:
        return("Exelente!")
    elif nota >=7:
        return("Bom")
    elif nota >5:
        return("Regular")
    else:
        return("Insuficiente!")
    
nota_usuario = int(input("Digite sua nota: "))
mensagem = analisar_desempenho(nota_usuario)
print(mensagem)