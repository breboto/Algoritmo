# 4. Listas Aninhadas:
#  Crie uma lista de listas onde cada sublista deve conter três elementos: o nome de uma pessoa, sua idade e sua cidade. 
# Imprima todas as informações no formato: 'Nome: [Nome], Idade: [Idade], Cidade: [Cidade]'.

lista = [
    ['Pedro', 32, 'Itaúna'],
    ['Douglas', 33, 'Centro'],
    ['Raphael', 28, 'Bacaxá'],
    ['Erica', 22, 'Rio de Areia']
]

for i in lista:
    print(f'Nome: {i[0]}, Idade: {i[1]}, Cidade: {i[2]}')