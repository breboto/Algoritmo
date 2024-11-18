
# 10. Dicionário Aninhado:
#  Crie um dicionário para armazenar informações sobre estudantes, onde cada chame é o
# nome de um estudante e o malor é outro dicionário contendo suas notas nas disciplinas
# 'Matemática', 'Português' e 'Ciências'. Permita que o usuário acesse e altere as notas dos
# alunos.


estudantes = {
    'Douglas': {'Matematica': 8.3, 'Portugues': 6.5, 'Ciencias': 8.4},
    'Pedro': {'Matematica': 8.7, 'Portugues': 5.9, 'Ciencias': 9.9},
    'Raphael': {'Matematica': 9.1, 'Portugues': 5.1, 'Ciencias': 2.0}
}



while True:
    print('-'*50)
    print('Menu de Gerenciamento de Notas')
    print('-'*50)
    print('1 - Alunos')
    print('2 - Notas')
    print('3 - Sair')
    print('-'*50)
    
    escolha = int(input('Digite uma opção: '))

    if escolha == 1:
        for estudante, materia in estudantes.items():
            print(f'Aluno: {estudante}')
            for m, nota in materia.items():
                print(f'{m}: {nota}', end = ' - ')
            print('')
    elif escolha == 2:
        
        nome = input('Digite o nome do estudante: ').capitalize()
        while nome not in estudantes:
                print(f'Aluno(a) {nome} não ecnontrado(a).')
                nome = input(f'Digite o nome de um estudante válido: ').capitalize()
                
        materia = input('Digite a matéria: ').capitalize()
        while materia not in estudantes[nome].keys():
                print(f'A matéria {materia} não foi ecnontrada.')
                materia = input(f'Digite o nome de uma matéria válida: ').capitalize()
        
        nova_nota = float(input('Digite a nova nota: '))
    
        if nome in estudantes and materia in estudantes[nome]:
            estudantes[nome][materia] = nova_nota
            print(f'Nota de {materia} de {nome} alterada para {nova_nota}.')

    elif escolha == 3:
        print('Programa encerrado.')
        break

        
        
    else: 
        break
