# 1. Criação e Manipulação de Listas:
#  Crie uma lista com 10 números inteiros aleatórios e escreva um programa para imprimir o maior e o menor número dessa lista.

import random

lista = [random.randint(1,100) for i in range(10)]

print(f'Os números da lista são {lista}')
print('-'*30)

print(f'O maior número é {max(lista)} e o menor número {min(lista)}')
print('-'*30)

maior = menor = 0

for x, y in enumerate(lista):
    if x == 0:
        mair = menor = y
    if y >= maior:
        maior = y
    if y <= menor:
        menor = y

print(f'O maior número é {maior} e o menor número {menor}')