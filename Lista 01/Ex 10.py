# 10. Inverter uma String Peça ao usuário para digitar uma string e imprima essa string de forma invertida.

palavra = input('Digite uma string: ')

invertida = ''
for i in palavra:
    invertida = i + invertida

print('String invertida:', invertida)