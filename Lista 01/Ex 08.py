# 8. Contagem de Números Ímpares 
# Escreva um programa que conta e imprime todos os números ímpares entre 1 e 100.

def contador():
    impares = []
        
    for n in range(1, 101):
        
        if n % 2 != 0:
            impares.append(n)
    
    print('Números ímpares entre 1 e 100:')
    for n in impares:
        print(n)


contador()