# sistema para biblioteca
# Requisitos Funcionais
# 1. O sistema deve permitir o cadastro de um livro com título, autor, gênero, quantidade e
# código.
# 2. O sistema deve permitir a busca de um livro pelo código e retornar suas informações.
# 3. O sistema deve permitir a atualização do estoque de um livro específico.
# 4. O sistema deve possibilitar a remoção de um livro através de seu código.
# 5. O sistema deve listar todos os livros cadastrados no sistema.






def cadastro_livro(lista, titulo, autor, genero, quantidade, codigo):
    lista.append({'Código': codigo, 'Título' : titulo, 'Autor' : autor, 'Gênero' : genero, 'Quantidade' : quantidade})
    print(f'O livro {titulo}, foi cadastrado.')

def busca_livro(lista, codigo):
    for livro in lista:
        if livro['Código'] == codigo:
            for chave, valor in livro.items():
                print(f'{chave} : {valor}')
            return
        
        print('Livro não encontrado')

def remover_livro(lista, codigo): 
    for livro in lista:
        if livro['Código'] == codigo:
            lista.remove(livro)
            print('Livro removido.')

def mudar_estoque(lista, codigo, quantidade):
    for livro in lista:
        if livro['Código'] == codigo:
            livro['Quantidade'] -= quantidade
            print('Quantidade atualizada')


def lista_livros(lista):
    for livro in lista:
        for chave, valor in livro.items():
            print(f'{chave} : {valor}')
        print('-'*40)


def menu():
    livros = []

    while True:
        print('-='*20)
        print('Menu de Gerenciamento Bibliotecário')
        print('=-'*20)
        print('1 - Cadastrar Livro')
        print('2 - Listar Livros')
        print('3 - Buscar Livro')
        print('4 - Atualizar Estoque')
        print('5 - Excluir Livro')
        print('6 - Sair')
        print('-'*40)
        escolha = int(input('Escolha uma opção: '))

        if escolha == 1:
            titulo = input('Digite o título do livro: ')
            autor = input('Digite o autor do livro: ')
            genero = input('Digite o gênero do livro: ')
            quantidade = input('Digite a quantidade de exemplares: ')
            codigo = input('Digite o código do livro: ')

            cadastro_livro(livros,titulo, autor, genero, quantidade, codigo)

        if escolha == 2:
            lista_livros(livros)

        if escolha == 3:
            codigo = input('Digite o código do livro: ')
            busca_livro(livros, codigo)

        if escolha == 4:
            codigo = input('Digite o código do livro: ')
            quantidade = input('Digite a nova quantidade de exemplares: ')
            mudar_estoque(livros, codigo, quantidade)
        
        if escolha == 5:
            codigo = input('Digite o código do livro para exclusão: ')
            remover_livro(livros, codigo)
        
        if escolha == 6:
            print('Programa encerrado.')
            break



menu()


# cadastro_livro(livros, 'abc', 'douglas', 'drama', 2, 1)
# # mudar_estoque(livros,1,1)

# # busca_livro(livros, 1)
# lista_livros(livros)