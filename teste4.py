def eh_par(numero):
    return numero % 2 == 0


assert eh_par(3) is True


# Correção:
# O problema está no teste e não na função
# A função está correta pois 3 é um número ímpar
# Mas o eh_par(3) retorna False
#
# O teste correto é:
assert eh_par(3) is False

# R:
# O número 3 não é divisível por 2 então ele é ímpar
# Por isso, a função retorna False e o teste corrigido passa

