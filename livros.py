biblioteca = []

def cadastrar_livros():
    codigo = input("Código: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input ("Ano: ")
    biblioteca.append([codigo,titulo,autor, ano])
    print ("Livro cadastrado com sucesso!")

def listar_livros():
    for contador in biblioteca:
           print("Código: ", contador[0])
           print("Título: ", contador[1])
           print("Autor: ", contador[2])
           print("Ano: ", contador[3])
           print("Quantidade: ", contador[4])
           print("----------------------")
