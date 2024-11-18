# 13. Função com Parâmetros Opcionais:
#  Crie uma função que recebe uma lista e um número opcional. Se o número for fornecido, a
# função deve retornar a lista multiplicada por esse número. Se não for fornecido, a função deve
# retornar a lista original

lista = [1,2,3,4,5,6,7,8,9,10]

def multiplicação(lista, num = None):
    if num != None:
        for x, y in enumerate(lista):
            lista[x] = y * num
    return lista


resultado = multiplicação(lista, 5)

print(resultado)