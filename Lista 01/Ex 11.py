# 11. Tabuada Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.

numero = int(input('Digite um número para ver sua tabuada: '))

print(f'Tabuada do {numero}:')

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')