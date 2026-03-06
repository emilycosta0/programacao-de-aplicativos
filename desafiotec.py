codigo = int(input("Digite o código do drone: "))
autorização = input("O drone possui autorização para pousar?: ")

if codigo == 999 or autorização == "S":
    print("Drone autorizado para pousar.")

    print("-------------------------")

    bateria = int(input("Qual a bateria do drone?: "))
    clima = input("Qual o clima do dia?: ")
    vento = int(input("Qual a velocidade do vento?: "))

    if bateria <= 10:
        print("Drone autorizado para pousar!")
    elif (bateria >= 10 and clima == "Ensolarado" and vento < 30) or (clima == "Chuvoso" and vento < 10):
        print("POUSO AUTORIZADO: INICIADO DESCIDA.")
    else:
        print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita")

else:
    print("ERRO 01: Drone não identificado. Retornando à base.")
