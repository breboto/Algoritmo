#  5. Média de Notas 
# Peça ao usuário para digitar três notas e calcule a média delas.



def media():

    nota1 = input('Digite a primeira nota: ')
    nota2 = input('Digite a segunda nota: ')
    nota3 = input('Digite a terceira nota: ')
    
    media = (nota1 + nota2 + nota3) / 3
    
    print(f'A média das notas {nota1}, {nota2} e {nota3} é {media:.2f}.')

media()
