# 12 Função que Trabalha com Dicionários:
#  Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e
# seus preços como valores. A função deve retornar o nome do produto mais caro.

produtos = {
    'Notebook': 2500.00,
    'Cafeteira': 200.00,
    'Smartphone': 1500.00,
    'Fone de Ouvido': 300.00
}
    

def produto_mais_caro(dic):
    produto = 0
    nome = ''
    for x, y in dic.items():
        if produto < y:
            produto = y
            nome = x
    return nome

resultado = produto_mais_caro(produtos)

print(f'O produto mais caro é o(a) {resultado}.')