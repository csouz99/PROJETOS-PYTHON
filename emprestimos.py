from datetime import date


def realizar_emprestimo(emprestimos, biblioteca, alunos):
    codigo = input("Código do livro: ")

    for livro in biblioteca:
        if livro[0] == codigo:

            if livro[4] > 0:
                matricula = input("Matrícula do aluno: ")

                for aluno in alunos:
                    if aluno[1] == matricula:
                        data_emprestimo = date.today()

                        emprestimos.append([codigo, matricula, data_emprestimo])
                        livro[4] = livro[4] - 1

                        print("Empréstimo realizado com sucesso!")
                        return
                print("Aluno não encontrado.")
                return
            
            else:
                print("Livro indisponivel.")
                return

    print("Livro não encontrado.")


def listar_emprestimos(emprestimos):
    if len(emprestimos) == 0:
        print("Nenhum empréstimo cadastrado.")
    else:
        for contador in emprestimos:
            print("-------------------------")
            print("Código do livro:", contador[0])
            print("Matricula do aluno:", contador[1])
            print("Data:", contador[2])


def editar_emprestimo(emprestimos, alunos):
    codigo = input("Codigo do livro: ")
    matricula = input("Matricula atual do aluno: ")

    for contador in emprestimos:
        if contador[0] == codigo and contador[1] == matricula:

            nova_matricula = input("Nova matricula: ")

            for aluno in alunos:
                if aluno[1] == nova_matricula:
                    contador[1] = nova_matricula

                    print("Emprestimo atualizado com sucesso!")
                    return

            print("Nova matricula não encontrada.")
            return

    print("Emprestimo não encontrado.")


def excluir_emprestimo(emprestimos, biblioteca):
    codigo = input("Codigo do livro: ")
    matricula = input("Matricula do aluno: ")

    for contador in emprestimos:
        if contador[0] == codigo and contador[1] == matricula:

            for livro in biblioteca:
                if livro[0] == codigo:
                    livro[4] = livro[4] + 1

            emprestimos.remove(contador)

            print("Emprestimo excluido com sucesso!")
            return

    print("Emprestimo não encontrado.")
