numeros = int(input("Digite um numero para ver a tabuada: "))
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"tabuada do {numeros}")

for numero in lista_numeros:
    resultado = numeros * numero
    print(f"{numeros} x {numero} = {resultado}")

