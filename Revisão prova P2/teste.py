estoque = []

def adicionar_produto(nome, categoria, preco, quantidade):
    try:
        if preco <= 0 or not int:
            print("Errom o preco deve ser um numero positivo")
            return
        if quantidade < 0:
            print("Errom o quantiade deve ser um numero positivo")
            return
        estoque.append({"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade })
        print('produito adicionado com suceddop')
    except Exception as e:
        print(f"erro {e}")

def listar_estoque(lista):
    if len(lista) == 0:
        print("Não há produtos")
    for i in estoque:
        print(f"Nome: {i['nome']}, Categoria: {i['categoria']}, preco: {i['preco']}, quantidade: {i['quantidade']}")

def salvar_estoque():
    try:
        with open ('estoque.txt', 'w') as arquivo:
            for i in estoque:
                arquivo.write(f"{i['nome']},{i['categoria']},{i['preco']:.2f},{i['quantidade']}\n")
                
    
    except PermissionError:
        print('nao tem permissao')
    except Exception as e:
        print(f'erro {e}')

def carregar_estoque(list):
    try:
        with open ('estoque.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for i in linhas:
                nome, categoria, preco, quantidade  = i.strip().split(',')
                list.append({'nome': nome, 'categoria': categoria, 'preco': float(preco), 'quantidade': int(quantidade)})
        print('adicionado')

    except Exception as e:
        print(f"erro {e}")

def ordena(list, opcao, ordem):
    if len(list) == 0:
        print('nÃO HÁ LISTA PARA ORDENARM')
        return
    
    if opcao == "1":
        chave = "preco"
    elif opcao == "2":
        chave = "quantidade"
    else:
        print("opcao invalida")
        return
    
    def partition(list, left, right, chave, ordem):
        pivot = list[right][chave]
        i = left - 1
        for j in range(left, right):
            if (ordem == "C" and list[j][chave] <= pivot) or (ordem == "D" and list[j][chave] >= pivot):
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[right] = list[right], list[i+1]
        return i+1
    
    def quicksort(list, left, right, chave, ordem):
        if left < right:
            pi = partition(list, left, right, chave, ordem)
            quicksort(list, left, pi - 1, chave, ordem)
            quicksort(list, pi + 1, right, chave, ordem)
    
    quicksort(list, 0, len(list) - 1, chave, ordem)
    # listar_estoque(estoque)





# adicionar_produto("mouse", "eletronico", 100, 10)
# adicionar_produto("teclado", "eletronico", 200, 20)
# adicionar_produto("smart", "eletronico", 250, 5)
carregar_estoque(estoque)
ordena(estoque,"2","D")
# print(estoque)
listar_estoque(estoque)
# salvar_estoque()