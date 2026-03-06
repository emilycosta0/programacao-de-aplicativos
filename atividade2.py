curso = input("Você tem o curso de segurança completo S/N: ")

if curso == "S":
    pergunta = input("O instrutor está presente na sala?: ")
    if pergunta == "S":
        print("Acesso liberado: operação iniciada.")
    else:
        print("Aguarde o instrutor para ligar a máquina.")

else:
    print("Acesso negado: faça o treinamento.")