def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# teste extra
assert situacao_aluno(5) == "Reprovado"


# Resposta:
# 6 e 5.9 são casos de limite porque 6 é o valor minimo
# para ser aprovado e 5.9 está imediatamente abaixo desse limite.