# 14. Função que Modifica Dicionários:
#  Escreva uma função que receba um dicionário representando um estoque de produtos
# (chave: nome do produto, valor: quantidade em estoque) e um produto vendido (nome do
# produto e quantidade vendida). A função deve atualizar o estoque conforme a venda e
# informar se a quantidade vendida excede o estoque disponível.

estoque = {
    'Notebook': 3,
    'Smartphone': 5,
    'Fone de Ouvido': 20,
    'Cafeteira': 4
}

def atualização_estoque(dic, produto, numero_vendido):
    if produto not in dic:
        return 'Produto fora de estoque.'
    if numero_vendido > dic[produto]:
        return 'Não há estoque suficiente.'
    if numero_vendido < dic[produto]:
         dic[produto] -= numero_vendido
    return dic

resultado = atualização_estoque(estoque, 'Smartphone', 10)

print(resultado)