# 19. Verificar Palíndromo 
# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = input('Digite uma string: ').upper()

invertida = ''
for i in palavra:
    invertida = i + invertida


if palavra == invertida:
    print(f'{palavra} - {invertida} é um palíndromo!')
else:
    print(f'{palavra} - {invertida} não é um palíndromo!')
