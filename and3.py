nivel_atual = int(input("digite seu nivel atual: "))
quantidade_de_esferas_coletadas = int(input("digite sua quantidade de esferas coletadas: "))

if nivel_atual >= 20 and quantidade_de_esferas_coletadas > 50:
    print ("Habilidade super salto desbloqueada.")
elif nivel_atual < 20 and quantidade_de_esferas_coletadas <= 50:
    print ("Requisitos insuficientes para nova habilidade.")
    