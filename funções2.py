def validar_senha(senha):
    while len(senha) < 6:
        print("Senha inválida.")
        senha = input("Digite sua senha novamente: ")
    if len(senha) >= 6:
        print("Senha cadastrada com sucesso.")

senha_usuario = input("Digite sua senha: ")
validar_senha(senha_usuario)