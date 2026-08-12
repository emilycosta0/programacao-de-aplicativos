def eh_par(numero):
    return numero % 2 == 0


def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)

def pode_votar(idade):
    
    if idade < 16:
        return "Não pode votar"
    elif idade < 18 or idade >= 70:
        return "Voto facultativo"
    return "Voto obrigatório"

assert eh_par(2) is True
assert eh_par(7) is False
assert eh_par(0) is True
assert eh_par(-4) is True

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 0) == 200
assert calcular_desconto(50, 100) == 0

assert pode_votar(15) == "Não pode votar"
assert pode_votar(16) == "Voto facultativo"
assert pode_votar(18) == "Voto obrigatório"
assert pode_votar(70) == "Voto facultativo"

print("Todos os testes passaram!")