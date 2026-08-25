# Função escolhida: calcular_desconto
# Regra encontrada: o desconto deve ser calculado como uma porcentagem
# do preço, e não apenas subtraído diretamente

# FUNÇÃO ORIGINAL (com erro)
def calcular_desconto(preco, percentual):
    return preco - percentual


# TESTES CRIADOS
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45


# Os testes mostram que a função está errada
# Por exemplo: 10% de R$ 100 é R$ 10, então o resultado deve ser R$ 90


# FUNÇÃO CORRIGIDA
def calcular_desconto(preco, percentual):
    return preco - (preco * percentual / 100)


# TESTES NOVAMENTE
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45


# Explicação:
# A função original subtraía o percentual diretamente do preço
# A correção foi calcular primeiro o valor correspondente à
# porcentagem e depois subtraí-lo do preço

# Ex:
# calcular_desconto(100, 10) retorna 90, pois 10% de 100 é 10
# e 100 - 10 = 90