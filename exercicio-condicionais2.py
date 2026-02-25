poder_de_ataque = float(input("digite o seu poder de ataque: "))
ponto_de_defesa = float(input("digite o seu ponto de defesa: "))

subtracao = poder_de_ataque - ponto_de_defesa

if subtracao <= 0:
    print ("O vilao bloqueou o ataque!, dano 0")
elif subtracao > 0:
    print ("ataque critico! Voce causou dano ao vilao de ", subtracao)




