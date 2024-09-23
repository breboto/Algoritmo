# 17. Calculando a Sequência de Fibonacci 
# Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.

n = 10

fibonacci = [0, 1]

for i in range(2, n):
    proximo_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_numero)

print('Os primeiros 10 números da sequência de Fibonacci são:')
print(fibonacci)