def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"


assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável"
assert classificar_temperatura(16) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(26) == "Quente"


# Resposta:
# O teste com 15 verifica o limite inferior
# Como 15 está dentro do intervalo de 15 até 25, o resultado esperado é 'Agradável'
