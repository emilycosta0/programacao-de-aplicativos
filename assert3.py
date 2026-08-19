def calcular_desconto(preco, prcentual):
    return preco - (preco * prcentual / 100)

assert calcular_desconto(100, 0) == 100
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(100, 50) == 50
assert calcular_desconto(100, 100) == 0
assert calcular_desconto(49.90, 10) == 44.91