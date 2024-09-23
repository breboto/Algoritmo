# 7. Atualização de Dicionários:
#  Dada uma lista de nomes de alunos e suas respectivas notas em uma prova, crie um
# dicionário e permita que o usuário consulte e atualize a nota de um aluno específico


lista= [
    ['DOUGLAS', 8],
    ['PEDRO', 9],
    ['ERICA', 7],
    ['RAPHAEL', 6],
  
]

dic = {}

for x, y in lista:
    dic[x] = y 
    
print (dic)

nome = str(input('Digite o nome do aluno para mudar a nota: ')).upper()
if nome in dic:
    nota = int(input('Digite a nova nota do(a) aluno(a): '))
    dic.update({nome:nota})
else:
    print(f'Aluno(a) {nome} não encontrado(a).')
print (dic)


