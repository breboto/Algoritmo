# 12.Contar Vogais em uma String 
# Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.

texto = input('Digite uma string para contar as vogais: ')

vogais = 'aeiouAEIOU'

contador_vogais = 0

for i in texto:
    if i in vogais:
        contador_vogais += 1

print(f'Total de vogais na string: {contador_vogais}')