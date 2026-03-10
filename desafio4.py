garrafas = int(input("Qual o número de garrafas que passaram pela esteira?: "))

if garrafas % 500 == 0:
    print("Hora da limpeza: Parar a máquina imediatamente!")

elif garrafas % 100 == 0:
    print("Qualidade: Retire a amostra para teste!")

elif garrafas == 500:
    print("Hora da limpeza: Parar a máquina imediatamente!")
    print("Qualidade: Retire a amostra para teste!")

else:
    print(f"Produção em dia, Garrafas número {garrafas} processadas.")