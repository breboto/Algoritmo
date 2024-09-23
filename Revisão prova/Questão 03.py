# Manipulação de Listas com Laços:
#  Crie uma lista de 10 elementos numéricos e escreva uma função que calcule a média dos números presentes na lista.
import random

lista = [random.randint(1,10) for i in range(10)]


def calculadora_lista(lista):
    n = 0
    c = 0
    for i in lista:
        n += i
        c += 1
        # print(n)
    media = n / c
    return media


resultado = calculadora_lista(lista)
print(lista)
print(resultado)