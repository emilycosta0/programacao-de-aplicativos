# Função original com erro

def calcular_desconto(preco, percentual):
    return preco - percentual


# Testes que revelam o problema:

# assert calcular_desconto(100, 10) == 90
# Este passa por coincidência.

# assert calcular_desconto(200, 20) == 160
# Este nao daria certo, por que o resultado seria 180

# assert calcular_desconto(50, 10) == 45
# Este nao daria certo , por que o resultado seria 40


# Função corrigida

def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45


# Resposta:
# O erro estava na função original
# Ela subtraía o percentual diretamente do preço
# A correção calcula primeiro o valor do desconto em porcentagem