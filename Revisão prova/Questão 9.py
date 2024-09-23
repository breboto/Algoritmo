# 9. Conversão entre Listas e Dicionários:
#  Crie duas listas: uma com nomes de países e outra com suas respectivas capitais. Converta
# essas duas listas em um dicionário, onde o país é a chave e a capital é o valor.

paises = ['Brasil', 'Argentina', 'Portugal', 'França', 'Alemanha']

capitais = ['Brasília', 'Buenos Aires', 'Lisboa', 'Paris', 'Berlim']

dic = {}

for i in range(len(paises)):
    dic.update({paises[i] : capitais[i]})
    # dic[paises[i]] = capitais[i]


print(dic)
