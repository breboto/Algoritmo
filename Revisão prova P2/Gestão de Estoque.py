estoque = []

def partition(list, left, right, chave):
    try:
        pivot = list[right][chave]
        i = left - 1
        for j in range(left, right):
            if list[j][chave] <= pivot:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i + 1], list[right] = list[right], list[i + 1]
        return i + 1
    except KeyError as e:
        print(f"Erro de chave não encontrada: {e}")
    except Exception as e:
        print(f"Erro na partição: {e}")

# Função Quicksort
def quicksort(list, left, right, chave):
    try:
        if left < right:
            pi = partition(list, left, right, chave)
            quicksort(list, left, pi - 1, chave)
            quicksort(list, pi + 1, right, chave)
    except Exception as e:
        print(f"Erro no quicksort: {e}")

def adicionar_produto(nome, categoria, preco, quantidade):
    try:
        if preco <= 0 or not int:
            print("Erro: O preço deve ser um número positivo.")
            return
        if quantidade < 0:
            print("Erro: A quantidade não pode ser negativa.")
            return
        
        estoque.append({"nome": nome,"categoria": categoria,"preco": preco,"quantidade": quantidade})
        print("Produto adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro ao adicionar produto: {e}")

def atualizar_quantidade(nome_produto, nova_quantidade):
    try:
        produto_encontrado = False
        for produto in estoque:
            if produto["nome"].lower() == nome_produto.lower():
                produto_encontrado = True
                quantidade_atual = produto["quantidade"]
                print(f"Quantidade atual de {produto['nome']}: {quantidade_atual}")
                if nova_quantidade < 0:
                    print("Erro: A quantidade não pode ser negativa.")
                else:
                    produto["quantidade"] = nova_quantidade
                    print(f"Quantidade de {produto['nome']} atualizada para {nova_quantidade}.")
                break
        if not produto_encontrado:
            print(f"Produto {nome_produto} não encontrado no estoque.")
    except ValueError as e:
        print(f"Erro ao atualizar quantidade: {e}")

def listar_produtos():
    try:
        if len(estoque) == 0:
            print("Não há produtos no estoque.")
        else:
            for produto in estoque:
                print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")

def ordenar_produtos(chave, ordem):
    try:
        if chave not in ['preco', 'quantidade']:
            print("Opção inválida para critério de ordenação.")
            return
        if ordem not in ['crescente', 'decrescente']:
            print("Opção inválida para ordem de ordenação.")
            return
        
        crescente = True if ordem == 'crescente' else False
        
        quicksort(estoque, 0, len(estoque) - 1, chave)
        
        if not crescente:
            estoque.reverse() #qual jeito mais facil???

        print(f"Produtos ordenados por {chave} ({'Crescente' if crescente else 'Decrescente'}):")
        listar_produtos()
    except Exception as e:
        print(f"Erro ao ordenar os produtos: {e}")

def salvar_estoque():
    try:
        with open('estoque.txt', 'w') as arquivo:
            for produto in estoque:
                linha = f"{produto['nome']},{produto['categoria']},{produto['preco']:.2f},{produto['quantidade']}\n"
                arquivo.write(linha)
        print("Os dados foram salvos no arquivo 'estoque.txt'.")
    except PermissionError:
        print("Erro: Permissão negada ao tentar salvar os dados no arquivo.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def carregar_estoque():
    try:
        with open('estoque.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) == 4:
                    nome, categoria, preco, quantidade = dados
                    try:
                        preco = float(preco)
                        quantidade = int(quantidade)
                        if preco > 0 and quantidade >= 0:
                            produto = {
                                "nome": nome,
                                "categoria": categoria,
                                "preco": preco,
                                "quantidade": quantidade
                            }
                            estoque.append(produto)
                        else:
                            print(f"Dados inválidos no arquivo para o produto {nome}.")
                    except ValueError as e:
                        print(f"Erro ao processar os dados do produto {nome} no arquivo: {e}")
        print("Dados carregados com sucesso.")
    except FileNotFoundError:
        print("Erro: Arquivo 'estoque.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar os dados do arquivo: {e}")

def menu():
    while True:
        try:
            print("\nBem-vindo ao Sistema de Gestão de Estoque!")
            print("Escolha uma opção:")
            print("1. Adicionar produto")
            print("2. Atualizar quantidade")
            print("3. Listar produtos")
            print("4. Ordenar produtos")
            print("5. Salvar dados em arquivo")
            print("6. Carregar dados do arquivo")
            print("7. Sair")
            
            opcao = input("> ").strip()
            
            if opcao == "1":
                nome = input("Nome do produto: ")
                categoria = input("Categoria: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                adicionar_produto(nome, categoria, preco, quantidade)
            elif opcao == "2":
                nome_produto = input("Digite o nome do produto para atualizar a quantidade: ")
                nova_quantidade = int(input("Digite a nova quantidade: "))
                atualizar_quantidade(nome_produto, nova_quantidade)
            elif opcao == "3":
                listar_produtos()
            elif opcao == "4":
                criterio = input("Ordenar por (1) Preço ou (2) Quantidade? ").strip()
                ordem = input("Ordem (Crescente ou Decrescente)? ").strip().lower()
                if criterio == "1":
                    criterio = "preco"
                elif criterio == "2":
                    criterio = "quantidade"
                ordenar_produtos(criterio, ordem)
            elif opcao == "5":
                salvar_estoque()
            elif opcao == "6":
                carregar_estoque()
            elif opcao == "7":
                salvar = input("Deseja salvar o estoque antes de sair? (S/N): ").strip().upper()
                if salvar == "S":
                    salvar_estoque()
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro inesperado no menu: {e}")
        
menu()
