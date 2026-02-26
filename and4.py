nome_de_usuario = input("digite seu nome: ")
codigo_secreto = int(input("digite seu codigo secreto: "))

if nome_de_usuario == "admin" and codigo_secreto == 999:
    print ("Acesso liberado! Sistema online.")
elif nome_de_usuario != "admin" and codigo_secreto != 999:
    print ("falha na autenticação! Alerta de segurança ligado. ")
    