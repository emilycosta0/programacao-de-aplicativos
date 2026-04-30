vida_inicial = 100
def sofrer_dano (vida_inicial, valor_dano):
    
    
    while vida_inicial > 0:
        if valor_dano > vida_inicial:
            return " Dano critico: Game Over"
        vida_inicial -= valor_dano
        print(vida_inicial)
        valor_dano = int(input("Qual o dano que o mostro causou?: "))
    return "Game Over"

valor_dano = int(input("Digite seu dano: "))
final = sofrer_dano(vida_inicial, valor_dano)
print(final)
 


