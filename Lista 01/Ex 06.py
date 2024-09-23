# 6. Converter Celsius para Fahrenheit 
# Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.

def celsius_fahrenheit():
    
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    
    fahrenheit = (celsius * 9/5) + 32
    
    print(f'A temperatura de {celsius:.2f} graus Celsius é igual a {fahrenheit:.2f} graus Fahrenheit.')

celsius_fahrenheit()