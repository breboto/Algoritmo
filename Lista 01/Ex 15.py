# 15. Números Pares em uma Lista 
# Dada uma lista de números, crie um programa que exiba apenas os números pares.


numeros = [10, 23, 44, 56, 78, 91, 100]

pares = [num for num in numeros if num % 2 == 0]

print('Números pares na lista:', pares)