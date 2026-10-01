from livros import cadastrar_livro, listar_livros, editar_livro, excluir_livro
from alunos import cadastrar_aluno, listar_alunos, editar_aluno, excluir_aluno
from emprestimos import realizar_emprestimo, listar_emprestimos, editar_emprestimo, excluir_emprestimo


biblioteca = []
alunos = []
emprestimos = []


while True:

    print("\n==============================")
    print("          BIBLIOTECA          ")
    print("==============================")
    print("1 - Livros")
    print("2 - Alunos")
    print("3 - Empréstimos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        while True:

            print("\n----- LIVROS -----")
            print("1 - Cadastrar livro")
            print("2 - Listar livros")
            print("3 - Editar livro")
            print("4 - Excluir livro")
            print("0 - Voltar")

            opcao_livro = input("Escolha uma opção: ")

            if opcao_livro == "1":
                cadastrar_livro(biblioteca)

            elif opcao_livro == "2":
                listar_livros(biblioteca)

            elif opcao_livro == "3":
                editar_livro(biblioteca)

            elif opcao_livro == "4":
                excluir_livro(biblioteca)

            elif opcao_livro == "0":
                break

            else:
                print("Opção inválida!")


    elif opcao == "2":

        while True:

            print("\n----- ALUNOS -----")
            print("1 - Cadastrar aluno")
            print("2 - Listar alunos")
            print("3 - Editar aluno")
            print("4 - Excluir aluno")
            print("0 - Voltar")

            opcao_aluno = input("Escolha uma opção: ")

            if opcao_aluno == "1":
                cadastrar_aluno(alunos)

            elif opcao_aluno == "2":
                listar_alunos(alunos)

            elif opcao_aluno == "3":
                editar_aluno(alunos)

            elif opcao_aluno == "4":
                excluir_aluno(alunos)

            elif opcao_aluno == "0":
                break

            else:
                print("Opção inválida!")


    elif opcao == "3":

        while True:

            print("\n----- EMPRÉSTIMOS -----")
            print("1 - Realizar empréstimo")
            print("2 - Listar empréstimos")
            print("3 - Editar empréstimo")
            print("4 - Excluir empréstimo")
            print("0 - Voltar")

            opcao_emprestimo = input("Escolha uma opção: ")

            if opcao_emprestimo == "1":
                realizar_emprestimo(emprestimos,biblioteca,alunos)

            elif opcao_emprestimo == "2":
                listar_emprestimos(emprestimos)

            elif opcao_emprestimo == "3":
                editar_emprestimo(emprestimos,alunos)

            elif opcao_emprestimo == "4":
                excluir_emprestimo(emprestimos,biblioteca)

            elif opcao_emprestimo == "0":
                break

            else:
                print("Opção inválida!")


    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")