def pode_votar(idade):
    return idade >= 16


# Testes de limite
assert pode_votar(15) is False
assert pode_votar(16) is True

# Teste extra: valor imediatamente acima do limite
assert pode_votar(17) is True

# Explicação:
# Os testes 15 e 16 são os mais importantes porque verificam exatamente onde a regra muda
# Com 15 anos, a pessoa não pode votar
# Com 16 anos, a pessoa pode votar
# O teste com 17 anos verifica que a regra continua funcionando depois do limite
