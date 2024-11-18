# Função para adicionar um aluno
def adicionar_aluno(alunos, nome, notas):
    
    media = sum(notas) / len(notas)
    alunos.append({'nome': nome, 'notas': notas, 'media': media})
    print(f"Aluno {nome} adicionado com sucesso!")

def ordenar_alunos(alunos):
    def quicksort(alunos, left, right):
        if left < right:
            pi = partition(alunos, left, right)
            quicksort(alunos, left, pi - 1)
            quicksort(alunos, pi + 1, right)

    def partition(alunos, left, right):
        pivot = alunos[right]['media']
        i = left - 1
        for j in range(left, right):
            if alunos[j]['media'] > pivot:
                i += 1
                alunos[i], alunos[j] = alunos[j], alunos[i]
        alunos[i + 1], alunos[right] = alunos[right], alunos[i + 1]
        return i + 1

    quicksort(alunos, 0, len(alunos) - 1)

def salvar_em_arquivo(alunos):
    try:
        arquivo = "alunos.txt"
        try:
            with open(arquivo, 'x') as f:
                for aluno in alunos:
                    f.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
            print(f"Os dados foram salvos no arquivo '{arquivo}'.")
        except FileExistsError:
            resposta = input("O arquivo 'alunos.txt' já existe. Deseja sobrescrevê-lo? (s/n): ")
            if resposta.lower() == 's':
                with open(arquivo, 'w') as f:
                    for aluno in alunos:
                        f.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
                print(f"Os dados foram salvos no arquivo '{arquivo}'.")
            else:
                print("Operação cancelada. Os dados não foram salvos.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def exibir_alunos(alunos):
    print("Alunos ordenados por média:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

def visualizar_alunos(alunos):
    print("\nVisualização dos alunos e suas notas:")
    for aluno in alunos:
        notas_formatadas = ', '.join([str(nota) for nota in aluno['notas']])
        print(f"Nome do aluno: {aluno['nome']}")
        print(f"Notas: {notas_formatadas}")
        print()

def menu():
    alunos = []
    while True:
        print("\nMenu:")
        print("1. Adicionar aluno")
        print("2. Exibir alunos ordenados por média")
        print("3. Visualizar alunos e suas notas")
        print("4. Salvar dados em arquivo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do aluno: ")
            while True:
                try:
                    qtd_notas = int(input("Quantas notas deseja inserir (mínimo 2, máximo 5)? "))
                    if qtd_notas < 2 or qtd_notas > 5:
                        print("O número de notas deve ser entre 2 e 5.")
                    notas = []
                    for i in range(qtd_notas):
                        while True:
                            try:
                                nota = float(input(f"Nota {i + 1}: "))
                                if nota < 0 or nota > 10:
                                    raise ValueError("A nota deve estar entre 0 e 10.")
                                notas.append(nota)
                                break
                            except ValueError as e:
                                print(f"Erro: {e}")
                    break
                except ValueError as e:
                    print(f"Erro: {e}")

            adicionar_aluno(alunos, nome, notas)
        elif opcao == '2':
            ordenar_alunos(alunos)
            exibir_alunos(alunos)
        elif opcao == '3':
            visualizar_alunos(alunos)
            print(alunos)
        elif opcao == '4':
            ordenar_alunos(alunos)
            salvar_em_arquivo(alunos)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
