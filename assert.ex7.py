# Função escolhida: classificação de idade
# Regra: 18 anos ou mais = Maior de idade


# Função original com erro
def classificar_idade(idade):
    if idade > 18:
        return "Maior de idade"
    return "Menor de idade"


# Testes criados:
# O teste abaixo falharia porque 18 deveria ser maior de idade
#
# assert classificar_idade(18) == "Maior de idade"

assert classificar_idade(17) == "Menor de idade"
assert classificar_idade(19) == "Maior de idade"


# Função corrigida
def classificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"


# Testes depois da correção

assert classificar_idade(17) == "Menor de idade"
assert classificar_idade(18) == "Maior de idade"
assert classificar_idade(19) == "Maior de idade"


# Resposta:
# Função escolhida: classificação de idade
# Regra encontrada: 18 anos também deve ser considerado maior de idade
# O erro era utilizar > em vez de >=