usuario = input("Digite seu nome de usuario: ")
senha = int(input("Digite sua senha: "))

if (usuario == "admin" or usuario == "root") and senha == 12345:
    print("Acesso liberado!")

