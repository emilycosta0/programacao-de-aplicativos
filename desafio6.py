livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
escolha = input("Digite o livro que você deseja: ")

if escolha in livros_disponiveis:
    livros_disponiveis.remove(escolha)
    livros_emprestados.append(escolha)
else:
    print("Desculpe, este livro não está no acervo.")

devolucao = input("Digite o nome do livro que está devolvendo: ")
if devolucao in livros_emprestados: 
    livros_emprestados.remove(devolucao)
    livros_disponiveis.append(devolucao)
else:
    print("Este livro não consta como emprestado.")
    
del livros_emprestados[0:2]

print(f"Estado final das duas listas {livros_disponiveis} e {livros_emprestados}.")