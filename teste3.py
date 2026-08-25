# Testes para encontrar o erro

def calcular_desconto(preco, percentual):
    return preco - percentual


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45


# A função estava errada porque estava apenas subtraindo o
# percentual do preço. O correto é calcular a porcentagem


# Função corrigida
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


# Testes novamente após a correção
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# Depois da correção todos os testes passam
