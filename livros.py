def cadastrar_livro(biblioteca):
    codigo = input("Código: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    quantidade = int(input("Quantidade: "))

    biblioteca.append([codigo, titulo, autor, ano, quantidade])

    print("Livro cadastrado com sucesso!")


def listar_livros(biblioteca):
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for contador in biblioteca:
            print("-------------------------")
            print("Código:", contador[0])
            print("Título:", contador[1])
            print("Autor:", contador[2])
            print("Ano:", contador[3])
            print("Quantidade:", contador[4])


def editar_livro(biblioteca):
    codigo = input("Digite o código do livro: ")

    for contador in biblioteca:
        if contador[0] == codigo:
            contador[1] = input("Novo título: ")
            contador[2] = input("Novo autor: ")
            contador[3] = int(input("Novo ano: "))
            contador[4] = int(input("Nova quantidade: "))

            print("Livro atualizado com sucesso!")
            return

    print("Livro não encontrado.")


def excluir_livro(biblioteca):
    codigo = input("Digite o código do livro: ")

    for contador in biblioteca:
        if contador[0] == codigo:
            biblioteca.remove(contador)

            print("Livro excluído com sucesso!")
            return

    print("Livro não encontrado.")
