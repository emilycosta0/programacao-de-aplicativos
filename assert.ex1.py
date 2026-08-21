def dobrar(numero):
    return numero * 2


# previsão antes de executar:
# 1º assert: P
# 2º assert: F
# 3º assert: P

assert dobrar(3) == 6

# este teste falharia:
# assert dobrar(0) == 1

assert dobrar(-2) == -4


# O segundo assert falhou.
# Resultado real: dobrar(0) = 0.
# A expectativa estava incorreta porque 0 * 2 = 0, e não 1.