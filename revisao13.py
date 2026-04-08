lista_secreta = ["888"]
tentativas = 0
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("Digite a senha: ")
    
    if palpite in lista_secreta:
        print("Senha correta!")
        acertou = True
    else:
        print("Senha incorreta!")
    
    tentativas += 1
if not acertou:
    print("Suas tentativas acabaram!")
    print("A senha correta era:", lista_secreta)

