from ligas import criar_tabelas, cadastrar_ligas, listar_ligas, atualizar_ligas, excluir_ligas
from arenas import criar_tabela, cadastrar_arenas, listar_arenas, atualizar_arenas, excluir_arenas

def menu():
    while True:
        try:
            print("\n--- SISTEMA DE TORNEIOS DE E-SPORTS ---")
            print("1 - Cadastrar Liga")
            print("2 - Listar Liga")
            print("3 - Atualizar Liga")
            print("4 - Excluir Liga")
            print("5 - Cadastrar Arena")
            print("6 - Listar Arena")
            print("7 - Atualizar Arena")
            print("8 - Excluir Arena")
            print("9 - Sair")

            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_ligas()

            elif opcao == 2:
                listar_ligas()

            elif opcao == 3:
                atualizar_ligas()

            elif opcao == 4:
                excluir_ligas()

            elif opcao == 5:
                cadastrar_arenas()

            elif opcao == 6:
                listar_arenas()

            elif opcao == 7:
                atualizar_arenas()

            elif opcao == 8:
                excluir_arenas()

            elif opcao == 9:
                print("Fechando o programa!")
                break

            else:
                print("Opção inválida, tente novamente!")

        except ValueError:
            print("Digite apenas números!")


criar_tabelas()
menu()


