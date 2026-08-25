def frete_gratis(valor):
    return valor >= 200


def pode_votar(idade):
    return idade >= 16


def senha_valida(senha):
    return len(senha) >= 8


# Frete grátis: abaixo, no limite e acima do limite
assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True


# Votação: abaixo, no limite e acima do limite
assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True


# Senha: 7, 8 e 9 caracteres
assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True


# Todos os testes devem passar
