# 8. Iteração sobre Dicionários:
#  Crie um dicionário que armazene a quantidade de produtos em estoque em uma loja.
# Escreva uma função que verifique se um produto está em estoque e quantas unidades estão
# disponíveis.

estoque = {
    'Notebook': 10,
    'Smartphone': 5,
    'Fone de Ouvido': 20,
    'Cafeteira': 4
}


def consulta_estoque(dic, produto):
    if produto not in dic:
        return 'Não há estoque para este produto.'
    if produto in dic:
        return dic[produto]
    

resultado = consulta_estoque(estoque, 'Fone de Ouvido')

print(f'Há no estoque {resultado} unidades.')
