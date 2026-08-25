def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado"

# Testes solicitados
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# Teste extra
assert situacao_aluno(6.1) == "Aprovado"

# Explicação:
# 6 e 5.9 são casos de limite porque estão próximos da nota
# mínima para aprovação. A média 6 é exatamente o limite e
# resulta em "Aprovado" enquanto 5.9 está logo abaixo do limite
# e resulta em "Reprovado"

# O teste extra escolhido foi 6.1 por que ele verifica uma média
# ligeiramente acima do limite e deve resultar em "Aprovado"
