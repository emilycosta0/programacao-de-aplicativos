numeros = [3, 6, 5, 8, 9, 10]
numeros_impares = []
numeros_pares = []

for numero in numeros:
    if numero %2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Números pares: ", numeros_pares)
print("Números ímpares: ", numeros_impares)