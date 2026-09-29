alunos = []

def cadastrar_alunos ():
    nome = input ("Aluno: ")
    matricula = input ("Matricula: ")
    alunos.append([nome,matricula])
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    for contador in alunos:
    print("Aluno: ",contador[0])