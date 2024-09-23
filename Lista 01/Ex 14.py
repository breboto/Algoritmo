# 14. Encontrar o Maior Número em uma Lista 
# Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.

entrada = int(input('Digite uma lista 4 números: '))
entrada2 = int(input('Digite outro número: '))
entrada3 = int(input('Digite outro número: '))
entrada4 = int(input('Digite o último número: '))

lista = []

lista.append(entrada)
lista.append(entrada2)
lista.append(entrada3)
lista.append(entrada4)

maior_numero = max(lista)

print(f'O maior número na lista é: {maior_numero}')