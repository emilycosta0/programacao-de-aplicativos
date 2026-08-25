def buscar_nome(lista, nome):
    return nome in lista


def tem_senha_valida(senha):
    return len(senha) >= 8


# Testes para buscar_nome
assert buscar_nome(["Ana", "João", "Maria"], "Ana") is True
assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana"], "Ana") is True


# Testes para tem_senha_valida
assert tem_senha_valida("") is False
assert tem_senha_valida("1234567") is False
assert tem_senha_valida("12345678") is True


# Resposta:
# Ao buscar um nome em uma lista vazia, o resultado é False. Porque a lista não te nenhum nome
