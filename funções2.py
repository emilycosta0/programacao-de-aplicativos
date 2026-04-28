def senha_valida(senha):
    while len(senha) < 6:
        print("Senha inválida.")
        senha = input("Digite sua senha novamente: ")
    if len(senha) >= 6:
        print("senha cadastrada com sucesso!")