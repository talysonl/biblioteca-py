from livro.livro_buscar import buscarPorCodigo
from livro.livro_editar import editarLivro
from livro.livro_listar import listarLivros
from livro.livro_deletar import deletarLivro
from livro.livro_registrar import registrarLivro

def menu() -> None:
    while True:
        print("---- Bem Vindo ao menu ---- ")
        print("1 - Adicionar Livro")
        print("2 - Editar Livro")
        print("3 - Deletar Livro")
        print("4 - Buscar por Código")
        print("5 - Listar todos")
        print("6 - Sair")
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            titulo = input('Digite o titulo: ')
            autor = input('Digite o Autor:')
            registrarLivro(titulo, autor)
        elif opcao == "2":
            codigo = int(input("Digite o código do livro: "))
            titulo = input('Digite o titulo: ')
            autor = input('Digite o Autor:')
            editarLivro(codigo, titulo, autor)
        elif opcao == "3":
            codigo = int(input('Digite o Autor: '))
            deletarLivro(codigo)
        elif opcao == "4":
            codigo = int(input("Busque um livro pelo codigo: "))
            print(buscarPorCodigo(codigo))
        elif opcao == "5":
            listarLivros()
        elif opcao == "6":
            break
        else:
            print("Opção Invalida!")