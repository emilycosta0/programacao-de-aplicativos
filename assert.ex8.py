def pode_votar(idade):
    return idade >= 16


# Testes de limite

assert pode_votar(15) is False
assert pode_votar(16) is True

# Teste adicional

assert pode_votar(17) is True


# Resposta:
# Os testes 15 e 16 são importantes porque verificam exatamente a mudança da regra no limite de 16 anos

