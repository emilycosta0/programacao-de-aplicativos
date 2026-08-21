def eh_par(numero):
    return numero % 2 == 0


# o teste original está errado:
# assert eh_par(3) is True


# Teste corrigido:
assert eh_par(3) is False


# Resposta:
# O problema está no teste e não na função.
# O número 3 é ímpar, mas o resultado correto é False.