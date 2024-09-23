# 9. Verificar Número Primo 
# Peça ao usuário para digitar um número e verifique se ele é primo.

def verificar_primo():
    
    numero = int(input('Digite um número inteiro para verificar se é primo: '))

    if numero <= 1:
        print(f'O número {numero} não é primo.')
        return
    
    eh_primo = True
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
        
    if eh_primo:
        print(f'O número {numero} é primo.')
    else:
        print(f'O número {numero} não é primo.')

verificar_primo()