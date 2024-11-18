# 16. Funções Recursivas:
#  Escreva uma função de busca binária recursiva
lista = [1, 2, 3, 5, 7, 8, 9, 13, 27, 31, 43, 70]


def busca_binaria(lista, busca, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)-1
    if inicio <= fim:
        m = (inicio + fim) // 2
        if lista[m] == busca:
            return m
        if lista[m] > busca:
            return busca_binaria(lista, busca, inicio, m-1)
        else:
            return busca_binaria(lista, busca, m+1, fim)
    return None


resultado = busca_binaria(lista, 35)

print(resultado)