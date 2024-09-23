#  20. Jogo de Adivinhação 
# Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve 
# tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor que a tentativa do usuário


import random

palpite = int(input('Digite seu palpite, desde que seja um núemro inteiro: '))

numero_secreto = random.randint(1,100)

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print('O número secreto é maior.') 
    elif palpite > numero_secreto:
        print('O número secreto é menor.')
    
    palpite = int(input('Digite seu novo palpite: '))

print(f'Parabéns! Você acertou o número secreto {numero_secreto}.')
