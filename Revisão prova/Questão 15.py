# 15. Combinação de Listas, Dicionários e Funções:
#  Escreva uma função que recebe uma lista de dicionários, onde cada dicionário representa
# um estudante com seu nome e uma lista de notas. A função deve calcular a média de cada
# estudante e retornar um novo dicionário com os nomes dos estudantes como chaves e suas
# médias como valores.


alunos= [
    {'Douglas': [8.1, 7.9]},
    {'Pedro': [9.9, 10]},
    {'Erica': [7.9, 6.5]},
    {'Raphael': [6.9, 6.9]},
  
]

def media(lista):
    
    alunos_media = {}
    for i in lista:
        for aluno, nota in i.items():
            media = sum(nota)/len(nota)
            alunos_media[aluno] = media
    return alunos_media

resultado = media(alunos)

print(resultado)
