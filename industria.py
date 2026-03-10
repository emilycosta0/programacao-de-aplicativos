id = int(input("Qual seu ID?: "))
temperatura = float(input("Qual a temperatura?: "))
tempo_uso = int(input("Qual o tempo de uso?: "))

if (id % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"Funcionario {id}, você foi escalado para a manutenção preventiva hoje.")
else:
    print(f"Funcionario {id}, sua máquina opera dentro dos padrões normais.") 
    


