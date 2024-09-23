# 11. Função com Listas:
#  Escreva uma função que receba uma lista de números e retorne a soma de todos os números pares dessa lista.

import random

lista = [random.randint(1,20) for i in range(10)]

def soma_lista(lista):
    lista_pares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
    print(f'Os números pares da lista são: {lista_pares}')
    return sum(lista_pares)
    


print(lista)

resultado = soma_lista(lista)

print(f'A soma de todos os valores pares da lista é: {resultado}')



   
