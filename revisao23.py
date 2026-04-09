notas = []

nota1 = float(input("Nota 1: "))
notas.append(nota1)
nota2 = float(input("Nota 2: "))
notas.append(nota2)
nota3 = float(input("Nota 3: "))
notas.append(nota3)
nota4 = float(input("Nota 4: "))
notas.append(nota4)

soma = 0
for nota in notas:
    soma = soma = nota

media = soma / 4

print("media", media)

if media >= 7:
    print("Aprovados")
elif media >= 5:
      print("Recuperação")
else:
      print("Reprovados")