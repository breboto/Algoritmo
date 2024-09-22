# 1. Criação e Manipulação de Listas:
#  Crie uma lista com 10 números inteiros aleatórios e escreva um programa para imprimir o maior e o menor número dessa lista.

import random

lista = []
for i in range(10):
    numero = random.randint(1,100)
    lista.append(numero)

print(f'Os números da lista são {lista}')
print('-'*30)

print(f'O maior número é {max(lista)} e o menor número {min(lista)}')
print('-'*30)

# maior = menor = 0

# for i, num in enumerate(lista):
#     if num >= maior:
#         maior = num
#     if num <= menor:
#         menor = num

# print(maior)
# print(menor)