cargo = input("Digite seu cargo: ")
codigo_de_acesso = int(input("Digite seu codigo de acesso: "))
botao_de_emergencia = input("Botao de emergencia pressionado?: ")
epi = input("EPI completo?: ")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo_de_acesso == 1234 or botao_de_emergencia == "sim") and epi == "sim":
    print("Acesso liberado.")
else:
    print("Acesso negado: Risco de segurança: ")