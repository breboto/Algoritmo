# 3. Verificar Par ou Ímpar 
# Peça ao usuário para digitar um número inteiro e informe se o número é par ou ímpar.

def par_impar():
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'

    print(f'O número {n} é {resultado}.')

par_impar()