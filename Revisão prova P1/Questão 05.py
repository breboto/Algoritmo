# 5. Remoção de Duplicatas:
#  Escreva um programa que receba uma lista de números do usuário e remova todos os números duplicados, exibindo a lista resultante sem repetições.

import random

lista = []
lista_unicos = []

c = 0

while c < 10:
    n = int(input('Digite um número para adicionar a lista: '))
    lista.append(n)
    c += 1

for i in lista:
    if i not in lista_unicos:
        lista_unicos.append(i)

print(lista)
print('-'*70)
print(lista_unicos)