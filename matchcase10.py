menu = int(input("Digite um número de 1 a 4: "))

match menu:
    case 1:
        print("Tela de Cadastro")
    case 2:
        print("Tela de consulta")
    case 3:
        print("Tela de relatórios")
    case 4:
        print("Saindo do sistema...")
    case _:
        print("Opção incorreta!")