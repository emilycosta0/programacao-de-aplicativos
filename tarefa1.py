numeros = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]
numeros_impares = []
numeros_pares = []

for numero in numeros:
    if numero %2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)