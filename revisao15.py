alunos = ["emily", "gabi", "joão", "arthur", "gustavo"]
notas = [80, 70, 100, 95, 55]
for nota in notas:

    if nota >= 60:
        indice = notas.index(nota)
        print(alunos[indice])
print(f"nova atual: {alunos}")
