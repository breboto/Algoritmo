#  Criação e Acesso a Dicionários:
#  Crie um dicionário que armazene os dias da semana como chaves e o número de horas trabalhadas em cada dia como valores. Solicite ao usuário a entrada dessas horas e depois
# calcule o total de horas trabalhadas na semana.

dic = {
    'segunda': 0,
    'terça': 0,
    'quarta': 0,
    'quinta': 0,
    'sexta': 0,
    'sábado': 0,
    'domingo': 0
}
# print(dic)

for i in dic:
    horas = float(input(f'Digite o número de horas para {i}: '))
    dic[i] = horas

horas_totais = 0

for x, y in dic.items():
    horas_totais += y


print(f'Foram trabalhadas o total de {horas_totais} horas na semana.')