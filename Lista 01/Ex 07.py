#  7. Fatorial de um Número 
# Peça ao usuário para digitar um número e calcule o fatorial desse número.

def fatorial():

    n1 = int(input('Digite um número inteiro para calcular o fatorial: '))
    
  
 
    if n1 < 0:
        return 'Não há como fazer fatorial de 0!'
    fatorial = 1

    for i in range(1, n1 + 1):
        fatorial *= i
    
    print(f'O fatorial de {n1} é {fatorial}.')


fatorial()