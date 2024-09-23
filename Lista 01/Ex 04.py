# 4. Calculadora Simples 
# Crie um programa que peça dois números e a operação desejada (+, -, *, /) e exiba o resultado.

def calculadora():
    
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
   
    operacao = input('Digite a operação desejada (+, -, *, /): ')

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
                if n2 != 0:
                    resultado = n1 / n2
                else:
                     return 'Um número não pode ser dividido por 0!'
    else:
        return 'Operação inválida. Por favor, escolha uma das operações: +, -, *, /.'
    
    
    return f'O resultado de {n1} {operacao} {n2} é: {resultado}.'


calculadora()