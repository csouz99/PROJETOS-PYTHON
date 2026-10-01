def cadastrar_aluno(alunos):
    nome = input("Nome: ")
    matricula = input("Matricula: ")

    alunos.append([nome, matricula])

    print("Aluno cadastrado com sucesso!")


def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for contador in alunos:
            print("-------------------------")
            print("Nome:", contador[0])
            print("Matricula:", contador[1])


def editar_aluno(alunos):
    matricula = input("Digite a matricula do aluno: ")

    for contador in alunos:
        if contador[1] == matricula:
            contador[0] = input("Novo nome: ")

            print("Aluno atualizado com sucesso!")
            return

    print("Aluno não encontrado..")


def excluir_aluno(alunos):
    matricula = input("Digite a matricula do aluno: ")

    for contador in alunos:
        if contador[1] == matricula:
            alunos.remove(contador)

            print("Aluno excluido com sucesso!")
            return

    print("Aluno não encontrado.")
