def menu(): 
	while True: 
        print("1. Cadastrar Aluno") 
        print("2. Sair") 
        opcao = input("Escolha: ") 
         
        if opcao == "1": 
            print("Cadastrando...") 
        elif opcao == "2": 
            print("Saindo do programa.") 
        	# Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 
            break
            
# R= o erro é que o 'pass' não interrompe o while, tem que usar o break para sair do loop e fechar o menu