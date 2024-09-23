# 2. Operações com Listas:
# Escreva um programa que receba 5 nomes de frutas do usuário e os armazene em uma lista. Depois, peça ao usuário que informe uma fruta e verifique se ela está na lista.

lista = []

i = 0

while i < 5:
    fruta = input('Digite uma Fruta: ').upper()
    lista.append(fruta)
    i += 1
   

pesquisa = input('Digite a fruta para saber se ela pertence a lista: ').upper()

if pesquisa in lista:
    print(f'A fruta {pesquisa} está na lista')
else:
    print(f'A fruta {pesquisa} não está na lista')