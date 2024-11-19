def ordenar_livros(livros, opcao, ordem):
    if len(livros) == 0:
        print("Nenhum livro cadastrado para ordenar.")
        return
        
    if opcao == "1":
        chave = "ano"
    elif opcao == "2":
        chave = "paginas"
    else:
        print("Opção inválida de ordenação!")
        return

    def partition(livros, low, high, chave, ordem):
        pivot = livros[high][chave]
        i = low - 1  # Índice do menor elemento
        for j in range(low, high):
            if (ordem == "C" and livros[j][chave] <= pivot) or (ordem == "D" and livros[j][chave] >= pivot):
                i += 1
                livros[i], livros[j] = livros[j], livros[i]  
        livros[i + 1], livros[high] = livros[high], livros[i + 1]
        return i + 1

    def quicksort(livros, low, high, chave, ordem):
        if low < high:
            pi = partition(livros, low, high, chave, ordem)
            quicksort(livros, low, pi - 1, chave, ordem)  
            quicksort(livros, pi + 1, high, chave, ordem) 

    quicksort(livros, 0, len(livros) - 1, chave, ordem)

    print("Livros ordenados com sucesso!")
    listar_livros(livros)

def listar_livros(livros):
    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(livros, 1):
            print(f"{i}. Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Páginas: {livro['paginas']}")

def adicionar_livro(livros, titulo, autor, ano, paginas):
    try:
        livro = {"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas}
        livros.append(livro)
        print("Livro adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar o livro: {e}")

def salvar_livros(livros):
    try:
        with open("biblioteca.txt", "w") as f:
            for livro in livros:
                f.write(f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n")
        print("Os dados foram salvos no arquivo 'biblioteca.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_livros():
    livros = []
    try:
        with open("biblioteca.txt", "r") as f:
            for linha in f:
                dados = linha.strip().split(",")
                if len(dados) == 4:
                    try:
                        titulo = dados[0]
                        autor = dados[1]
                        ano = int(dados[2])
                        paginas = int(dados[3])
                        livros.append({"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas})
                    except ValueError:
                        print(f"Dados inválidos encontrados: {linha.strip()}. Livro não carregado.")
    except FileNotFoundError:
        print("Arquivo 'biblioteca.txt' não encontrado. Nenhum dado carregado.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
    
    return livros

def validar_int_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor <= 0:
                print("O valor deve ser um número inteiro positivo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! O valor deve ser um número inteiro. Tente novamente.")

def menu():
    livros = []
    
    livros = carregar_livros()

    while True:
        print("\nBem-vindo à Biblioteca Digital!")
        print("Escolha uma opção:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar livros")
        print("4. Salvar dados em arquivo")
        print("5. Carregar dados do arquivo")
        print("6. Sair")

        opcao = input("> ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor: ")
            ano = validar_int_positivo("Ano de publicação: ")
            paginas = validar_int_positivo("Número de páginas: ")
            adicionar_livro(livros, titulo, autor, ano, paginas)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            print("Escolha a ordem de classificação:")
            print("1. Ordenar por ano de publicação")
            print("2. Ordenar por número de páginas")
            opcao_ordenacao = input("Escolha uma opção (1 ou 2): ")
            while opcao_ordenacao not in ["1", "2"]:
                print("Opção inválida! Escolha 1 ou 2.")
                opcao_ordenacao = input("Escolha uma opção (1 ou 2): ")

            ordem = input("Deseja ordenar de forma crescente ou decrescente? (C/D): ").upper()
            while ordem not in ["C", "D"]:
                print("Opção inválida! Escolha C para crescente ou D para decrescente.")
                ordem = input("Deseja ordenar de forma crescente ou decrescente? (C/D): ").upper()

            ordenar_livros(livros, opcao_ordenacao, ordem)
        elif opcao == "4":
            salvar_livros(livros)
        elif opcao == "5":
            livros = carregar_livros()
        elif opcao == "6":
            # Perguntar se o usuário deseja salvar os dados antes de sair
            salvar = input("Deseja salvar os dados antes de sair? (S/N): ").upper()
            if salvar == "S":
                salvar_livros(livros)
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()